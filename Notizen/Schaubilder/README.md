# Schaubilder

Interaktive Übersichtsseiten (**Artifacts**), die den Wiki-Bestand visuell zusammenfassen.

> **Sie legen nichts fest.** Jedes Schaubild ist eine Lesehilfe auf den Stand der Quelldateien zum genannten Datum. Im Zweifel gilt immer die Quelle, nie das Schaubild. Gruppierungen und Einordnungen, die nur in einem Schaubild stehen (z. B. die vorausgewählte Anfang-Grenze in der Szenenliste), sind Darstellung, keine Entscheidung.

## Bestand

| Schaubild | Inhalt | Quellen | Stand | Link |
|---|---|---|---|---|
| [Zeitgerüst](Zeitgeruest.html) — *Zehn Jahre, zwei Stränge* | **Wird erzeugt.** Beide Stränge Jahr für Jahr (0 bis +10) nebeneinander, mit den Jahren ohne eigene Szene — dieselben Karten wie die Szenenliste, nach Zeit statt nach Erzählfolge geordnet | [Szenen](../../Plots/Plot-1/Szenen.md), Altersgerüst aus [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md) | 05.09.2026 | [öffnen](https://claude.ai/code/artifact/24282ce3-78a8-4594-a751-c771394502fa) |
| [Kapitelraster](Kapitelraster.html) — *Vor dem Kapitelraster* | **Überholt** — durch die Szenenliste ersetzt. Steht noch auf 43 Einheiten und Jahr −1 | [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md), [Kapitelstruktur](../../Plots/Plot-1/Kapitelstruktur.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/cc1d621a-e67f-4d29-b4c5-7f41ca7bab0d) |
| [Szenenliste](Szenenliste.html) — *Was jede Szene will* | **Wird erzeugt** aus [Szenen.md](../../Plots/Plot-1/Szenen.md), nicht von Hand gepflegt. 45 Szenenkandidaten mit Ziel, Hindernis, Ausgang; gegliedert in Prolog / Anfang / Hauptteil / Schluss (Anfang endet nach „Der Blitz — Tibun“ — Voreinstellung), umsortierbar nach Darstellung und Strang (die gespeicherte Reihenfolge **ist** die Erzählreihenfolge). Modus *Parallel* zeigt **alle Teile** als zwei versetzte Bahnen — Tibun links, Girlin rechts | [Szenen](../../Plots/Plot-1/Szenen.md) — **einzige Quelle** | 05.09.2026 | [öffnen](https://claude.ai/code/artifact/425e137d-9af9-4cbb-9871-ed77ed74df6c) |

## Wie das funktioniert

- Die **HTML-Datei hier im Wiki ist die Quelle**; der Link zeigt auf die veröffentlichte Fassung. **Ausnahme: Szenenliste und Zeitgerüst** — siehe unten.
- **Ausnahme Szenenliste und Zeitgerüst:** Beide werden aus [Szenen.md](../../Plots/Plot-1/Szenen.md) erzeugt und dürfen **nicht von Hand bearbeitet** werden — jede Änderung am HTML ist beim nächsten Lauf weg.
- **Aktualisieren:** Claude bitten, das Schaubild auf den neuen Stand zu bringen. Die veröffentlichte Seite behält dabei **ihre URL** — geteilte Links bleiben gültig, ein Reload zeigt die neue Fassung.
- Beim Aktualisieren wird **auch die Datei hier ersetzt** und das Standdatum in dieser Tabelle nachgezogen.
- Die Seiten sind eigenständiges HTML ohne Abhängigkeiten und lassen sich lokal im Browser öffnen.

## Wann ein Schaubild veraltet

Nach jeder Sitzung, in der Entscheidungen gefallen sind. Betroffen ist:

- das **Kapitelraster-Material**, sobald Beats dazukommen — und vollständig, sobald das echte Raster angelegt ist
- **Szenenliste und Zeitgerüst** brauchen nur einen Lauf des Skripts — sie veralten nicht von selbst, solange er nach jeder Änderung an `Szenen.md` läuft

Alle tragen ihr Standdatum sichtbar im Kopf bzw. Fuß.

## Die erzeugten Schaubilder

Aus dem Wurzelverzeichnis des Wikis:

```
python3 tools/szenenliste.py --nummerieren   # Nummern in Szenen.md nachziehen, dann erzeugen
python3 tools/szenenliste.py                 # nur erzeugen
python3 tools/zeitgeruest.py                 # Zeitgerüst erzeugen
python3 tools/szenenliste.py --pruefen       # nur melden, ob die Datei zum Stand passt
python3 tools/zeitgeruest.py --pruefen
```

Nach einer Änderung an `Szenen.md` beide laufen lassen. `--nummerieren` ist rein mechanisch: es zieht die Szenennummern und die Nummern in der Gliederungstabelle nach — Reihenfolge, Titel und Inhalte bleiben unangetastet.

| Datei | Rolle |
|---|---|
| `tools/wiki.py` | Liest Szenen.md und das Altersgerüst. Beide Generatoren benutzen es, damit sie dieselbe Lesart haben |
| `tools/pruefe_challenges.py` | Prüft `Challenges.md` gegen sich selbst (Statusmarker, Übersicht) — getrennt von den Schaubildern |
| `tools/szenenliste.py` + `szenenliste.template.html` | Szenenliste |
| `tools/zeitgeruest.py` + `zeitgeruest.template.html` | Zeitgerüst |

**Was die Skripte bei jedem Lauf neu rechnen** — und was deshalb nicht mehr still veralten kann: Positionsnummern; die Einträge des Auswahlfelds *Anfang endet nach*; die Grenzen von Prolog und Schluss; alle Kennzahlen; die Wortzahl-Größenordnung; die Jahresachse samt Alter; welche Jahre je Strang **keine** Szene haben; die Zahl der verschiedenen offenen Punkte.

Prolog- und Schlussgrenze werden über den **Szenentitel** gebunden, nicht über eine Nummer — sonst zeigen sie nach dem ersten Umsortieren auf die falsche Szene.

**Was die Skripte nicht können:** Der redaktionelle Text beider Seiten — Einleitung, Hinweis-Kästen, Bändertexte, die Lücken-Liste des Zeitgerüsts, Legenden und Fußzeilen — steht in den Template-Dateien und wird von Hand gepflegt. Er kann veralten, ohne dass es auffällt. Auch Aussehen (CSS) und Verhalten (JS) liegen dort.

Bricht das Format einer Quelle, brechen die Skripte **laut** — sie melden die Stelle und schreiben nichts. Dazu zählt ein Challenge-Titel **ohne Statusmarker**: er würde den Anker verschieben und Links brechen (Regel in [Regeln.md](../Regeln.md#status-marker-in-challengesmd)). Läuft der Marker der Übersicht davon, melden sie es als Hinweis, ohne abzubrechen.

**Die Schaubilder kennen `Challenges.md` nicht** (umgestellt 05.09.2026). Der Szenenkopf in Szenen.md nennt hinter **Offen** die Sachen im Klartext; die Karten zeigen sie so, wie sie dort stehen. Wird `Challenges.md` gelöscht, ändert sich an den Schaubildern nichts.
