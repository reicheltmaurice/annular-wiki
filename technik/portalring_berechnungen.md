# Größenberechnungen für Portalringe

Dies ist eine Übersicht über die skalierten Größen der Portalringe basierend auf dem Referenzring (2 cm Innendurchmesser).

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Innendurchmesser</th>
      <th>Außendurchmesser (m)</th>
      <th>Dicke radial (m)</th>
      <th>Breite axial (m)</th>
      <th>Volumen (cm³)</th>
      <th>Volumen (m³)</th>
      <th>Gewicht (g)</th>
      <th>Gewicht (kg)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0,30 m</td>
      <td>0,39</td>
      <td>0,045</td>
      <td>0,075</td>
      <td>365,512</td>
      <td>0,000366</td>
      <td>646,957</td>
      <td>0,647</td>
    </tr>
    <tr>
      <td>1,00 m</td>
      <td>1,30</td>
      <td>0,150</td>
      <td>0,250</td>
      <td>13537,5</td>
      <td>0,013537</td>
      <td>23961,375</td>
      <td>23,961</td>
    </tr>
    <tr>
      <td>2,00 m</td>
      <td>2,60</td>
      <td>0,300</td>
      <td>0,500</td>
      <td>108300,0</td>
      <td>0,108300</td>
      <td>191691,0</td>
      <td>191,691</td>
    </tr>
    <tr>
      <td>3,00 m</td>
      <td>3,90</td>
      <td>0,450</td>
      <td>0,750</td>
      <td>365512,5</td>
      <td>0,365513</td>
      <td>646957,125</td>
      <td>646,957</td>
    </tr>
  </tbody>
</table>


## Rechenwege

### 1. Skalierungsfaktor
\[
F = \frac{D_\text{neu}}{D_\text{ref}}
\]

### 2. Volumen
\[
V_\text{neu} = V_\text{ref} \cdot F^3
\]

### 3. Gewicht
\[
m_\text{neu} = V_\text{neu} \cdot \rho
\]

mit \(\rho = 1,77\,\text{g/cm}^3\).

### 4. Stadion-Fläche

Fläche eines Stadions:
\[
A = r \cdot (\pi \cdot r + 2 \cdot a)
\]

Volumen des Stadion-Torus:
\[
V = 2 \pi R \cdot A
\]

