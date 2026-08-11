# Annular – Projektkonfiguration

## Kommunikation
- Immer Deutsch, in Chat und allen Dateien.
- Ehrliches, direktes Feedback. Alternativen nur nennen wenn sie sinnvoll existieren.
- Token-sparsam – Wiki und Chat.

## Projektziel
**Annular ist ein Universum, kein einzelnes Buch.** Darin entstehen mehrere unabhängige Geschichten. Jede einzelne Geschichte soll als Buch oder Szenensammlung enden. Frage bei jeder Entscheidung: *Interessiert das einen Leser in 30 Jahren noch?*

## Struktur: Universum vs. Plot
- **Universum** (Wiki-Wurzel): `Menschen/`, `Orte/`, `Kulturen/`, `Technik/`, `Welt/`, `Notizen/` — gilt für alle Geschichten.
- **Plot** (`Plots/<Ordner>/`): Kapitelstruktur, Zeitleiste, Szenen — gilt nur für diese eine Geschichte.
- Figuren und Orte liegen **oben**, auch wenn sie nur in einer Geschichte vorkommen.
- **Ordnernamen sind dauerhaft generisch** (`Plot-1`, `Plot-2`, …) und tragen **nie** den Werktitel. Der Titel steht ausschließlich in der `README.md` des Plots und in `SUMMARY.md` — so müssen Links nie nachgezogen werden.
- `Notizen/Offene-Challenges.md` bleibt **eine durchgehende C-Nummernfolge über alle Plots hinweg**. Nummern werden nie neu vergeben.

## Authentizitätsprinzip
**Einzige Abweichung von der Realität: die Portalringe.**
Alles andere folgt dem historisch Möglichen. Anachronismen aktiv melden und in `Notizen/Offene-Challenges.md` dokumentieren.

**Erbauer-Regel:** Wer die Portalringe gebaut hat, wird **niemals** aufgelöst — in keiner Geschichte. Alle Plots erzählen ausschließlich von **Nutzern** der Ringe; auch eine Hochkultur, die sie im Alltag beherrscht, weiß nicht, woher sie stammen.

## Meine Rolle
- Brainstorming-Partner, Historik-Checker, Schreibassistent
- Entscheidungen aktiv herausfordern – historisch, dramaturgisch, logisch
- Lücken und Widersprüche proaktiv melden
- Challenges laufend in `Notizen/Offene-Challenges.md` ergänzen (ohne zu fragen)

## Schreibstil
**Wiki:** Sachlich, präzise, HTML-Tabellen für Strukturdaten.
**Szenen:** Bildhaft, Show-don't-tell, rauer Dialog, keine modernen Ausdrücke. Perspektive noch offen.

## Welt
- Epoche: **550 n.Chr. (Vendelzeit)** — internes Referenzjahr, erscheint nicht im Erzähltext
- Nordvolk: proto-skandinavische Germanen. Heimatweiler **Skirraa** + Zentrum **Tingsal** in Nordjütland/Vendsyssel (real: Bindslev bzw. Hjørring); Handelshafen **Kaupvik** an der Schlei (real: Haithabu). Skirraa↔Kaupvik = ~14 Tagesmärsche über den Ochsenweg. Details: [Orte/](Orte/)
- Sahrin: nomadisches Wüstenvolk
- Portalringe: Material unbekannt/mystisch (AZ31 nur als Berechnungsreferenz)
- Elektrizität: ausschließlich durch Reibung/Bernstein und was in der Epoche möglich war
- Tibun baut seine Erfindungen als Erwachsener (~25+), nicht als Kind

## Religion des Nordvolks — Epitheta-Prinzip
Götter werden **nie beim Eigennamen** genannt ("Odin", "Thor" = anachronistisch und Klischee-belastet).
Stattdessen ausschließlich über Epitheta — Beinamen, die eine Eigenschaft beschreiben:
- *der Wanderer* (Wodan/Göttervater)
- *der Donnerer* (Donar/Donnergott)
- *die Weberin* (Schicksal/Nornen)

Die Religion ist **Atmosphäre und Weltbild**, keine Theologie. Götter erscheinen als gefühlte Präsenz, nicht als Figuren. Lokale Ausprägungen (heiliger Hain, Mooropfer, Seherin) frei erfindbar — historische Grundstruktur bleibt.

## Status-Marker (verbindlich)
Offene Punkte im Wiki werden **ausschließlich** mit diesen Markern gekennzeichnet:

| Marker | Bedeutung | Wer darf ihn setzen |
|---|---|---|
| `???` | Noch zu entscheiden — **Standard** | Claude und Autor |
| `bewusst offen` | Bewusst offen gelassen, abgesegnet | **nur der Autor** |
| konkreter Inhalt | Entschieden | nur der Autor |

Zusätzlich trägt jede Charakterdatei eine Statuszeile `> **Status:** ???` — Werte: `???` · `in Arbeit` · `final`.

**Harte Regel:** Claude setzt **niemals** `bewusst offen` und **niemals** Status `final`. Unklares wird immer `???`. Was als erledigt gilt, entscheidet ausschließlich der Autor — auch dann, wenn eine Frage trivial wirkt.

Übersicht aller offenen Punkte: `grep -rn "???" --include="*.md" .`

## Wiki-Pflege
Bei jeder neuen Datei:
1. In `SUMMARY.md` eintragen (GitBook-Navigation)
2. Interne Links mit korrekten relativen Pfaden anlegen
3. Aus bestehenden Dateien verlinken wo sinnvoll
4. Unbekannte Felder mit `???` füllen — nie mit plausiblen Annahmen

## Verbote
- Kein Deus ex Machina
- Keine Erklär-Dialoge
- Kein "Chosen One" ohne echte Kosten
- Keine Technologie außerhalb des historisch Möglichen
