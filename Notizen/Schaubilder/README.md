# Schaubilder

Interaktive Übersichtsseiten (**Artifacts**), die den Wiki-Bestand visuell zusammenfassen.

> **Sie legen nichts fest.** Jedes Schaubild ist eine Lesehilfe auf den Stand der Quelldateien zum genannten Datum. Im Zweifel gilt immer die Quelle, nie das Schaubild. Gruppierungen und Einordnungen, die nur in einem Schaubild stehen (z. B. „Art der Arbeit" im Challenge-Board), sind Darstellung, keine Entscheidung.

## Bestand

| Schaubild | Inhalt | Quellen | Stand | Link |
|---|---|---|---|---|
| [Zeitgerüst](Zeitgeruest.html) — *Zehn Jahre, zwei Stränge* | Beide Stränge Jahr für Jahr (0 bis +10) nebeneinander, mit den Jahren ohne eigenen Beat | [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md), [Kapitelstruktur](../../Plots/Plot-1/Kapitelstruktur.md), Szenen (`annular-assets`), [Challenges](../Challenges.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/24282ce3-78a8-4594-a751-c771394502fa) |
| [Challenge-Board](Challenges-Board.html) — *Challenges nach Thema* | Die 96 offenen Challenges nach Sachgebiet und Art der Arbeit, mit Suche und Filter | [Challenges](../Challenges.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/c6322d49-0449-4c58-ba58-709daf014c86) |
| [Figurennetz](Figurennetz.html) — *Wer wen kennt* | Beziehungsnetz beider Stränge; zeigt die Rollen, die noch keine Figur sind | [Menschen/](../../Menschen/README.md), [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md), [Challenges](../Challenges.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/5522a52c-8128-4238-9c3b-71df314cae64) |
| [Kapitelraster](Kapitelraster.html) — *Vor dem Kapitelraster* | **Überholt** — durch die Szenenliste ersetzt. Steht noch auf 43 Einheiten und Jahr −1 | [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md), [Kapitelstruktur](../../Plots/Plot-1/Kapitelstruktur.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/cc1d621a-e67f-4d29-b4c5-7f41ca7bab0d) |
| [Szenenliste](Szenenliste.html) — *Was jede Szene will* | 44 Szenenkandidaten mit Ziel, Hindernis, Ausgang; gegliedert in Prolog / Anfang / Hauptteil / Schluss (Anfang endet nach „Der Blitz“), umsortierbar nach Reihenfolge und Strang. Modus *Parallel* zeigt den Hauptteil als zwei versetzte Bahnen — Tibun links, Girlin rechts | [Zeitleiste](../../Plots/Plot-1/Zeitleiste.md), [Kapitelstruktur](../../Plots/Plot-1/Kapitelstruktur.md) | 04.09.2026 | [öffnen](https://claude.ai/code/artifact/425e137d-9af9-4cbb-9871-ed77ed74df6c) |

## Wie das funktioniert

- Die **HTML-Datei hier im Wiki ist die Quelle**; der Link zeigt auf die veröffentlichte Fassung.
- **Aktualisieren:** Claude bitten, das Schaubild auf den neuen Stand zu bringen. Die veröffentlichte Seite behält dabei **ihre URL** — geteilte Links bleiben gültig, ein Reload zeigt die neue Fassung.
- Beim Aktualisieren wird **auch die Datei hier ersetzt** und das Standdatum in dieser Tabelle nachgezogen.
- Die Seiten sind eigenständiges HTML ohne Abhängigkeiten und lassen sich lokal im Browser öffnen.

## Wann ein Schaubild veraltet

Nach jeder Sitzung, in der Entscheidungen gefallen sind. Betroffen ist:

- das **Zeitgerüst**, sobald sich Beats, Jahre oder das Altersgerüst ändern
- das **Challenge-Board**, sobald Challenges dazukommen, gelöst oder gestrichen werden
- das **Figurennetz**, sobald Figuren Namen bekommen, dazukommen oder wegfallen
- das **Kapitelraster-Material**, sobald Beats dazukommen — und vollständig, sobald das echte Raster angelegt ist
- die **Szenenliste**, sobald Ziele oder Hindernisse entschieden werden (jedes `???` dort ist eine offene Stelle)

Alle tragen ihr Standdatum sichtbar im Kopf bzw. Fuß.
