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
      <td>Wie ein niedriger Brunnenrand</td>
      <td>Kein dünner Reifen</td>
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
      <td><strong>Wandstärke</strong></td>
      <td>0,405 m</td>
      <td></td>
    </tr>
    <tr>
      <td><strong>Höhe über Grund</strong></td>
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

**Zwei Fallstricke:** Generatoren stellen den Ring gern *aufrecht* hin (Stargate-Reflex) und ignorieren die Höhe von 1,05 m. `hip-height circular well-curb` wirkt zuverlässiger als die Zahl. `brushed aluminium` zieht Richtung Sci-Fi — nötigenfalls `no sci-fi, no industrial` verstärken.

**Noch offen, in den Prompts vorläufig gesetzt:** Bürstrichtung umlaufend statt axial ([C-037](../notizen/Offene-Challenges.md)); Runenform bewusst vage ([C-013](../notizen/Offene-Challenges.md)).

**Nutzung:** Midjourney `--ar 3:2` anhängen, NEGATIVE-Block in `--no` umbauen. DALL·E/Imagen: Fließtext unverändert.

---

## P-001: Ring zwischen Bäumen, bemoost, inaktiv

Stimmungsbild. Der Bach Skir liegt außerhalb des Ausschnitts.

```
Photorealistic. A colossal ring lies flat and forgotten in a stand of trees. Northern European, damp, still, ancient.

THE RING — exact geometry, this is critical:
A single seamless band ring lying FLAT and HORIZONTAL on the forest floor, its circular opening facing straight up at the sky, like a low circular well-curb. Outer diameter 3.81 m. Inner opening 3.0 m across. Wall thickness 0.405 m. It stands 1.05 m tall above the ground — hip-to-waist height on an adult. Rectangular cross-section with softly rounded edges. Proportionally slender like a plain wedding band, but absolutely enormous.

SURFACE — the key contrast of the image:
The bare material looks exactly like BRUSHED ALUMINIUM: matte silver-grey, with a fine directional grain running circumferentially around the ring. No mirror shine, no reflections, no seams, no welds, no casting marks, no tool marks.
It has NOT aged at all: no rust, no corrosion, no patina, no discolouration, no scratches, no pitting — despite being unimaginably old.
Moss and pale lichen grow ON it, carpeting the upper face and the shaded side, gathering in the grooves — but they only sit on the surface. Where the moss has slipped away, the bare material shows through, flawless and factory-fresh, as if made yesterday. The contrast between ancient growth and untouched surface is the emotional core of the image.

MARKINGS: A band of shallow chiselled angular grooves around the outer face, half-buried under moss. UNLIT — dark, dry, empty channels. Not glowing, no light. Unknown, unclassifiable script: NOT Elder Futhark, NOT Tengwar, NOT Celtic knotwork.

SETTING: A dense stand of alder, willow and birch — twisted, wind-shaped, hung with moss. Damp black soil, ferns, deadfall, fallen leaves gathered in the ring's opening. Soft green filtered light through the canopy, mist between the trunks, utterly silent.

CAMERA: Elevated three-quarter view from roughly 3 m up, so the opening reads clearly as an ellipse and the ring's height above ground is unmistakable.

NEGATIVE: no green glow, no light emission, no portal effect, no energy, no Stargate, no upright or standing ring, no gold, no mirror polish, no chevrons, no machinery, no sci-fi, no industrial setting, no stream, no river, no water, no people, no modern objects, no rust, no patina.
```

---

## P-002: Fundszene — Erdrutsch am Skir

Kanonische Szene nach [C-008](../notizen/Offene-Challenges.md): Der Erdrutsch am Steilufer legt den Ring frei.

```
Photorealistic. Northern Jutland heathland, Vendsyssel, near the Skagerrak coast. A fresh landslide has torn open a steep stream bank, exposing a colossal ring lying flat in the slump debris.

THE RING — exact geometry, this is critical:
A single seamless band ring lying FLAT and HORIZONTAL on the ground, its circular opening facing straight up at the sky, like a low circular well-curb. Outer diameter 3.81 m. Inner opening 3.0 m across. Wall thickness 0.405 m. It stands 1.05 m tall above the ground — hip-to-waist height on an adult. Rectangular cross-section with softly rounded edges. Proportionally slender like a plain wedding band, but absolutely enormous.

SURFACE — the key contrast of the image:
The bare material looks exactly like BRUSHED ALUMINIUM: matte silver-grey, fine directional grain running circumferentially. No mirror shine, no seams, no welds, no casting marks.
It has NOT aged: no rust, no corrosion, no patina, no scratches — despite millennia underground.
The landslide has ripped away most of the covering: wet clay, torn moss mats and root threads still cling in patches, sliding off the flanks. Where the earth has fallen away, the bare surface is utterly flawless and gleams dull silver against the black wet soil — shockingly new-looking in the raw, ancient ground.

MARKINGS: A band of shallow chiselled angular grooves around the outer face, clay still packed into some of them. UNLIT — dark, dry, empty channels. Not glowing, no light. Unknown, unclassifiable script: NOT Elder Futhark, NOT Tengwar, NOT Celtic knotwork.

SETTING: Raw torn earth, exposed roots, collapsed heather turf, sparse alder and willow scrub along the bank. Low diffuse northern light, overcast, wind-bent vegetation, damp air.

CAMERA: Elevated three-quarter view from roughly 3 m up, so the opening reads clearly as an ellipse and the ring's height above ground is unmistakable.

NEGATIVE: no green glow, no light emission, no portal effect, no energy, no Stargate, no upright or standing ring, no gold, no mirror polish, no chevrons, no machinery, no sci-fi, no industrial setting, no people, no modern objects, no rust, no patina.
```

---

## P-003: Objektstudie mit Maßstab

Zum Festnageln von Größe und Material — nüchtern, ohne Stimmung.

```
Photorealistic technical study, neutral presentation. A colossal band ring lying flat and horizontal on open heathland, circular opening facing straight up at the sky.

GEOMETRY: Outer diameter 3.81 m. Inner opening 3.0 m. Wall thickness 0.405 m. Height above ground 1.05 m. Rectangular cross-section, softly rounded edges. Proportionally slender like a plain wedding band, scaled to monstrous size.

SCALE ANCHOR: One adult human in undyed 6th-century woollen clothing stands beside it, hand resting on the rim — the rim reaches just above their waist. The human is the scale reference and must be anatomically correct.

SURFACE: Looks exactly like BRUSHED ALUMINIUM — matte silver-grey, fine directional grain running circumferentially, no mirror shine, no seams, no welds, no casting marks, completely un-aged and flawless. Shallow unlit angular grooves band the outer face.

SETTING: Flat open heather, overcast diffuse light, low horizon, no other objects.

CAMERA: Eye-level three-quarter view, 50 mm lens, no distortion.

NEGATIVE: no glow, no portal, no Stargate, no upright ring, no gold, no mirror polish, no machinery, no sci-fi, no rust, no patina, no modern objects.
```
