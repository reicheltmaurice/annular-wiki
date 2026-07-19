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

---

## Orte — Stimmungsbilder

Fotorealistische Ortsansichten (Vendelzeit / ~550 n. Chr.). **Autorenebene** — Arbeitsdateien in [bilder/](bilder/), kein Kanon. Grundlage: [orte/](../orte/).

| ID | Datei | Ort | Motiv |
|----|--------|-----|--------|
| **O-skirraa-01** | [bilder/O-skirraa-01-weiler.jpg](bilder/O-skirraa-01-weiler.jpg) | [Skirraa](../orte/Skirraa.md) | Weiler-Übersicht (~6 Höfe, Heide, Bach) |
| **O-skirraa-02** | [bilder/O-skirraa-02-hof.jpg](bilder/O-skirraa-02-hof.jpg) | Skirraa | Freier Bauernhof am Skir |
| **O-skirraa-03** | [bilder/O-skirraa-03-heide.jpg](bilder/O-skirraa-03-heide.jpg) | Skirraa | Karge Heide/Moor, Küstenrand |
| **O-tingsal-01** | [bilder/O-tingsal-01-halle.jpg](bilder/O-tingsal-01-halle.jpg) | [Tingsal](../orte/Tingsal.md) | Häuptlingshalle außen |
| **O-tingsal-02** | [bilder/O-tingsal-02-thingplatz.jpg](bilder/O-tingsal-02-thingplatz.jpg) | Tingsal | Freiluft-Thingplatz |
| **O-tingsal-03** | [bilder/O-tingsal-03-siedlung.jpg](bilder/O-tingsal-03-siedlung.jpg) | Tingsal | Siedlungsübersicht Halle + Höfe |
| **O-kaupvik-01** | [bilder/O-kaupvik-01-hafen.jpg](bilder/O-kaupvik-01-hafen.jpg) | [Kaupvik](../orte/Kaupvik.md) | Hafen, Ruderboote ohne Segel |
| **O-kaupvik-02** | [bilder/O-kaupvik-02-markt.jpg](bilder/O-kaupvik-02-markt.jpg) | Kaupvik | Ufermarkt / Handel |
| **O-kaupvik-03** | [bilder/O-kaupvik-03-anfahrt.jpg](bilder/O-kaupvik-03-anfahrt.jpg) | Kaupvik | Anfahrt vom Wasser |
| **O-bellbrim-01** | [bilder/O-bellbrim-01-schlucht.jpg](bilder/O-bellbrim-01-schlucht.jpg) | [Bellbrims Werkstatt](../orte/Bellbrims-Werkstatt.md) | Felsschlucht (Petra-Typ) |
| **O-bellbrim-02** | [bilder/O-bellbrim-02-hoehlenmund.jpg](bilder/O-bellbrim-02-hoehlenmund.jpg) | Bellbrim | Höhleneingang mit Werkzeug |
| **O-bellbrim-03** | [bilder/O-bellbrim-03-werkstatt.jpg](bilder/O-bellbrim-03-werkstatt.jpg) | Bellbrim | Höhlenwerkstatt innen, Wasserlauf |

**Vorgaben:** Photorealistic / documentary. Nordvolk = Holz, Reet/Torfdach, Heide, grau-nasses Licht. Kaupvik = **keine Segel** (nur Ruder). Bellbrim = Wüste/Sandstein, keine Moderne. Kein Fantasy-Stil, keine Burgen, keine Stäbekirchen.

### O-skirraa-01 — Weiler-Übersicht

```
Photorealistic documentary photograph of a tiny 6th-century AD Germanic hamlet in northern Jutland, Vendsyssel. About six low timber longhouses with turf and thatch roofs sit scattered across bleak heather moorland beside a narrow dark stream. Sparse birch and willow, peat-brown soil, wind-bent scrub, no fields of note. Overcast northern sky, damp cold light, empty and remote near the North Sea coast. No people in the foreground. Shot from a slight rise, wide establishing view, 35 mm lens, natural color, no fantasy, no modern objects.
```

### O-skirraa-02 — Hof am Bach

```
Photorealistic close view of a free farmer’s longhouse in a 6th-century North Jutland hamlet beside a quiet stream. Weathered oak posts, wattle-and-daub walls under a thick thatched roof, smoke seeping from a roof opening, wood pile and simple wattle pen for sheep nearby. Damp black soil, reeds at the stream bank, pale heather beyond. Soft overcast daylight, quiet and everyday, documentary realism of the Migration Period / Vendel age. No people, no metal roofs, no glass windows, no fantasy architecture.
```

### O-skirraa-03 — Heide und Moor

```
Photorealistic landscape of barren northern Jutland heath near the Skagerrak coast, 6th century atmosphere. Rolling purple-brown heather, peat bog patches, wind-scoured dunes in the far distance under a low grey sky. A thin silver stream cuts through the moor. Sparse twisted trees, mist and damp air, utterly remote northern Europe. Elevated wide shot, natural muted colors, no buildings, no people, no modern elements, no fantasy.
```

### O-tingsal-01 — Häuptlingshalle

```
Photorealistic exterior of a large 6th-century Vendel-period chieftain’s timber hall in inland northern Jutland. Long high-roofed hall with massive oak posts, steep thatched roof, carved wooden door posts, smoke from a ridge vent. Smaller outbuildings and pens nearby on open heath grassland. Overcast northern light, power and settlement without castles or stone walls. Documentary historical realism, no people in frame, no fantasy spires, no stone keep.
```

### O-tingsal-02 — Thingplatz

```
Photorealistic outdoor assembly place of free farmers in 6th-century northern Jutland: a flat open green with a ring of weathered standing posts and flat stone seats, a simple wooden raised platform for speakers, sparse birch trees at the edge. Distant thatched roofs of a regional center. Cold damp air, grey sky, empty after gathering. Migration-period Thing site atmosphere, documentary realism, no modern objects, no runestones covered in readable modern lettering, no people.
```

### O-tingsal-03 — Siedlungsübersicht

```
Photorealistic elevated view of a small regional center in 6th-century Vendsyssel: a dominant chieftain’s long hall, a cluster of farm longhouses, animal pens, dirt paths, and an open Thing green to one side. Rolling inland heath and low woods beyond. Soft overcast Scandinavian light, muted earth colors, quiet pre-Viking settlement scale. No fortifications, no stone buildings, no modern elements, no fantasy.
```

### O-kaupvik-01 — Hafen

```
Photorealistic view of a 6th-century trading harbor on a narrow fjord inlet like the Schlei in Schleswig. Wooden jetties and slipways, several clinker-built open rowing boats without sails moored or beached, low thatched warehouses and huts along the muddy shore. Grey water, overcast sky, seagulls, damp northern light. Documentary realism of Migration-period Baltic trade, no Viking longships with square sails, no modern ships, no cranes.
```

### O-kaupvik-02 — Markt

```
Photorealistic open-air market on the shore of a 6th-century North European trading bay. Rough wooden stalls and cloth awnings, stacked barrels, amber chunks, wool bales, iron tools, pottery. Thatched huts and a wooden jetty in the background, muddy ground, overcast daylight. Sparse figures in undyed woollen cloaks and tunics of the early medieval North, unobtrusive. Documentary historical realism, no fantasy markets, no bright medieval fair banners, no sails on boats.
```

### O-kaupvik-03 — Anfahrt vom Wasser

```
Photorealistic view from a small open rowing boat approaching a 6th-century harbor settlement on a calm fjord. Low cluster of thatched timber buildings along a muddy inlet shore, wooden piers, smoke from cookfires, reed beds, distant inland fields. Flat grey northern sky reflected in still water. Purely rowed clinker boats only, no sails. Documentary wide shot, historical realism, quiet trade port atmosphere, no modern structures.
```

### O-bellbrim-01 — Schlucht

```
Photorealistic narrow desert canyon of warm red sandstone, inspired by the Siq near Petra, Jordan. Sheer cliff walls, winding dry path of sand and stone, harsh midday sun and deep blue sky, sparse desert scrub. Hidden and remote, no modern paths, no tourists, no carved classical facades. Documentary landscape photography feel.
```

### O-bellbrim-02 — Höhleneingang

```
Photorealistic entrance to a natural cave workshop in a red sandstone desert canyon. Dark cave mouth in a cliff face, improvised wooden scaffolding, rope, clay vessels, and rough work tables near the entrance, dusty tools of bronze and iron age technology. Underground spring water glinting just inside the shadow. Harsh desert light outside, cool shade within. Remote secret research place, no electricity, no modern lab equipment, no people.
```

### O-bellbrim-03 — Werkstatt innen

```
Photorealistic interior of a cave workshop in a desert rock system. Rough sandstone walls lit by oil lamps and a few high openings, workbenches with brass instruments, parchment, stone weights, wooden gears and experimental mechanisms of pre-industrial craft. A narrow underground stream runs through a carved channel across the floor. Dust motes in shafts of light, secret laboratory atmosphere of an isolated desert researcher. No computers, no plastic, no modern devices, no people in frame.
```

---

## Kulturen — Menschenbilder

Ethnografische Arbeitsbilder zur allgemeinen Vorstellung (Kleidung, Haut, Haar, Alltag). **Kein Kanon für Einzelpersonen** — Charaktere haben eigene Dateien. Grundlagen: [kulturen/nordvolk](../kulturen/nordvolk/README.md), [kulturen/sahrin](../kulturen/sahrin/README.md), [Sahrin Aussehen](../menschen/wuestenvolk/Sahrin.md).

| ID | Datei | Kultur | Motiv |
|----|--------|--------|--------|
| **K-nordvolk-01** | [bilder/K-nordvolk-01-gruppe.jpg](bilder/K-nordvolk-01-gruppe.jpg) | Nordvolk | Gruppenbild — Alter, Haar, Kleidung |
| **K-nordvolk-02** | [bilder/K-nordvolk-02-haushalt.jpg](bilder/K-nordvolk-02-haushalt.jpg) | Nordvolk | Haushaltsinneres (Langhaus) |
| **K-nordvolk-03** | [bilder/K-nordvolk-03-alltag.jpg](bilder/K-nordvolk-03-alltag.jpg) | Nordvolk | Hofarbeit / Alltag draußen |
| **K-sahrin-01** | [bilder/K-sahrin-01-gruppe.jpg](bilder/K-sahrin-01-gruppe.jpg) | Sahrin | Gruppenbild — Schleier, Roben |
| **K-sahrin-02** | [bilder/K-sahrin-02-lager.jpg](bilder/K-sahrin-02-lager.jpg) | Sahrin | Zeltlager / Haushalt |
| **K-sahrin-03** | [bilder/K-sahrin-03-karawane.jpg](bilder/K-sahrin-03-karawane.jpg) | Sahrin | Karawane unterwegs |

**Nordvolk (~550, Vendel):** helle bis wettergegerbte Haut; Haar blond / aschblond / hellbraun / rotbraun gemischt (kein Einheitsblond); ungefärbte und schwach pflanzengefärbte Wolle (grau, braun, naturweiß, gedämpftes Waidblau); Tunika, lange Kleider, Rechteckmäntel mit Bronze-Fibeln; **keine** Hörnerhelme, kein Fantasy-Schmuck.

**Sahrin:** sonnengeschwärzte, sehnige Körper; dunkles Haar; weite mehrlagige Gewänder in Sand/Ocker/Schwarz; Tagelmust-ähnliche Schleier; Knochen-/Metallschnallen geometrisch; Ziegenhaarzelt, Kamele. (Kultur noch dünn — optisch an [Sahrin.md](../menschen/wuestenvolk/Sahrin.md) / [allgemein.md](../menschen/wuestenvolk/allgemein.md).)

### K-nordvolk-01 — Gruppenbild

```
Photorealistic ethnographic group portrait of proto-Scandinavian Germanic people of northern Jutland, about 550 AD Vendel period. Six adults and two children standing outdoors on damp heath: fair to lightly weathered skin, freckles, wind-reddened cheeks; hair in natural blondes, ash-brown, dirty-blond, and one reddish-brown; men with full beards and shoulder-length hair, women with long braids or loose hair under simple linen headscarves. Clothing: undyed and lightly plant-dyed wool tunics and long dresses in grey, natural brown, off-white and muted woad-blue; rectangular cloaks pinned with simple bronze brooches; leather belts, soft leather shoes, wool leg wrappings. Everyday faces, not models — worn hands, practical clothing, no horns, no fantasy jewelry, no polished armor. Soft overcast northern light, documentary photography style.
```

### K-nordvolk-02 — Haushalt

```
Photorealistic interior of a 6th-century North Jutland farm longhouse household. Low timber posts, wattle walls, packed earth floor, smoke-darkened thatch overhead. Central hearth fire with iron pot, wooden bowls, clay pots, hanging herbs and dried fish. Family life: woman spinning wool on a drop spindle, man mending a wooden tool, child nearby; undyed wool clothing, fair northern European features, ash-blond and light-brown hair. Dim warm firelight mixed with grey daylight from the open door. Documentary historical realism, Migration Period / Vendel age, no glass windows, no chimneys, no fantasy interiors, no modern objects.
```

### K-nordvolk-03 — Alltag

```
Photorealistic outdoor daily-work scene of a small Vendel-period Germanic farmstead in northern Jutland heath. Two men shearing a sheep and stacking peat, a woman carrying a wooden pail of water from a stream, a girl herding geese. Natural undyed wool tunics and cloaks, leather belts, weather-beaten fair skin, hair in blond and brown tones, practical braids and beards. Bleak heather, thatched longhouse in background, overcast damp light. Ethnographic documentary feel, about 550 AD, no Viking horned helmets, no fantasy weapons display, no modern farm equipment.
```

### K-sahrin-01 — Gruppenbild

```
Photorealistic ethnographic group portrait of the Sahrin, a desert nomad people. Six adults of mixed ages standing in bright desert light before dark goat-hair tents: lean sinewy bodies, sun-darkened copper-brown to deep tanned skin, deep wind lines around eyes; dark brown and black hair; men with short beards or clean-shaven under face cloths. Clothing: wide multi-layered robes and wraps in sand, ochre, dusty white and black wool; tagelmust-style indigo and black face-and-head veils leaving only eyes visible on some figures; leather belts with geometric bone and bronze buckles; simple bone bead necklaces. Serious reserved faces, not glamorous models. Documentary photography, North African / Sahara nomad feel without modern plastics or logos.
```

### K-sahrin-02 — Lager / Haushalt

```
Photorealistic interior and courtyard of a Sahrin nomad household camp at dusk. Black and brown goat-hair tents arranged in a loose circle around a low fire. Inside a tent opening: woven rugs, goatskin water bags, clay jars, date baskets, a woman grinding grain, an older woman sorting wool. Sun-darkened skin, dark hair, multi-layer ochre and black robes, face veils half-lowered indoors. Warm firelight and cool desert evening sky. Ethnographic documentary realism of pre-Islamic Sahara nomads, no modern camping gear, no plastic, no fantasy costumes.
```

### K-sahrin-03 — Karawane

```
Photorealistic daily life of a Sahrin desert caravan on the move. Line of camels loaded with goods walking through pale sand dunes; lean men and women in wide sand-colored and black robes and tagelmust veils walking beside them; one rider; spears for protection; children on a camel. Sun-darkened skin, only eyes visible under veils for some, heat haze and dust. Documentary wide shot, harsh midday desert light, nomadic trade life, no jeeps, no modern clothing, no fantasy armor.
```
