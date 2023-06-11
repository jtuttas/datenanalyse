# FIDP - Lernfeld 10c

## LS 10.9: Verstärkendes Lernen

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
| Rahmenlehrplan für Fachinformatiker für Daten- und Prozessanalyse in der Fassung vom 13.12.2019, S. 27 | LS 10.9: Verstärkendes Lernen | 11 Unterrichtsstunden |

### Handlungssituation

> Ein großer deutscher internationaler Automobilkonzern, plant die Einführung einer autonomen Taxiflotte. Dabei sollen Fahrgäste ein fest definierten Stationen die Möglichkeit haben eine Fahrt zu buchen und eine weitere Station als Zielort anzugeben.
>
> Der Chefentwickler der Abteilung Daten- und Prozessanalyse der ChangeIT GmbH schlägt vor dieses Problem mit Hilfe des verstärkenden Lernens zu lösen. Die Kollegen der Anwendungsentwicklung haben dazu bereits eine Simulationsumgebung geschaffen. Ihre Aufgabe wird es sein, einen Lernalgorithmus zu entwickeln, der in dieser Simulationsumgebung Fahrgäste aufnimmt und optimal zu ihrem Ziel befördert.

### Handlungsergebnis

- Machine Learning Modell zum automatischen Befördern von Passagieren

<div style="page-break-after: always;"></div>

### Vorausgesetzte Fähigkeiten und Kenntnisse

| | Handlungskompetenz<br/>$\newline$(Fachkompetenz und Personale Kompetenz) | Inhalte | Sozialform/Methoden |
| :--- | :--- | :--- | :--- |
| Informieren bzw. Analysieren | - Grundlagen des Reinforced Learning </br> - Analysieren der Simulationsumgebung  | Die Schülerinnen und Schüler informieren sich über Grundbegriffe des Reinforced Learning, wie *Agent*, *Environment*, *Action*, *Reward* </br> - Sie untersuchen die Simulationsumgebung und führe erste *Aktionen* durch und beobachten die Reaktion der Simulationsumgebung   | - Einzelarbeit </br> - Plenum </br> - Als Umgebung wird das *Taxi* Environment der RIL Umgebung aus dem OpenAI Paket verwendet  |
| Planen / Entscheiden | - Brute Force Ansatz | Die Schülerinnen und Schüler versuchen zunächst die Aufgabe mittels eine Brute Force Ansatzes zu lösen  | - Einzelarbeit </br> - Plenum </br> |
| Durchführen | - Q-Learning Algorithmus | Die Schülerinnen und Schüler implementieren den Q-Learning Algorithmus und trainieren dieses anhand des gegebenen Modells | - Einzelarbeit </br> - Plenum </br> |
| Kontrollieren / Bewerten |- Qualitätsaspekte für das RiL Modell  | Die Schülerinnen und Schüler beurteilen die Qualität des entwickelten Modells, Sie verändern wichtige Parameter um ggf. die Qualität zu verbessern | - Einzelarbeit </br> |
| Reflektieren | - Die Schülerinnen und Schüler erarbeiten ein ML-Modell für das Reinforced Learning anhand einer weiteren Umgebung </br> - Die Schülerinnen und Schüler beantworten Fragen zur Lerneinheit | Erarbeiten eines ML Modells an einer anderen Umgebung auf dem GYM Framework | - Gruppenarbeit </br> - als weitere Umgebungen bieten sich folgende Umgebungen an (*FrozenLake*, *Cliff Walking*, *MountainCar* und *CartPole*) |

### Arbeitsmaterialien / Links

- Moodle-Kurs: [LF10c: Werkzeuge des maschinellen Lernens einsetzen](https://moodle.mm-bbs.de/moodle/course/view.php?id=2812)
- [GitHub Repository](https://github.com/jtuttas/datenanalyse)

### Schulische Entscheidungen

- Die Implementierung der Software sollte in Python unter Verwendung von VS-Code erfolgen. Hier sollte möglichst das in der Python Extension enthaltene Jupyter Notebook verwenden werden.
- Als Simulationsumgebung wir das GYM Framework von OpenAI verwendet

<div style="page-break-after: always;"></div>

### Leistungsnachweise

- Bewertung des Handlungsergebnisses aus der Reflexionsphase ggf. im Form eines Fachgespräches mit den einzelnen Arbeitsgruppen.

### Mögliche Verknüpfungen zu anderen Lernfeldern / Fächern

