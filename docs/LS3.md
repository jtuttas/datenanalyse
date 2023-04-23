# FIDP - Lernfeld 10c

## LS 10.3: ML auf der Grundlage von Entscheidungsbäumen modellieren

| Lernfeld | Bildungsgang | Ausbildungsjahr |
| :--- | :--- | :---: |
| LF 10c:</br>$\newline$Werkzeuge des maschinellen Lernens einsetzen | Fachinformatiker für Daten- und Prozessanalyse (FIDP) | 3 |

### Kompetenzformulierung

"**Die Schülerinnen und Schüler verfügen über die Kompetenz, maschinelles Lernen zur
Problemlösung anzuwenden und den Lernfortschritt des Entscheidungssystems zu
begleiten**".

Die Schülerinnen und Schüler **stellen** Einsatzmöglichkeiten des maschinellen Lernens **dar**.
Auf dieser Basis entscheiden sie über die betriebswirtschaftlich sinnvolle Eignung maschinellen Lernens bezüglich kundenspezifischer Problemstellungen.

Sie führen die benötigten Daten zusammen. Dazu analysieren sie freie und kommerzielle
Datenquellen und **wählen** diese nach Eignung zur Lösung der Aufgabe durch maschinelles
Lernen aus. Die Schülerinnen und Schüler berücksichtigen datenschutzrechtliche, moralische und wirtschaftliche Aspekte.

Sie **legen** für die Aufgabenstellung maschinellen Lernens adäquate Werkzeuge und Systeme **fest**.

Sie bereiten das ausgewählte System technisch vor und **implementieren** die Schnittstellen
zum Datenimport.

Die Schülerinnen und Schüler **überwachen** die technische Funktionsfähigkeit im Hinblick
auf den Lernfortschritt des Systems.

Sie **reflektieren** die Wirksamkeit des angelernten Entscheidungssystems. Dabei diskutieren
sie auch datenschutzrechtliche, moralische und wirtschaftliche Aspekte.

| Curricularer Bezug | Titel der Lernsituation (Kurzfassung) | Geplanter Zeitrichtwert |
| :--- | :--- | :---: |
| Rahmenlehrplan für Fachinformatiker für Daten- und Prozessanalyse in der Fassung vom 13.12.2019, S. 27 | LS 10.3: ML auf der Grundlage von Entscheidungsbäumen modellieren | 10 Unterrichtsstunden |

### Handlungssituation

Ein großer Landmaschinenhersteller wünscht sich eine größere Kundenbindung und beauftragt die ChangeIT GmbH mit der Entwicklung einer App, die Landwirten Empfehlungen gibt, wann der Weizen zu ernten ist. Die App misst dazu über einen via Bluetooth gekoppelten Feuchte-Sensor die Bodenfeuchte im Feld und kann über eine API Abfrage die Regenwahrscheinlichkeit bestimmen.

Erste Erfahrungswerte liegen bereits vor und werden vom Landmaschinenhersteller der ChangeIT in Form einer CSV Datei zur Verfügung gestellt. 

Als Mitglied der Abteilung Daten- und Prozessanalyse erhalten Sie die Aufgabe ein geeignetes Vorhersagemodell zu entwickeln.

### Handlungsergebnis

Ein Modell auf der Grundlage eines Entscheidungsbaumes, um für eine App Bauern die Empfehlung zu geben, ob Weizen zu ernten ist oder doch besser noch gewartet werden soll!

<div style="page-break-after: always;"></div>

### Vorausgesetzte Fähigkeiten und Kenntnisse

| | Handlungskompetenz</br>(Fachkompetenz und Personale Kompetenz) | Inhalte | Sozialform/Methoden |
| :--- | :--- | :--- | :--- |
| Informieren bzw. Analysieren | Daten Visualisieren </br> Muster in Datenstrukturen erkennen </br> Entropie einer Datenmenge bestimmen </br> | Die Schülerinnen und Schüler stellen den Datensatz grafisch dar </br> Sie versuchen Muster für Entwicklung eines Modells zu erkennen </br> | Plenum </br> Einzelarbeit |
| Planen / Entscheiden | Auf der Grundlage der Entropie Teildatenmengen einteilen | Die Schülerinnen und Schülern entwickeln eine Funktion zur Bestimmung der Entropie und wenden die an einer Teildatenmenge an</br>  | Einzelarbeit </br> Plenum |
| Durchführen | Einen Entscheidungsbaum entwickeln | Unter Verwendung der Python Bibliothek *sklearn* implementieren die Schülerinnen und Schüler ein Vorhersagemodell | Einzelarbeit |
| Kontrollieren / Bewerten | Bewerten eines Vorhersagemodells | Die Schülerinnen und Schüler bewerten das erzeugte Vorhersagemodell  | Einzelarbeit </br> Plenum |
| Reflektieren | Selbständige Problemlösung | Die Schülerinnen und Schüler wählen einen weiteren geeigneten Datensatz aus und entwickeln für diesen ein Vorhersagemodell und stellen das entwickelte Modell vor  | Gruppenarbeit </br> Plenum   |

### Arbeitsmaterialien / Links

- Moodle-Kurs: [LF10c: Werkzeuge des maschinellen Lernens einsetzen](https://moodle.mm-bbs.de/moodle/course/view.php?id=2812)
- [GitHub Repository](https://github.com/jtuttas/datenanalyse)

### Schulische Entscheidungen

- Die Programmiersprache Python wird verwendet
- Als Entwicklungsumgebung wird VS Code / Jupyter Notebook benutzt

### Leistungsnachweise

Die Präsentation der einzelnen Vorhersagemodelle kann zur Leistungsbewertung herangezogen werden!

### Mögliche Verknüpfungen zu anderen Lernfeldern / Fächern
