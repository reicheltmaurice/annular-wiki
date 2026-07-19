# Annular × Claude Code — Arbeitsanleitung

## Modellwahl

| Modell | Wann benutzen |
|---|---|
| **Sonnet** (Standard) | Alles: Brainstorming, Recherche, Szenen, Korrekturen |
| **Opus** | Nur für kritische Entscheidungen: Schlüsselszenen, komplexe Historik-Recherche, Plotprobleme |
| **Haiku** | Mechanisches: Datei suchen, Namen prüfen, kleine Edits |

Für dieses Projekt: **Sonnet als Default**. Opus sparend einsetzen (teurer/mehr Token).

---

## Arbeitsmodi — wie du Anfragen formulierst

**Brainstormen**
> "Gib mir 3 verschiedene Ansätze für [Problem]. Mindestens einer soll unkonventionell sein."

**Schreiben**
> "Schreib einen Roh-Entwurf: [Szene]. Priorität: emotionale Wahrheit, ~500 Wörter."

**Kritisieren** ← wertvollster Modus
> "Lies [Szene/Idee] und sag mir: Wo verliert sie Spannung? Was ist unglaubwürdig?"

**Historik-Check**
> "Ist [Idee/Technologie/Objekt] für ~900 n.Chr. plausibel?"

**Konsistenz-Check**
> "Prüf alle Dateien in [Ordner] — widerspricht [neue Idee] irgendetwas?"

---

## Szenenprozess

Nie direkt zur Endfassung. Schritte:
1. **Outline** — Was passiert? Ein Absatz.
2. **Rohfassung** — Ausschreiben, Fokus auf Rhythmus.
3. **Kritik** — Was ist schwach?
4. **Revision** — Gezielt verbessern.

---

## Memory sinnvoll nutzen

Wichtige Entscheidungen explizit speichern:
> "Wir haben entschieden: [X]. Bitte in der Memory speichern."

Dann ist es in jeder zukünftigen Session verfügbar.

---

## Mobiles Brainstorming (claude.ai unterwegs)

Repo ist öffentlich → Claude.ai kann Dateien direkt laden. Einfach die URL in den Chat einfügen:

```
https://raw.githubusercontent.com/reicheltmaurice/annular-wiki/main/CLAUDE.md
https://raw.githubusercontent.com/reicheltmaurice/annular-wiki/main/Zeitleiste.md
https://raw.githubusercontent.com/reicheltmaurice/annular-wiki/main/Notizen/Offene-Challenges.md
```

**Einstiegsformel für neue mobile Session:**
> "Lies diese drei Dateien: [URLs]. Du bist mein Brainstorming-Partner für diese Welt. Kommuniziere auf Deutsch."

**Ideen sichern:** Gute Einfälle per Working Copy oder GitHub App ins Repo schreiben (z. B. in die passende Fachdatei oder als kurzen Notiz-Commit) — am Laptop dann mit Claude Code einarbeiten.

---

## Token sparen

- Kurze, präzise Anfragen statt langer Erklärungen.
- Nur die relevanten Dateien lesen lassen, nicht den ganzen Wiki.
- Für einfache Edits: direkt sagen was geändert werden soll.
- Haiku für mechanische Aufgaben nutzen.
