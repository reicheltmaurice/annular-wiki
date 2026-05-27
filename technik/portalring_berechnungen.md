# Größenberechnungen für Portalringe

Skaliert von Referenzring. Formreferenz: Der Eine Ring, Peter Jacksons *Herr der Ringe* (Jens Hansen, 18kt Gold, US Größe 11).

## Referenzring

| Maß | Referenz | One Ring (Filmrequisite) |
|---|---|---|
| Innen-Ø | 20,0 mm | 20,6 mm (US Gr. 11) |
| Außen-Ø | 25,4 mm | ~26,0 mm |
| Wandstärke | 2,7 mm | 2,7 mm |
| Breite (axial) | 7,0 mm | 7,0 mm |
| Volumen | 1,3478 cm³ | ~1,38 cm³ |

Quellen: [Jens Hansen FAQ](https://www.jenshansen.com/pages/which-one-ring-to-choose) · [HeroProp Prototype](https://heroprop.com/product/the-lord-of-the-rings-the-one-ring-wide-production-prototype/)

---

## Skalierte Portalringe (AZ31 als Gewichtsreferenz, ρ = 1,77 g/cm³)

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Innen-Ø</th>
      <th>Außen-Ø</th>
      <th>Wandstärke</th>
      <th>Breite axial</th>
      <th>Volumen (cm³)</th>
      <th>Volumen (m³)</th>
      <th>Gewicht (kg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0,30 m</td>
      <td>0,381 m</td>
      <td>0,0405 m</td>
      <td>0,105 m</td>
      <td>4.549,0</td>
      <td>0,004549</td>
      <td>8,052</td>
    </tr>
    <tr>
      <td>1,00 m</td>
      <td>1,270 m</td>
      <td>0,1350 m</td>
      <td>0,350 m</td>
      <td>168.479,7</td>
      <td>0,168480</td>
      <td>298,209</td>
    </tr>
    <tr>
      <td>2,00 m</td>
      <td>2,540 m</td>
      <td>0,2700 m</td>
      <td>0,700 m</td>
      <td>1.347.837,5</td>
      <td>1,347838</td>
      <td>2.385,672</td>
    </tr>
    <tr>
      <td>3,00 m</td>
      <td>3,810 m</td>
      <td>0,4050 m</td>
      <td>1,050 m</td>
      <td>4.548.951,5</td>
      <td>4,548952</td>
      <td>8.051,644</td>
    </tr>
  </tbody>
</table>

---

## Formel

**Hohlzylinder** (verwendete Formel):

```
V = π × h × (R_außen² − R_innen²)
```

**Skalierung:**
```
F = D_neu / D_ref  (D_ref = 20 mm)
Alle Dimensionen × F, Volumen × F³
```
