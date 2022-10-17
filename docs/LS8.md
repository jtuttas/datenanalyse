# FIDP - Lernfeld 10c

## LS 10.8: Cloud KI Systeme nutzen

| Lernfeld | Bildungsgang | Ausbildungsjahr |
| :--- | :--- | :---: |
| LF 10c:</br>Werkzeuge des maschinellen Lernens einsetzen | Fachinformatiker für Daten- und Prozessanalyse (FIDP) | 3 |

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
| Rahmenlehrplan für Fachinformatiker für Daten- und Prozessanalyse in der Fassung vom 13.12.2019, S. 27 | LS 10.8: Cloud KI Systeme nutzen | 12 Unterrichtsstunden |

### Handlungssituation

Sie arbeiten bei der ChangeIT GmbH in der Abteilung Datenanalyse und erhalten folgenden Auftrag:

>Der Besitzer eines Eigenheims möchte gerne wissen welche Autos für wie lange auf seinen Parkplatz parken. Die Kamera vor dem Haus mach dazu alle 5 Minuten ein Bild von dem Parkplatz. Sie erhalten der Auftrag eine Anwendungssystem zu entwickeln welches das KFZ Kennzeichen erfasst und dieses mit einem Zeitstempel in eine Datenbank schreibt.

Da das antrainieren einer eigenen Texterkennungs KI zu aufwendig erscheint, entscheidet sich die Geschäftsführung dazu einen Cloud Dienstleister zu nutzen. Da bereits ein Azure Konto existiert, soll der Azure Bilderkennungsdienst genutzt werden.

### Handlungsergebnis

- Bildanalyse (KFZ Kennzeichen) eines geparkten Autos.

<div style="page-break-after: always;"></div>

### Vorausgesetzte Fähigkeiten und Kenntnisse

| | Handlungskompetenz<br/> (Fachkompetenz und Personale Kompetenz) | Inhalte | Sozialform/Methoden |
| :--- | :--- | :--- | :--- |
| Informieren bzw. Analysieren | Die Schülerinnen und Schüler Analysieren den Auftrag und identifizieren einzelne Arbeitspakete. Für diese Arbeitspakete bestimmen Sie, ob dazu noch weitere Informationen notwendig sind. <br/> $\newline$ Für das Arbeitspaket des maschinellen Sehens mit Azure lesen Sie den zur Verfügung gestellten Artikel. | - Zerlegen des Auftrages in einzelne Arbeitspakete<br/> - Die Azure REST Api  | Einzelarbeit / Klassenplenum <br/><br/> $\newline$ $\newline$ **Hinweise für den DU Unterricht**: Das Gliedern der Arbeitspakete kann in Moodle über die Aktivität *Moodle Board* erfolgen |
| Planen / Entscheiden | Die Schülerinnen und Schülern Planen in Kleingruppen das weitere Vorgehen zum Bewältigen des Arbeitsauftrages. Dazu Priorisieren Sie einzelne Arbeitspakete nach ihrer Zeitlichen Reihenfolge und Wichtigkeit |  | Gruppenarbeit |
| Durchführen | Die Schülerinnen und Schüler implementieren die gewünschte Funktionalität entsprechend des Arbeitsauftrages | | Moodle Aufgabe A1 bis A3 (A4 ist optional) |
| Kontrollieren / Bewerten | Die Schülerinnen und Schüler bewerten das Ergebnis hinsichtlich der Qualität. <br/> Die Schülerinnen und Schüler erstellen für den Kunden ein Angebot aus denen die Kosten für den Täglichen Betrieb des Systems ersichtlich werden. | | Gruppenarbeit<br/>Moodle Aufgabe A5  |
| Reflektieren | Die Schülerinnen und Schüler erhalten eine Email eines Autobesitzers und verfassen eine Antwort, die mögliche Datenschutzprobleme thematisiert | Datenschutzaspekte bei automatischen KI Systemen | Moodle Aufgabe A6 |

### Arbeitsmaterialien / Links

- Moodle-Kurs: [LF10c: Werkzeuge des maschinellen Lernens einsetzen](https://moodle.mm-bbs.de/moodle/course/view.php?id=2812)
- [GitHub Repository](https://github.com/jtuttas/datenanalyse)

### Schulische Entscheidungen

- Für die Nutzung des Azure Dienstes kann der Zugang genutzt werden, der im Rahmen des O365 Angebots vorliegt.
- Die Implementierung der Software sollte in Python unter Verwendung von VS-Code erfolgen. Hier sollte möglichst das in der Python Extension enthaltene Jupyter Notebook verwenden werden.

<div style="page-break-after: always;"></div>

### Leistungsnachweise

- Bewertung des Handlungsergebnisses ggf. im Form eines Fachgespräches mit den einzelnen Arbeitsgruppen.

### Mögliche Verknüpfungen zu anderen Lernfeldern / Fächern
