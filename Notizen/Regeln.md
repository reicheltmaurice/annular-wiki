# Regeln & Prüfliste

Wird gegen Szenen, Artikel und Charakterbeschreibungen geprüft.
Neue Regeln laufend ergänzen — keine Begründungen, nur die Regel selbst.

---

## Authentizität

- Die einzige Abweichung von der historischen Realität sind die Portalringe — alles andere muss historisch möglich sein
- Epoche: **550 n.Chr. (Vendelzeit)** — internes Referenzjahr, erscheint nicht im Erzähltext
- Anachronismen sofort in `challenges.md` dokumentieren
- Keine Technologie, die für 550 n.Chr. nicht belegt oder plausibel herleitbar ist
- Elektrizität nur durch Reibung/Bernstein und was in der Epoche möglich war

## Religion

- Götter erscheinen nie beim Eigennamen ("Wodan", "Donar" = nur interne Referenz — im Text verboten)
- Ausschließlich Epitheta: *der Wanderer*, *der Donnerer*, *die Weberin* — oder neue, passend erfundene
- Spezifisch altnordische Konzepte erscheinen nicht im Text (Valhalla → *Weltenbaum*, Asgard → *die obere Welt* o.ä.)
- Religion ist Atmosphäre und Weltbild — keine Theologie, keine Erklärungen
- Erlaubt: heilige Haine, Mooropfer, Seherin, Runen, Schicksalsvorstellung

## Status-Marker

> Verbindlich, ebenfalls in `CLAUDE.md` verankert (nur die wird pro Session automatisch geladen).

- `???` = noch zu entscheiden — **Standardzustand** für alles Unbekannte
- `bewusst offen` = bewusst offen gelassen und abgesegnet — **setzt nur der Autor**
- konkreter Inhalt = entschieden — **setzt nur der Autor**
- Charakterdateien tragen `> **Status:** ???` — Werte `???` · `in Arbeit` · `final`; `final` setzt nur der Autor
- Claude schreibt bei Unklarheit immer `???`, nie `bewusst offen`, nie `final`
- Keine plausiblen Annahmen als Feldinhalt — lieber `???`
- Vollständige Liste offener Punkte: `grep -rn "???" --include="*.md" .`

## Was in Challenges.md gehört

> Entschieden 05.09.2026 vom Autor.

**Challenges sind ausnahmslos für den Buchinhalt.** Was die Welt, die Figuren, die Handlung oder die historische Plausibilität betrifft, wird als Challenge geführt.

**Nicht in die Challenges gehören:** Probleme des Wikis selbst, der Werkzeuge oder der Schaubilder — Dateistruktur, Links und Anker, Formatkonventionen, Generatoren, Artifacts. Solche Punkte werden **sofort gelöst**, nicht notiert. Braucht es dafür eine Entscheidung, wird sie im Chat erfragt.

Bereits vergebene C-Nummern technischer Art bleiben stehen ([C-137 ✓](Challenges.md#c-137-detailabschnitte-ab-c-099-stehen-unter-der-falschen-überschrift-), [C-148 ✓](Challenges.md#c-148-der-statusmarker-im-titel-bricht-die-anker-)) — Nummern werden nie neu vergeben.

## Verwiesen wird nur in eine Richtung

> Entschieden 05.09.2026 vom Autor.

**Challenges sind ein Werkzeug des Autors, kein Teil des Wikis.** Sie dürfen ins Wiki verweisen — das Wiki verweist nicht zurück.

- **In Wiki-Artikeln** (`Menschen/`, `Orte/`, `Kulturen/`, `Technik/`, `Welt/`) steht **kein Link auf eine Challenge**. Was dort offen ist, wird mit `???` markiert — das genügt, um es wiederzufinden.
- **In Challenges.md** wird weiter auf die betroffenen Wiki-Stellen verlinkt; dort ist der Verweis der Zweck.
- Wer von einer offenen Stelle zur Challenge will, findet sie über `grep -rn "???" --include="*.md" .` oder über die Übersicht in Challenges.md.

Ein Leser des Wikis soll den Artikel lesen können, ohne über Arbeitsstände zu stolpern.

## Status-Marker in Challenges.md

> Entschieden 05.09.2026 ([C-148 ✓](Challenges.md#c-148-der-statusmarker-im-titel-bricht-die-anker-)). Diese Regel ist **technisch**, nicht kosmetisch: wird sie gebrochen, brechen Links.

**Jede Überschrift im Detailteil endet auf ein Leerzeichen plus genau einen Marker:**

| Marker | Bedeutung |
|---|---|
| `○` | offen |
| `✓` | entschieden |
| `✗` | gestrichen oder zurückgezogen |

```
### C-034: Tibuns Lebensgrundlage während der Wanderschaft ○
```

- **Kein Eintrag ohne Marker.** Ein fehlender Marker verschiebt den Anker und bricht jede Verlinkung auf die Challenge.
- **Kein Zusatzwort nach dem Marker** — nicht `✗ gestrichen`, nicht `✓ (Kernfrage)`. Der Marker ist das letzte Zeichen der Zeile. Begründungen stehen im Abschnittstext.
- **Genau ein Leerzeichen** davor, nie zwei, nie keins.
- Der **Linktext in der Übersicht** trägt denselben Marker; der Anker dort endet immer auf `-`.
- Maßgeblich für den Status ist die **Übersicht** am Dateikopf ([C-137 ✓](Challenges.md#c-137-detailabschnitte-ab-c-099-stehen-unter-der-falschen-überschrift-)). Marker und Übersicht dürfen nicht auseinanderlaufen.

**Warum das trägt:** Der Slugger wirft das Markerzeichen weg und macht aus dem Leerzeichen davor einen Bindestrich. Der Anker endet dadurch immer auf `-`, egal welcher der drei Marker steht — ein Statuswechsel `○ → ✓` lässt ihn unverändert.

**Geprüft wird das maschinell:** `python3 tools/zeitgeruest.py --pruefen` bricht ab, wenn ein Titel keinen Marker trägt, und meldet jede Abweichung zwischen Marker und Übersicht.

## Charaktere

- Tibun erfindet und baut als Erwachsener (~25+) — mit **16** nur die Entdeckung des Bernstein-Effekts, wenige Tage vor Girlins Verschwinden (beides Jahr 0, geändert 04.09.2026)
- Keine "Chosen One"-Momente ohne echte Kosten
- Keine Erklär-Dialoge — Figuren erklären einander nichts, was sie beide wissen
- Das Feld **Inspiration** meint **ausschließlich das Äußere** (Gesicht, Statur, Auftreten) — nie Charakter, Rolle oder Wesen der Vorlage. Aus einer Inspiration darf nichts über die Figur abgeleitet werden.

## Namen

- **Nordvolk:** zweigliedrige Vollnamen aus festem Elementvorrat, im Alltag Kurzformen (Erstglied + `-un` m. / `-in`,`-a` w. / `-i`). Kein Familienname, sondern Vatersname `-sun`/`-dohtar`. **Keine Götterelemente** (`Thor-`, `Tiw-`, `Ing-`) — sie unterlaufen das Epitheta-Prinzip. Muster und Elementvorrat: [C-092](Challenges.md#c-092-namenssystem-des-nordvolks-)
- **Kel Aman:** libysch-berberisch. Frauennamen umklammert ein `t`, Männernamen enden konsonantisch oder auf `-an`/`-en`, Abstammung mit `u-`/`ult-`, Gruppen mit `Kel-`. Siehe [C-090](Challenges.md#c-090-kel-aman--eigenname-und-namenssystem-)
- **Keine Sonderzeichen — überall im Wiki.** Alles wird mit deutscher Tastatur geschrieben: kein Thorn, kein Eth, keine Längenstriche über Vokalen. Stattdessen `th`, `d` und einfache Vokale.

## Schreiben

- Show-don't-tell — keine Gefühlsberichte, nur Handlung und Bild
- Kein moderner Sprachgebrauch im Erzähltext oder Dialog
- Kein Deus ex Machina
- Rauer, knapper Dialog — keine Reden

## Dramaturgie

- Frage bei jeder Entscheidung: *Interessiert das einen Leser in 30 Jahren noch?*
- Kein Deus ex Machina
- Jede Lösung hat eine Vorgeschichte — nichts taucht ohne Vorbereitung auf
