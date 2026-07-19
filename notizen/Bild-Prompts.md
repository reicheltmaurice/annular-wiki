# Bild-Prompts

Prompts für KI-Bildgeneratoren. **Autorenebene** — kein Story-Inhalt, keine Kanon-Quelle. Maßgeblich bleibt immer die Fachdatei (für den Ring: [Portalringe.md](../technik/Portalringe.md)).

**Prompts sind englisch.** Bildgeneratoren arbeiten bei Material-, Licht- und Kamerabegriffen deutlich präziser auf Englisch — bewusste Ausnahme von der Deutsch-Regel, da Werkzeug-Input.

---

## Portalring — Kanon-Grundlage

Was jeder Ring-Prompt korrekt treffen muss:

<table>
  <caption>Verbindliche Vorgaben für Ring-Darstellungen</caption>
  <tbody>
    <tr>
      <td><strong>Lage</strong></td>
      <td>Flach liegend, Öffnung zeigt zum Himmel</td>
      <td>Kein aufrecht stehendes „Tor"</td>
    </tr>
    <tr>
      <td><strong>Silhouette</strong></td>
      <td>Wie der Eine Ring (PJ / Jens Hansen): massiver Fingerring, skaliert</td>
      <td>Keine flachen Seitenwände, kein Brunnenrand, kein Rechteckprofil, kein rundes Rohr</td>
    </tr>
    <tr>
      <td><strong>Querschnitt</strong></td>
      <td><strong>Oval</strong> (voll gerundet) — axial höher als radial dick</td>
      <td>1,05 m hoch × 0,405 m dick; nicht kreisrund (sonst Donut-Schlauch)</td>
    </tr>
    <tr>
      <td><strong>Außen-Ø</strong></td>
      <td>3,81 m</td>
      <td><a href="../notizen/Offene-Challenges.md">C-007</a></td>
    </tr>
    <tr>
      <td><strong>Innere Öffnung</strong></td>
      <td>3,00 m</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Wandstärke (radial)</strong></td>
      <td>0,405 m</td>
      <td>Dicke des Ringkörpers von innen nach außen</td>
    </tr>
    <tr>
      <td><strong>Höhe / Bandbreite (axial)</strong></td>
      <td>1,05 m</td>
      <td>Reicht einem Erwachsenen über die Hüfte</td>
    </tr>
    <tr>
      <td><strong>Optik</strong></td>
      <td>Wie gebürstetes Aluminium, matt silbrig-grau</td>
      <td><a href="../notizen/Offene-Challenges.md">C-035</a> — kein Spiegelglanz, kein Gold</td>
    </tr>
    <tr>
      <td><strong>Alterung</strong></td>
      <td>Keine — kein Rost, keine Patina, keine Kratzer</td>
      <td><a href="../notizen/Offene-Challenges.md">C-036</a></td>
    </tr>
    <tr>
      <td><strong>Bewuchs</strong></td>
      <td>Moos/Flechte liegen <em>auf</em> der Oberfläche</td>
      <td>Darunter makellos</td>
    </tr>
    <tr>
      <td><strong>Runen</strong></td>
      <td>Flache gemeißelte Nuten, unbekannte Schrift</td>
      <td>Kein Futhark, kein Tengwar, kein Knotwork</td>
    </tr>
    <tr>
      <td><strong>Inaktiv</strong></td>
      <td>Runen dunkel und leer</td>
      <td>Kein grünes Leuchten</td>
    </tr>
  </tbody>
</table>

**Der Bildkern:** Der Kontrast zwischen uraltem Bewuchs und der ungealterten Oberfläche darunter. Nicht der Fund ist unheimlich, sondern der Moment, in dem das Moos weggezogen wird.

**Fallstricke:**
- Generatoren stellen den Ring gern *aufrecht* hin (Stargate-Reflex) und ignorieren die Höhe von 1,05 m.
- **`well-curb` / Rechteckprofil → flache Seiten.** Stattdessen: `One Ring`, `oval cross-section`, `fully rounded`, `NO flat faces`.
- **`circular tube` / runder Rohr-Torus → Donut-Schlauch.** Falsch: Querschnitt ist **oval** (1,05 m hoch, 0,405 m radial) wie ein Fingerring, nicht kreisrund.
- `brushed aluminium` zieht Richtung Sci-Fi — nötigenfalls `no sci-fi, no industrial` verstärken.

**Noch offen, in den Prompts vorläufig gesetzt:** Bürstrichtung umlaufend statt axial ([C-037](../notizen/Offene-Challenges.md)); Runenform bewusst vage ([C-013](../notizen/Offene-Challenges.md)).

**Nutzung:** Midjourney `--ar 3:2` anhängen, NEGATIVE-Block in `--no` umbauen. DALL·E/Imagen: Fließtext unverändert.

**Render-Ordner:** [bilder/](bilder/) — Arbeitsdateien, kein Kanon.

| ID | Datei | Status |
|----|--------|--------|
| **P-001o** | [bilder/P-001o-oval-objektstudie.jpg](bilder/P-001o-oval-objektstudie.jpg) | Objektstudie, ovales Profil |
| **P-001u** | [bilder/P-001u-s-aussenrunen-behalten.jpg](bilder/P-001u-s-aussenrunen-behalten.jpg) | **Form/Szene-Lock** (Referenz; 24 Runen) |

**Arbeitsstand (verbindlich für nächste Renders):**
- **Form:** Eine Ring (PJ) — gigantischer Fingerring, flach liegend
- **Querschnitt:** **Oval**, voll gerundet (axial 1,05 m × radial 0,405 m) — nicht Rechteck, nicht kreisrundes Rohr
- **Prompt-Fallen:** `well-curb`, `rectangular`, `circular tube` → **nicht verwenden**
- **Lock:** **P-001u** (Form, Farbe, Szene, Runenstil). Nicht weiter per image_edit „nur Runen“ iterieren — Tool setzt Innenrunen wieder und zerstört Details.
- **Runen-Ziel (offen):** 12 am Umfang (Uhr-Stunden), sichtbar ~5–6; nur Außenäquator; innen glatt. Umsetzung: externes Masken-Inpaint oder manuell auf u.
- Ältere Zwischenstände (P-001–n, p–t, v/w, P-002*, P-003*) gelöscht.


### Form-Prompt (ersetzen für Geometrie)

```
FORM: Giant plain wedding band like the One Ring in Peter Jackson's Lord of the Rings (Jens Hansen prop). Oval cross-section, fully rounded — taller than thick (height 1.05 m, radial thickness 0.405 m), continuous soft curves. NO circular pipe/tube doughnut, NO flat faces, NO rectangular sides, NO well-curb. Matte brushed aluminium (not gold). Lies flat, hole to sky, outer diameter 3.81 m, hip height.
RUNES: Exactly 12 discrete glyphs, evenly spaced like clock hour marks (every 30°), outer equator only. Nordic/Stargate angular symbols — straight strokes only. Clear sharp V-cut wedge grooves (Keilrillen), not curved or soft channels. Inner curve of the hole blank. UNLIT.
```

**Runen-only-Edit (aus P-001u):** Form/Szene sperren; nur Anzahl/Position der Außenrunen anfassen.


---

## P-001: Ring zwischen Bäumen, bemoost, inaktiv

Stimmungsbild. Der Bach Skir liegt außerhalb des Ausschnitts.

```
Photorealistic. A colossal ring lies flat and forgotten in a stand of trees. Northern European, damp, still, ancient.

THE RING — exact geometry, this is critical:
A single seamless giant wedding band lying FLAT and HORIZONTAL on the forest floor, circular opening facing straight up at the sky. Form exactly like the One Ring in Peter Jackson's Lord of the Rings films (Jens Hansen prop): OVAL cross-section, fully rounded — taller than thick (height 1.05 m axial, radial thickness 0.405 m). Continuous soft curves only — NO circular pipe/doughnut tube, NO flat faces, NO rectangular sides, NO well-curb. Outer diameter 3.81 m. Hip-to-waist height on an adult.

SURFACE — the key contrast of the image:
The bare material looks exactly like BRUSHED ALUMINIUM: matte silver-grey, with a fine directional grain running circumferentially around the ring. No mirror shine, no reflections, no seams, no welds, no casting marks, no tool marks.
It has NOT aged at all: no rust, no corrosion, no patina, no discolouration, no scratches, no pitting — despite being unimaginably old.
Moss and pale lichen grow ON it, carpeting the upper face and the shaded side, gathering in the grooves — but they only sit on the surface. Where the moss has slipped away, the bare material shows through, flawless and factory-fresh, as if made yesterday. The contrast between ancient growth and untouched surface is the emotional core of the image.

MARKINGS: Exactly 12 discrete angular geometric glyphs on the outer equator only, spaced like clock hour marks (every 30°). Sharp V-cut Keilrillen, Nordic/Stargate angular. UNLIT. Inner curve of the hole blank. Not glowing.

SETTING: A dense stand of alder, willow and birch — twisted, wind-shaped, hung with moss. Damp black soil, ferns, deadfall, fallen leaves gathered in the ring's opening. Soft green filtered light through the canopy, mist between the trunks, utterly silent.

CAMERA: Elevated three-quarter view from roughly 3 m up, so the opening reads clearly as an ellipse and the ring's height above ground is unmistakable.

NEGATIVE: no green glow, no light emission, no portal effect, no energy, no upright or standing ring, no gold, no mirror polish, no machinery, no sci-fi, no industrial setting, no stream, no river, no water, no people, no modern objects, no rust, no patina.
```

Arbeitsdateien in [bilder/](bilder/). Formverbindlich ist der Block oben (ovales One-Ring-Profil).

---

## P-002: Fundszene — Erdrutsch am Skir

Kanonische Szene nach [C-008](../notizen/Offene-Challenges.md): Der Erdrutsch am Steilufer legt den Ring frei.

```
Photorealistic. Northern Jutland heathland, Vendsyssel, near the Skagerrak coast. A fresh landslide has torn open a steep stream bank, exposing a colossal ring lying flat in the slump debris.

THE RING — exact geometry, this is critical:
A single seamless giant wedding band lying FLAT and HORIZONTAL on the ground, circular opening facing straight up at the sky. Form like the One Ring (Peter Jackson / Jens Hansen): OVAL cross-section, fully rounded — taller than thick (1.05 m high, 0.405 m radial). NO circular pipe/doughnut tube, NO flat faces, NO rectangular sides, NO well-curb. Outer diameter 3.81 m. Hip-to-waist height.

SURFACE — the key contrast of the image:
The bare material looks exactly like BRUSHED ALUMINIUM: matte silver-grey, fine directional grain running circumferentially. No mirror shine, no seams, no welds, no casting marks.
It has NOT aged: no rust, no corrosion, no patina, no scratches — despite millennia underground.
The landslide has ripped away most of the covering: wet clay, torn moss mats and root threads still cling in patches, sliding off the flanks. Where the earth has fallen away, the bare surface is utterly flawless and gleams dull silver against the black wet soil — shockingly new-looking in the raw, ancient ground.

MARKINGS: Exactly 12 discrete angular glyphs on the outer equator only, clock-hour spacing; clay may pack some. Inner curve blank. UNLIT.

SETTING: Raw torn earth, exposed roots, collapsed heather turf, sparse alder and willow scrub along the bank. Low diffuse northern light, overcast, wind-bent vegetation, damp air.

CAMERA: Elevated three-quarter view from roughly 3 m up, so the opening reads clearly as an ellipse and the ring's height above ground is unmistakable.

NEGATIVE: no green glow, no light emission, no portal effect, no energy, no upright or standing ring, no gold, no mirror polish, no machinery, no sci-fi, no industrial setting, no people, no modern objects, no rust, no patina.
```

---


## P-003: Objektstudie mit Maßstab

Zum Festnageln von Größe und Material — nüchtern, ohne Stimmung.

**Fallen:** Generatoren machen den Querschnitt zu einem dicken Rohr oder zu einem eckigen Bord. Oval erzwingen (1,05 m hoch, 0,405 m radial); Hüfthöhe am Körper; 24 Glyphen am Außenäquator.

```
Photorealistic technical study, neutral presentation. A colossal wedding-band ring lying flat and horizontal on open heathland, circular opening facing straight up at the sky.

GEOMETRY — One Ring oval band, not a trough, curb, or doughnut tube:
Outer diameter 3.81 m. Radial thickness ONLY 0.405 m. Height above ground 1.05 m. OVAL cross-section, fully rounded — taller than thick. NO circular pipe profile, NO flat faces, NO rectangular sides.

SCALE ANCHOR: One adult human in undyed 6th-century woollen clothing stands beside it, hand resting on the upper curve — top of band reaches just above their waist.

SURFACE: BRUSHED ALUMINIUM — matte silver-grey, circumferential grain, no mirror shine, seamless, un-aged, flawless.

MARKINGS: Exactly 12 discrete angular geometric glyphs on the outer equator only, clock-hour spacing. Inner curve blank. UNLIT.

SETTING: Flat open heather, overcast diffuse light, low horizon, no other objects.

CAMERA: Eye-level three-quarter view, 50 mm lens, no distortion.

NEGATIVE: no glow, no portal, no upright ring, no gold, no mirror polish, no machinery, no sci-fi, no rust, no patina, no modern objects, no thick trough walls, no plain parallel grooves only.
```
