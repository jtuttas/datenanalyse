# Neuronale Netze

## Handlungssituation

![Teaser](images/ailight.png)

>Die Firma Home-IoT ist eine bekannter Hersteller von Smart Home Produkten. Es ist geplant für diese Firma eine smarte Lichtsteuerung "AI Light" zu entwickeln, die an die jeweiligen Anforderungen der Kunden angepasst werden kann.
>
>Der Chefentwickler der Abteilung Daten- und Prozessanalyse der ChangeIT GmbH beauftragt Sie damit ein Neuronalen Netz zu entwickeln und dieses für eine exemplarische Anforderung zu trainieren.

## AI-Light

Die smarte Lichtsteuerung "AI-Light" besitzt zwei Sensoren.

- Präsenzerkennung: Über Sensoren ist das System in der Lage zu erkennen, ob sich Personen im Raum befinden.
- Tag / Nachterkennung: Das System ist ebenso in der Lage, Tag- / Nachtzeiten zu erkennen.

![Sensorik AI Light](../html/neuro_hs.drawio.png)

## Kundenanforderungen

Die Kunden stellen dabei unterschiedliche Anforderungen an das System vlg. [^1].

[^1]: Brandt, Y., Eickhoff-Schachtebeck, A. und Strecker, K. (2022) „Schulbuch starkeSeiten Informatik Jahrgang 9/10
Gymnasium Niedersachsen“, Klett-Verlag 2022, ISBN: 978-3-12-007572-1

- In den **Büros** der **Fabrikhalle** sollen die Lampen nachts immer leuchten aus Gründen des Einbrecherschutzes, und tagsüber nur, wenn die Mitarbeiter an ihren Plätzen sind.
- Im **Bürogebäude** der Softwarefirma sollen die Lampen nur nachts leuchten, wenn Mitarbeiter da sind. Tagsüber ist es durch die vielen Fenster immer hell genug.
- Im alten Gebäude der **Stadtverwaltung** müssen die Lampen tagsüber angeschaltet sein, wenn Mitarbeiter da sind, da die Fenster zu wenig Licht hereinlassen. Sollten Mitarbeiter auch nachts arbeiten, müssen auch dann die Lampen eingeschaltet werden. Sonst können sie aus bleiben.
- Im Haus der **Familie Schmidt** sollen die Lampen tagsüber an sein, wenn jemand zuhause ist, und aus sein, wenn keiner da ist. Nachts sollen die Lampen aus sein, wenn die Bewohner im Haus sind und schlafen, und aus Gründen des Einbrecherschutzes an sein, wenn niemand da ist

### Aufgabe Wahrheitstabelle erzeugen

Wählen Sie sich eine Anforderung des Kunden aus und erstellen Sie eine Wahrheitstabelle, die alle möglichen Eingangssignale darstellt und ob sich die Lampe in der jeweiligen Situation an oder ausgehen soll.

### Lösung Wahrheitstabelle erzeugen

Für ein **Büro** und eine **Fabrikhalle** könnte diese Tabelle wie folgt aussehen.

| Tag / Nacht ($X_1$) | Person ($X_2$)    | Lampe ($Y$)   |
| ----------- | --------- | ------- |
| Tag (1)     | nein (0)  | aus (0) |
| Tag (1)     | ja (1)    | an (1)  |
| Nacht (0)   | nein  (0) | an (1)  |
| Nacht (0)   | ja (1)    | an (1)  |

## Das neuronale Netz

Ein neuronales Netzwerk ist ein Modell, das von der Funktionsweise des menschlichen Gehirns inspiriert ist. Es besteht aus einer Sammlung miteinander verbundener künstlicher Neuronen, die Informationen verarbeiten und weiterleiten.

Ähnlich wie biologische Neuronen empfangen auch künstliche Neuronen Eingaben, verarbeiten diese und geben sie als Ausgabe weiter. Die Eingaben werden gewichtet und durch Aktivierungsfunktionen in eine Ausgabe transformiert. 

Ein einfaches Neuron (man spricht hier auch von einem *Perzeptron*) kann dabei wie folgt aussehen.

![Perzeptron](Perzeptron.drawio.png)

Die Werte $X_1$ bis $X_3$ sind z.B. Sensorwerte oder Werte aus einer vorherigen Stufe. $G_1$ bis $G_3$ sind Gewichtungsfaktoren die im laufe des Trainings des Neuronalen Netzes angepasst werden und zur Initialisierung auf zufällige Werte gesetzt werden. Als Aktivierungsfunktionen können Funktionen genutzt werden, wie die Sigmoid-, ReLu- oder Tanh-Funktion bzw. einfache Schwellwerte. Die Funktion gibt an, ob und wie stark das Neuron "feuert".

**Aufgabe**: Berechnen Sie den Ausgabewert $Y$ für das Neuron, wenn als Aktivierungsfunktion ein Tanh-Funktion genutzt wird und folgende Eingangsvektoren und Gewichtsvektoren vorliegen.

$G = \begin{pmatrix} G_1 \\ G_2 \\ G_3 \end{pmatrix}=\begin{pmatrix} 0.4 \\ 0.2 \\ -0.5 \end{pmatrix}$

$X = \begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix}=\begin{pmatrix} 0.7 \\ -0.1 \\ -0.4 \end{pmatrix}$

**Lösung**: 

$Y_*= X_1*G_1+X_2*G_2+X_3*G_3=0.4*0.7+0.2*(-0.1)+(-0.5)*(-0.4)=0.46$

$Y=tanh(0.46)=0.43$

Diese Ausgaben können dann wieder als Eingaben für andere Neuronen dienen, wodurch das Netzwerk Schicht für Schicht komplexere Berechnungen durchführen kann.

Ein neuronales Netzwerk lernt, indem es seine Gewichte anpasst, basierend auf dem Vergleich zwischen seinen Ausgaben und den erwarteten Ausgaben. Dieser Lernprozess wird durch mathematische Algorithmen unterstützt, die als Backpropagation bezeichnet werden. Durch wiederholtes Training auf großen Datensätzen kann ein neuronales Netzwerk Muster erkennen, Zusammenhänge verstehen und Vorhersagen treffen.

Obwohl neuronale Netzwerke nicht genau die gleiche Funktionsweise wie biologische Neuronen haben, sind sie dennoch stark von ihnen inspiriert. Die Idee besteht darin, komplexe Informationsverarbeitung nach dem Vorbild des Gehirns zu ermöglichen und dadurch komplexe Aufgaben in Bereichen wie Bilderkennung, Spracherkennung, Textanalyse und vielem mehr zu lösen.

Für die Steuerung der Lichtanlage benötigen wir pro Sensors ein Neuron, in diesem Fall wäre das demnach zwei Neuronen in der Eingangsschicht (*input Layer*). Die Ausgangsschicht (*output layer*) steuert mir einem Neuron die Lampe. Für einen ersten Ansatz wählen wir 3 Neuronen in der *hidden Layer*. Dementsprechend hat unser Neuronales Netz folgendes Aussehen.

![Neuronale Netz](neuronalesnetz.drawio.png).

### Initialisierung des Netzes

Die Gewichte $W_{11}$ bis $W_{32}$, sowie $W_4$ bis $W_5$ werden initial auf zufällige Werte zwischen +1 / -1 gesetzt.

$W_1 = \begin{pmatrix} w_{11} & w_{21} & w_{31} \\ w_{12} & w_{22} & w_{32} \end{pmatrix}== \begin{pmatrix} -0.19 & -0.96 & 0.43 \\ -0.23 & 0.97 & 0.46 \end{pmatrix}$

$W_2 = \begin{pmatrix} w_4 \\ w_5 \\ w_6 \end{pmatrix}=\begin{pmatrix} -1.0 \\ -0.21 \\ 0.16 \end{pmatrix}$

Als Aktivierungsfunktion $f(x)$ können unterschiedliche Funktionen wie die Sigmoid-, ReLu- oder Tanh-Funktion genutzt werden. Wie verwenden in diesem Beispiel die $tanh$ Funktion im **hidden Layer** und die Sigmoid Funktion in der Ausgabeschicht. Die Sigmoid Funktion ist dabei wie folgt definiert.

$\sigma(x) = \frac{1}{1 + e^{-x}}$

Hier sind beide Funktion nochmals grafisch dargestellt.

![Sigmoid und tanh Funktion](images/neuro1.png)

### Forward Propagation

Um nun den Wert der Zwischenschicht $O$ zu ermitteln müssen wir folgende Rechnungen durchführen.

$O_1=  tanh((X_1*W_{11}+X_2*W_{12})+b_1)$

$O_2=  tanh((X_1*W_{21}+X_2*W_{22})+b_2)$

$O_3=  tanh((X_1*W_{31}+X_2*W_{32})+b_3)$

Im ersten Durchgang nehmen wird den X-Vektor wie folgt an:

$X = \begin{pmatrix} X_1 & X_2 \end{pmatrix}=\begin{pmatrix} 1 & 0 \end{pmatrix}$

Die Bias Werte legen wir zunächst auf 1 fest.

$B_1 = \begin{pmatrix} b_1 \\ b_2 \\ b_3 \end{pmatrix}=\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$

$B_4 = 1$

Mit den angenommen Werten kann nun weiter gerechnet werden:

$O_1=  tanh((X_1*W_{11}+X_2*W_{12})+b_1)= tanh((1*-0.19+0*-0.23)+1)=0.6696$

$O_2=  tanh((X_1*W_{21}+X_2*W_{22})+b_2) = tanh((1*-0.96+0*0.97)+1)=0.0006$

$O_3=  tanh((X_1*W_{31}+X_2*W_{32})+b_3) = tanh((1*-0.43+0*0.46)+1)=0.5154$

Für die *output Layer* ergeben sich folgende Werte.

$O_4'=  (O_1*W_4+O_2*W_5+O_3*W_6)+b_4 = (0.6696*-1.0+0.0006*-0.21+0.5154*0.16)+1=0.4127$

$O_4 = Y'= \frac{1}{1 + e^{-O_4'}}=0.6017$

Als Ergebnis würde das Neuronale Netz also die Lampe einschalten, was leider falsch wäre, denn wir hatten ja angegeben, dass es Nacht ist (1) und keine Person anwesend ist (0). Unser Netzwerk hat also einen Fehler gemacht, dieser kann z.B. wie folgt bestimmt werden:

$E(Y')=Y-Y'=0-0.6017=-0.6017=-60.17%$

Eine andere (besser geeignete) Fehlerfunktion ist der *Binary Cross Entropy Error*. Dieser ist wie folgt bestimmt:

$E(Y')=-(Y*log(Y')+(1-y)*log(1-Y'))$

Für unsere Beispiel würde sich also folgender *Binary Cross Entropy Error* ergeben:

$E(Y')=-(0*log(0.6017)+(1-0)*log(1-0.6017))=0.3998$

Neben dieser Fehlerfunktion gibt es noch weitere, wie z.B. *Categorical Cross Entropy*, *Mean Squared Error* und *Cosine Distance*. Für unsere binäres Klassifizierungsproblem (Lampe an/aus) eignet sich jedoch am besten die zuvor berechnete Binary Cross Entropy Error.

Damit das Modell nun lernen kann (also sich der Fehler minimiert), müssen die Gewichte und die Bias Werte angepasst werden.

## Backward Propagation

## Implementierung in Python

Zum Implementieren dieses Modells nutzen wir die Bibliothek *Tensorflow*. Der folgende Code importiert die notwendige Bibliothek und legt die Daten für die Lichtsteuerung in einem *NumPy* Array an.

```py
import tensorflow as tf
import numpy as np

# Daten definieren
data = np.array([[1, 0, 0],
                 [1, 1, 1],
                 [0, 0, 1],
                 [0, 1, 1]])
```

Anschließend müssen die Daten in Eingangs- und Ausgangsdaten aufgeteilt werden. Für unsere Aufgabenstellung enthalten die ersten beiden Spalten die Eingangsdaten (Tag_Nacht und Person) und die letzte Spalte die Ausgangsdaten.

```py
# Aufteilen der Daten in Features (X) und Labels (y)
X = data[:, :-1]  # Eingangsdaten: Erste beiden Spalten
y = data[:, -1]   # Ausgangsdaten: Letzte Spalte
```

Anschließend muss das neuronale Netz aufgebaut werden:

![Neuronale Netz](neuronalesnetz.drawio.png).

```py
# Definition des neuronalen Netzwerks
model = tf.keras.Sequential([
    tf.keras.layers.Dense(3, activation='relu', input_dim=2),  # Hidden-Layer mit 3 Neuronen
    tf.keras.layers.Dense(1, activation='sigmoid')             # Ausgangsneuron
])
```

Unser Netz hat 3 Neuronen als *hidden layer*. Auf dieser Ebene verwenden wir die **ReLu** Funktion als Aktivierungsfunktion. Von der Eingangsebene erhalten wird 2 Daten **input_dim**. Die drei Neuronen der **hidden layer** speisen ein Neuron auf der Ausgabeebene (**output layer** ), hier verwenden wir die **Sigmoid** Funktion als Aktivierungsfunktion. 

Nachdem das Neuronale Netz gebaut wurde, muss es 'compiliert' werden.

```py
# Kompilieren des Modells
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

Angegeben wird hier der Optimizer **adam**, der dazu dient das absolute Minimum im Fehler zu finden.

Nachdem das Neuronale Netz kompiliert wird, kann es angelernt werden.

```py
model.fit(X, y, epochs=600)
```

Eine *Epoche* ist dabei der Zyklus von Forward- und Backward Propagation mit allen Testdaten.

Nach dem Training kann das Modell überprüft werden. 

```py
# Beispiel-Eingabe für die Vorhersage (Nacht und Person anwesend)
input_data = [[0, 1]] 

# Vorhersage für die Klasse "Lampe" (Binärklassifikation)
prediction = model.predict(input_data)

print(prediction)
```

Das Neuronale Netz liefert z.B. einen Wert von *0.9583882*, welches in unserem Beispiel bedeuten würde, dass die Lampe einzuschalten ist. Dieses wäre auch korrekt für die Annahme, dass es Nacht ist (0) und eine Person im Raum anwesend wäre (1).

Die berechneten Gewichte und Bias Werte im Modell können über folgendes Python Skript ausgegeben werden.

```py
for layer in model.layers:
    weights = layer.get_weights()
    print('Gewichtungen:', weights)
```

Für das Output Layer sieht die Ausgabe z.B. wie folgt aus:

```txt
Gewichtungen: [array([[ 1.6754032 ],
       [-0.9415936 ],
       [ 0.18030357]], dtype=float32), array([0.34544384], dtype=float32)]
```

![Neuronale Netz](neuronalesnetz.drawio.png).

Das letzte Neuron wird gespeist aus den drei Neuronen der hidden Layer. Die Gewichte sind hier $W_4=1.6754$, $W_5=-0.94159$ und $W_6=0.180303$. Das zweite Array listet den Bias Wert $b_4=0.34544$.

**Aufgabe:** Trainieren Sie das Modell wie angegeben und beurteilen Sie die Qualität des Modells. Diskutieren Sie wie die Qualität des Modells gesteigert werden kann.

## Ein eigenes Netzwerk entwerfen und trainieren

**Aufgabe:** Wählen Sie einen anderen Datensatz (s.u.) und entwerfen und trainieren Sie ein neuronales Netz. Dokumentieren Sie ihr Vorgehen und Ihr Ergebnis und präsentieren Sie dieses abschließend der Klasse.

Mögliche Datensätze wären (Sie können aber auch gerne einen eigenen Datensatz auswählen):

1. **Titanic-Datensatz**: Der Titanic-Datensatz enthält Informationen über Passagiere an Bord des Schiffes Titanic, einschließlich Merkmalen wie Alter, Geschlecht, Klasse und Überlebensstatus. Dieser Datensatz ist gut geeignet für binäre Klassifizierungsaufgaben und kann auch zur Vorhersage des Überlebens von Passagieren auf anderen Schiffsreisen verwendet werden.
   - URL: <https://www.kaggle.com/c/titanic/data>

2. **Bank Marketing-Datensatz**: Dieser Datensatz enthält Informationen zu Kunden einer portugiesischen Bank und ob sie Ja oder Nein für ein Termingeld-Abonnement abgeschlossen haben. Es enthält eine Vielzahl von Kundenmerkmalen wie Alter, Beruf, Familienstand usw., die verwendet werden können, um vorherzusagen, ob ein Kunde ein Abonnement abschließen wird oder nicht.
   - URL: <https://archive.ics.uci.edu/ml/datasets/Bank+Marketing>

3. **Breast Cancer Wisconsin (diagnostic) Dataset**: Dieser Datensatz enthält Details zu den Zellkernmerkmalen von malignen und benignen Brustgewebeproben sowie einer Diagnose, ob eine Probe maligne oder benign ist. Der Datensatz ist gut geeignet für binäre Klassifizierungsaufgaben zum Erkennen von Brustkrebs.
   - URL: <https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic)>

## Fragen zum Verständnis

1. Was ist ein Neuron in einem künstlichen neuronalen Netzwerk?
    - [ ] Eine Datenstruktur, die Informationen speichert
    - [ ] Eine Funktion, die das Ergebnis des Netzes berechnet
    - [ ] Eine Einheit, die Eingaben empfängt und eine Ausgabe basierend auf diesen Eingaben generiert
    - [ ] Ein spezielles Modell von neuronalen Netzwerken

2. Welche der folgenden ist KEINE typische Schicht in einem neuronalen Netzwerk?
    - [ ] Eingabeschicht
    - [ ] Ausgabeschicht
    - [ ] Versteckte Schicht
    - [ ] Datenbankschicht

3. Was ist der Zweck einer Aktivierungsfunktion in einem neuronalen Netzwerk?
    - [ ] Um die Genauigkeit des Modells zu erhöhen
    - [ ] Um die Größe des Modells zu reduzieren
    - [ ] Um nicht-lineare Transformationen einzuführen
    - [ ] Um die Geschwindigkeit des Trainings zu erhöhen

4. Welches Problem kann durch zu viel Training eines neuronalen Netzwerks auftreten?
    - [ ] Overfitting
    - [ ] Underfitting
    - [ ] Datenverlust
    - [ ] Netzwerkfehler

5. Welches der folgenden Verfahren wird verwendet, um ein neuronales Netzwerk zu trainieren?
    - [ ] Random Forest Algorithmus
    - [ ] Backpropagation
    - [ ] Linear Regression
    - [ ] Naive Bayes Klassifikation

6. Was ist die Hauptfunktion der "Verlustfunktion" (Loss Function) beim Training eines neuronalen Netzwerks?
    - [ ] Sie definiert die Architektur des Netzwerks
    - [ ] Sie bestimmt die Art der Aktivierungsfunktion in den Neuronen
    - [ ] Sie misst, wie gut das Netzwerk die Ausgabe vorhersagt, und wird für die Optimierung des Netzwerks verwendet
    - [ ] Sie dient dazu, das Netzwerk vor Overfitting zu schützen

