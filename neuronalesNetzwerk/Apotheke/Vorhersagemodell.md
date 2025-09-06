# Vorhersagemodell zur Personalplanung in einer Apotheke

Sie sind Auszubildender zum Fachinformatiker für Daten- und Prozessanalyse und bei der Change IT GMbH tätig. Ihr aktuelles Projekt besteht darin, ein Vorhersagemodell zu entwickeln, das den Personalbedarf in der Eulen Apotheke in Hannover prognostiziert. Ziel ist es, die Personalplanung zu optimieren, um sowohl den Kundenservice zu verbessern als auch die Personalkosten zu senken.

## Handlungssituation

Die Eulen Apotheke in Hannover steht vor der Herausforderung, ihre Personalplanung zu optimieren, um den Kundenservice zu verbessern und gleichzeitig die Personalkosten zu senken. Die Apotheke möchte ein Vorhersagemodell entwickeln, das auf Basis historischer Daten den Personalbedarf für verschiedene Tageszeiten und Wochentage prognostiziert.

Die Eulenapotheke hat festgestellt, dass es Zeiten mit Überbesetzung gibt, während zu Stoßzeiten oft nicht genügend Personal vorhanden ist. Dies führt zu längeren Wartezeiten für Kunden und einer erhöhten Belastung für die Mitarbeiter.

![Team](team.jpg)

Die Apotheke beschäftigt derzeit 16 Mitarbeiter, darunter Apotheker, Pharmazeutisch-technische Assistenten (PTA) und Pharmazeutisch-kaufmännische Angestellte (PKA). Die Öffnungszeiten sind von Montag bis Freitag von 8:00 bis 18:00 Uhr und samstags von 9:00 bis 13:00 Uhr.

Die Apotheke verfügt über 8 Arbeitsplätze, die flexibel besetzt werden können. Die Personalplanung erfolgt derzeit manuell durch die  Inhaberin, basierend auf Erfahrungswerten und allgemeinen Annahmen über Kundenfrequenz.

![iris_wien](iris_wien.jpg)


## Zielsetzung

Das Ziel dieses Projekts ist es, ein Vorhersagemodell zu entwickeln, das den Personalbedarf in der Eulen Apotheke basierend auf historischen Daten genau prognostiziert. Das Modell soll in der Lage sein, den Personalbedarf für verschiedene Tageszeiten und Wochentage vorherzusagen, um eine optimale Personalplanung zu ermöglichen.

Das Modell soll folgende Anforderungen erfüllen:
- **Genauigkeit**: Das Modell soll eine hohe Vorhersagegenauigkeit aufweisen, um Über- und Unterbesetzungen zu minimieren.
- **Flexibilität**: Das Modell soll in der Lage sein, sich an saisonale Schwankungen und besondere Ereignisse anzupassen.
- **Benutzerfreundlichkeit**: Das Modell soll einfach zu bedienen sein und klare Empfehlungen für die Personalplanung liefern.

## Planen / Informieren

### Vorüberlegungen

> Sammeln Sie im Klassenverband Ideen und Überlegungen, die Ihnen bei der Entwicklung des Vorhersagemodells helfen könnten. Berücksichtigen Sie dabei Aspekte wie Datenquellen, relevante Variablen, mögliche Herausforderungen.
>
>Wie könnten sich folgende Faktoren auf den Personalbedarf auswirken?

- **Tageszeit**: Morgens, mittags, nachmittags, abends
- **Wochentag**: Montag bis Samstag
- **Saisonale Schwankungen**: Winter (Grippezeit), Sommer (Urlaubszeit)
- **Wetterbedingungen**: Regen, Sonne, Schnee
- **Besondere Ereignisse**: Feiertage, lokale Veranstaltungen, Schulferien

### Datenexploration

Die Apotheke verfügt über historische Daten des letzten Jahres, die folgende Informationen enthalten:

- Datum und Uhrzeit der Kundenbesuche
- Anzahl der Kunden pro 30 Minuten Intervall

```csv
timestamp;count
2024-07-01 00:00:00+02:00;0
2024-07-01 00:30:00+02:00;0
2024-07-01 01:00:00+02:00;0
2024-07-01 01:30:00+02:00;0
2024-07-01 02:00:00+02:00;0
2024-07-01 02:30:00+02:00;0
2024-07-01 03:00:00+02:00;0
2024-07-01 03:30:00+02:00;0
2024-07-01 04:00:00+02:00;0
2024-07-01 04:30:00+02:00;0
2024-07-01 05:00:00+02:00;0
2024-07-01 05:30:00+02:00;0
2024-07-01 06:00:00+02:00;0
2024-07-01 06:30:00+02:00;0
2024-07-01 07:00:00+02:00;0
2024-07-01 07:30:00+02:00;0
2024-07-01 08:00:00+02:00;61
2024-07-01 08:30:00+02:00;63
2024-07-01 09:00:00+02:00;65
2024-07-01 09:30:00+02:00;53
2024-07-01 10:00:00+02:00;85
```

#### Aufgabe 1: Datenvorbereitung

1. Laden Sie die CSV-Datei apotheke_sales.csv in ein Pandas DataFrame.
2. Konvertieren Sie die Spalte `timestamp` in ein Datetime-Format und setzen Sie sie als Index des DataFrames.



3. Extrahieren Sie relevante Zeitmerkmale wie Stunde, Minute und Wochentag aus dem Index und fügen Sie diese als neue Spalten hinzu.

```python
df["hour"] = df.index.hour
df["minute"] = df.index.minute
df["dayofweek"] = df.index.dayofweek
df.head()
```

Ihr Dataframe sollte nun wie folgt aussehen:

![dataframe](vorverarbeitung.png)

4. Überprüfen Sie Ihre zuvor aufgestellten Thesen anhand der geladenen Daten.

#### Aufgabe 2: Skalieren der Daten

Neuronale Netze lernen stabiler, wenn die Daten skaliert sind (z. B. 0–1). Führen Sie die Skalierung der Daten durch, z. B. mit MinMaxScaler aus sklearn.

```python
%pip install scikit-learn

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df["count_scaled"] = scaler.fit_transform(df[["count"]])
df.head()
```

Lassen Sie sich die ersten Zeilen des DataFrames anzeigen, um die neuen skalierten Werte zu sehen.

## Durchführen / Umsetzen

### Aufgabe 3: Entwicklung des Vorhersagemodells

1. Teilen Sie die Daten in Trainings- und Testdatensätze auf (z. B. 80% Training, 20% Test).

```python
from sklearn.model_selection import train_test_split

X = df[["hour", "minute", "dayofweek"]]
y = df["count_scaled"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

2. Entwickeln Sie ein einfaches neuronales Netz mit Keras, das die skalierten Kundenzahlen vorhersagt. Verwenden Sie dabei die extrahierten Zeitmerkmale als Eingabedaten.

```python
%pip install keras
%pip install tensorflow

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
``` 

3. Evaluieren Sie die Leistung des Modells anhand des Testdatensatzes und berechnen Sie Metriken wie den Mean Squared Error (MSE).

```python
mse = model.evaluate(X_test, y_test)
print(f'Mean Squared Error: {mse}')
``` 

4. Visualisieren Sie die Vorhersagen des Modells im Vergleich zu den tatsächlichen Werten.

```python
import matplotlib.pyplot as plt

y_pred = model.predict(X_test)
plt.plot(y_test, label='Tatsächliche Werte')
plt.plot(y_pred, label='Vorhergesagte Werte')
plt.legend()
plt.show()
```


