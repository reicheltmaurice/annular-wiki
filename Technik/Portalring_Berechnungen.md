# Größenberechnungen für Portalringe

**Der 3-m-Ring ist der Referenzring.** Alle anderen Größen werden aus ihm abgeleitet, nicht umgekehrt. Die frühere Herleitung aus dem Einen Ring (Peter Jackson / Jens Hansen) ist **abgelöst** — siehe [C-007](../Notizen/Offene-Challenges.md#c-007-proportionen-der-portalringe-), [C-117](../Notizen/Offene-Challenges.md#c-117-ringgeometrie-neu-vermessen-).

---

## Referenzring (3,00 m)

Form: **flacher Armreif** — abgerundetes Rechteck im Querschnitt, alle vier Ecken mit gleichem Radius gebrochen.

<table>
  <caption>Referenzring — verbindliche Maße</caption>
  <tbody>
    <tr><td>Innen-Ø (ID)</td><td><strong>3,00 m</strong></td><td>Leitmaß, alles andere folgt daraus</td></tr>
    <tr><td>Außen-Ø (AD)</td><td>3,30 m</td><td>ID + 2 × Dicke</td></tr>
    <tr><td>Dicke (radial)</td><td>0,15 m</td><td>Ringkörper von innen nach außen</td></tr>
    <tr><td>Breite (axial)</td><td>0,50 m</td><td>Verhältnis Breite : Dicke = 3,3 : 1</td></tr>
    <tr><td>Rundungsradius</td><td>0,03 m</td><td>20 % der Dicke; lässt 0,09 m gerade Kante</td></tr>
    <tr><td>Querschnittsfläche</td><td>0,074227 m²</td><td></td></tr>
    <tr><td>Volumen</td><td>0,734556 m³</td><td>734.556 cm³</td></tr>
    <tr><td>Gewicht (bei 7,8 g/cm³)</td><td>5.729,5 kg</td><td>Referenzdichte, kein Materialbeschluss</td></tr>
  </tbody>
</table>

---

## Ableitungsverhältnisse

Jedes Maß hängt am Innendurchmesser:

| Maß | Verhältnis zum Innen-Ø |
|---|---|
| Breite (axial) | 1 : 6 |
| Dicke (radial) | 1 : 20 |
| Rundungsradius | 1 : 100 |
| Außen-Ø | 1,10 : 1 |

Alle Längen skalieren mit dem Faktor **F = ID / 3,00 m**, das Volumen mit **F³**.

---

## Skalierte Portalringe (Referenzdichte ρ = 7,8 g/cm³)

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Innen-Ø</th>
      <th>Außen-Ø</th>
      <th>Dicke</th>
      <th>Breite axial</th>
      <th>Radius</th>
      <th>Volumen (cm³)</th>
      <th>Volumen (m³)</th>
      <th>Gewicht (kg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0,30 m</td><td>0,330 m</td><td>0,015 m</td><td>0,0500 m</td><td>0,003 m</td>
      <td>734,6</td><td>0,000735</td><td>5,730</td>
    </tr>
    <tr>
      <td>1,00 m</td><td>1,100 m</td><td>0,050 m</td><td>0,1667 m</td><td>0,010 m</td>
      <td>27.205,8</td><td>0,027206</td><td>212,205</td>
    </tr>
    <tr>
      <td>2,00 m</td><td>2,200 m</td><td>0,100 m</td><td>0,3333 m</td><td>0,020 m</td>
      <td>217.646,2</td><td>0,217646</td><td>1.697,640</td>
    </tr>
    <tr>
      <td>3,00 m</td><td>3,300 m</td><td>0,150 m</td><td>0,5000 m</td><td>0,030 m</td>
      <td>734.555,9</td><td>0,734556</td><td>5.729,536</td>
    </tr>
  </tbody>
</table>

Kanonisch sind nur **3,00 m** und **0,30 m** ([C-010](../Notizen/Offene-Challenges.md#c-010-ringsystem--kopplungsmechanik-)); 1,00 m und 2,00 m stehen als Rechenbeispiele, nicht als bestätigte Größen ([C-017](../Notizen/Offene-Challenges.md#c-017-weitere-ringgrößen)).

---

## Formel

**Querschnitt** — abgerundetes Rechteck (Breite h, Dicke t, Eckradius r):

```
A = h · t − (4 − π) · r²
```

Der Term `(4 − π) · r²` ist das Material, das die vier gebrochenen Ecken wegnehmen.

**Volumen** — Rotationskörper nach Pappus:

```
V = 2 · π · R_s · A          mit R_s = ID/2 + t/2
```

`R_s` ist der Schwerpunktradius des Querschnitts. Er liegt exakt in der Mitte der Dicke, weil das abgerundete Rechteck symmetrisch zur radialen Mittellinie ist.

**Kontrollrechnung 3-m-Ring:**
```
A = 0,50 · 0,15 − (4 − π) · 0,03²  = 0,075 − 0,000773 = 0,074227 m²
V = 2π · 1,575 · 0,074227           = 0,734556 m³
m = 0,734556 · 7.800 kg/m³          = 5.729,5 kg
```

**Größter Radius beim Flip** (Eckbogen, nicht Außen-Ø/2):
```
R_flip = √((AD/2 − r)² + (h/2 − r)²) + r  = 1,6649 m
```

---

## Nicht mehr gültig

Frühere Fassungen dieser Datei rechneten den Ring als **Hohlzylinder**, skaliert aus den Proportionen des Einen Rings (Innen-Ø 20,0 mm, Wand 2,7 mm, Breite 7,0 mm) — Ergebnis: 4,549 m³ und ~8.052 kg. Diese Zahlen sind **überholt**. Zwei Fehler steckten darin:

1. **Falsche Skalierungsbasis.** Skaliert wurde ab 20,0 mm Innen-Ø, der Eine Ring hat als US-Größe 11 aber 20,6 mm.
2. **Falsche Querschnittsform.** Der Hohlzylinder ist schon am Referenzobjekt widerlegt: Jens Hansen gibt für den Filmring ~17 g in 18ct Gelbgold an, der Hohlzylinder ergäbe 21–22 g.

Beides dokumentiert in [C-117](../Notizen/Offene-Challenges.md#c-117-ringgeometrie-neu-vermessen-). Die Eine-Ring-Referenz ist damit vollständig abgelöst; Formvorbild ist jetzt der flache Armreif ([C-073](../Notizen/Offene-Challenges.md#c-073-querschnitt-der-ringe--flacher-armreif-)).
