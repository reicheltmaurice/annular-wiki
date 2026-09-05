#!/usr/bin/env python3
"""Gemeinsames Lesen der Wiki-Quellen fuer die erzeugten Schaubilder.

Wird von tools/szenenliste.py und tools/zeitgeruest.py benutzt, damit beide
dieselbe Lesart haben. Enthaelt keine Darstellung -- nur Lesen und Rechnen.
"""

import re
import sys
from pathlib import Path

WURZEL = Path(__file__).resolve().parent.parent
SZENEN = WURZEL / "Plots" / "Plot-1" / "Szenen.md"
CHALLENGES = WURZEL / "Notizen" / "Challenges.md"
ZEITLEISTE = WURZEL / "Plots" / "Plot-1" / "Zeitleiste.md"


def fehler(text):
    print("FEHLER: " + text, file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------- Szenen.md

SZENE = re.compile(
    r"^### (?P<nr>\d+) · (?P<titel>.+?)\n"
    r"\n> \*\*POV:\*\* (?P<pov>\S+) · \*\*Jahr (?P<jahr>[+\d]+)\*\* · \*\*Challenges:\*\* (?P<ch>.+?)\n"
    r"\n(?P<satz>.+?)\n"
    r"\n- \*\*Will:\*\* (?P<will>.+?)\n"
    r"- \*\*Hindernis:\*\* (?P<hindernis>.+?)\n"
    r"- \*\*Ausgang:\*\* (?P<ausgang>.+?)\n",
    re.M,
)


def lies_szenen(md):
    """Liest die Szenenabschnitte. Reihenfolge der Datei = Erzaehlreihenfolge."""
    szenen = [m.groupdict() for m in SZENE.finditer(md)]
    if not szenen:
        fehler("keine Szene in %s erkannt -- Format geaendert?" % SZENEN)

    ueberschriften = len(re.findall(r"^### \d+ · ", md, re.M))
    if ueberschriften != len(szenen):
        fehler(
            "%d Szenen-Ueberschriften, aber nur %d vollstaendig geparst. "
            "Mindestens eine Szene weicht vom Format ab." % (ueberschriften, len(szenen))
        )

    for i, s in enumerate(szenen, start=1):
        if int(s["nr"]) != i:
            fehler(
                "Nummerierung nicht lueckenlos: an Position %d steht Szene %s (%s). "
                "Mit --nummerieren nachziehen." % (i, s["nr"], s["titel"])
            )
        s["pos"] = i
        s["jahr_zahl"] = int(s["jahr"].lstrip("+"))
        if s["pov"] not in ("Tibun", "Girlin"):
            fehler("unbekannter POV %r in Szene %d" % (s["pov"], i))
        s["cs"] = [int(n) for n in re.findall(r"C-(\d{3})", s["ch"])]

    titel = [s["titel"] for s in szenen]
    doppelt = {t for t in titel if titel.count(t) > 1}
    if doppelt:
        fehler(
            "doppelte Szentitel: %s. Grenzen werden ueber den Titel gebunden, "
            "deshalb muessen Titel eindeutig sein." % ", ".join(sorted(doppelt))
        )
    return szenen


def lies_grenze(md, teil):
    """Szenentitel und genannte Nummer aus einer Zeile der Gliederungstabelle."""
    zeile = re.search(r"^\| %s \| (.+?) \|" % teil, md, re.M)
    if not zeile:
        fehler("Zeile %r fehlt in der Gliederungstabelle von Szenen.md" % teil)
    text = zeile.group(1)
    klammer = re.search(r"\(([^)]+)\)", text)
    nummer = re.search(r"Szene (\d+)", text)
    return (
        klammer.group(1).strip() if klammer else None,
        int(nummer.group(1)) if nummer else None,
    )


def position_von(szenen, titel, wozu):
    for s in szenen:
        if s["titel"] == titel:
            return s["pos"]
    fehler("%s: keine Szene mit dem Titel %r in Szenen.md" % (wozu, titel))


def offen(wert):
    return wert.strip() == "???"


def kennzahlen(szenen):
    voll = [s for s in szenen if not any(offen(s[k]) for k in ("will", "hindernis", "ausgang"))]
    ohne_h = [s for s in szenen if offen(s["hindernis"])]
    zustand = [s for s in ohne_h if offen(s["will"])]
    return {
        "N": len(szenen),
        "T": sum(1 for s in szenen if s["pov"] == "Tibun"),
        "G": sum(1 for s in szenen if s["pov"] == "Girlin"),
        "VOLL": len(voll),
        "OHNE_H": len(ohne_h),
        "ZUSTAND": len(zustand),
    }


# ------------------------------------------------------------ Challenges.md


def lies_challenges():
    """Titel und Status je C-Nummer.

    **Massgeblich ist die Uebersicht am Kopf der Datei**, nicht der Marker am
    Detailtitel -- so festgelegt in C-137. Ein Marker im Titel wuerde ausserdem
    den Anker aendern und bestehende Links brechen.
    """
    c = CHALLENGES.read_text(encoding="utf-8")
    if "## Alle Challenges nach Nummer" not in c:
        fehler("Challenges.md: Abschnitt 'Alle Challenges nach Nummer' fehlt")
    uebersicht = c.split("## Alle Challenges nach Nummer")[0]
    try:
        block_offen = uebersicht.split("**Offen**")[1].split("**Gelöst / Entschieden**")[0]
        block_geloest = uebersicht.split("**Gelöst / Entschieden**")[1]
    except IndexError:
        fehler("Challenges.md: Uebersicht hat nicht die Bloecke 'Offen' und 'Gelöst / Entschieden'")
    ist_offen = {int(n) for n in re.findall(r"^- \[C-(\d{3})", block_offen, re.M)}
    ist_geloest = {int(n) for n in re.findall(r"^- \[C-(\d{3})", block_geloest, re.M)}

    doppelt = ist_offen & ist_geloest
    if doppelt:
        fehler("Challenges.md: in beiden Uebersichtslisten: %s" % sorted(doppelt))

    # Codebloecke ausblenden -- dort stehen Beispieltitel, keine Abschnitte
    ohne_code = re.sub(r"^```.*?^```", "", c, flags=re.M | re.S)

    challenges = {}
    ohne_marker = []
    for m in re.finditer(r"^### C-(\d{3}): (.+)$", ohne_code, re.M):
        nr = int(m.group(1))
        titel = m.group(2).strip()
        # Jeder Titel endet auf ' ' + genau einem Marker (Regeln.md, C-148).
        # Das Leerzeichen davor haelt den Anker stabil: der Slugger wirft das
        # Zeichen weg und macht aus dem Leerzeichen einen Bindestrich -- der
        # Anker endet damit immer auf '-', egal welcher Marker steht.
        letzt = re.search(r" ([✓✗○])$", titel)
        if not letzt:
            ohne_marker.append(nr)
            continue
        challenges[nr] = {
            "titel": titel[:-2].strip(),
            "geloest": nr in ist_geloest,
            "gelistet": nr in ist_offen or nr in ist_geloest,
            "marker": letzt.group(1),
            "anker": anker(m.group(0)[4:]),
        }

    if ohne_marker:
        fehler(
            "Challenges.md: diese Titel tragen keinen Statusmarker am Ende -- das "
            "bricht ihren Anker (siehe Regeln.md): %s" % ohne_marker
        )

    nicht_gelistet = sorted(n for n, d in challenges.items() if not d["gelistet"])
    if nicht_gelistet:
        fehler(
            "Challenges.md: diese Nummern haben einen Detailabschnitt, stehen aber in "
            "keiner Uebersichtsliste: %s" % nicht_gelistet
        )
    ohne_detail = sorted((ist_offen | ist_geloest) - set(challenges))
    if ohne_detail:
        fehler(
            "Challenges.md: diese Nummern stehen in der Uebersicht, haben aber keinen "
            "Detailabschnitt: %s" % ohne_detail
        )
    return challenges


def anker(ueberschrift):
    """Ankername, wie GitHub/GitBook ihn aus einer Ueberschrift bildet."""
    t = ueberschrift.strip().lower()
    t = "".join(ch for ch in t if ch.isalnum() or ch in " -_")
    return t.replace(" ", "-")


def pruefe_status(szenen, challenges):
    """Meldet Unstimmigkeiten rund um den Challenge-Status. Bricht nicht ab."""
    warnungen = []
    for s in szenen:
        for nr in s["cs"]:
            if nr not in challenges:
                warnungen.append("Szene %d (%s) nennt C-%03d -- gibt es nicht" % (s["pos"], s["titel"], nr))
                continue
            hat_haken = ("C-%03d ✓" % nr) in s["ch"]
            if hat_haken != challenges[nr]["geloest"]:
                warnungen.append(
                    "Szene %d (%s): C-%03d steht als %s, laut Challenges-Uebersicht ist es %s"
                    % (s["pos"], s["titel"], nr,
                       "gelöst" if hat_haken else "offen",
                       "gelöst" if challenges[nr]["geloest"] else "offen")
                )
    for nr, d in sorted(challenges.items()):
        passt = d["marker"] in ("✓", "✗") if d["geloest"] else d["marker"] == "○"
        if not passt:
            warnungen.append(
                "C-%03d: Uebersicht sagt %s, der Detailtitel trägt %s"
                % (nr, "gelöst" if d["geloest"] else "offen", d["marker"])
            )
    return warnungen


# ----------------------------------------------------------- Zeitleiste.md


def lies_alter():
    """Startalter aus dem Altersgeruest der Zeitleiste; prueft alle Stuetzstellen.

    Die Zeitleiste nennt Tibun als Ankerfigur (Alter = 16 + Jahr) und fuehrt eine
    Tabelle mit den Jahren 0, +1, +9 und +10. Hier wird das Startalter gelesen und
    gegen jede Stuetzstelle geprueft -- weicht eine ab, bricht es.
    """
    z = ZEITLEISTE.read_text(encoding="utf-8")
    kopfzeile = re.search(r"<tr><th>Figur</th>(.*?)</tr>", z, re.S)
    if not kopfzeile:
        fehler("Zeitleiste.md: Kopfzeile des Altersgeruests nicht gefunden")
    spalten = re.findall(r"<th>(.*?)</th>", kopfzeile.group(1), re.S)
    jahre = []
    for sp in spalten:
        m = re.search(r"\(([+-]?\d+)\)|Jahr (\d+)", re.sub(r"<[^>]+>", "", sp))
        jahre.append(int((m.group(1) or m.group(2))) if m else None)

    alter = {}
    for figur in ("Tibun", "Girlin"):
        zeile = re.search(r"<tr><td>%s</td>(.*?)</tr>" % figur, z, re.S)
        if not zeile:
            fehler("Zeitleiste.md: Zeile %r im Altersgeruest fehlt" % figur)
        werte = [re.sub(r"<[^>]+>", "", w).strip() for w in re.findall(r"<td>(.*?)</td>", zeile.group(1), re.S)]
        stuetz = {j: int(w) for j, w in zip(jahre, werte) if j is not None and w.isdigit()}
        if not stuetz:
            fehler("Zeitleiste.md: keine lesbaren Altersangaben für %s" % figur)
        start = min(stuetz.items())[1] - min(stuetz)
        for j, a in stuetz.items():
            if start + j != a:
                fehler(
                    "Zeitleiste.md: Altersgerüst für %s ist nicht linear -- Jahr %+d nennt %d, "
                    "aus Jahr %+d folgt %d." % (figur, j, a, min(stuetz), start + j)
                )
        alter[figur] = start
    return alter
