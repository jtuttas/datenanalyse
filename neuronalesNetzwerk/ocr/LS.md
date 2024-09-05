# FIDP - Lernfeld 10c

## LS 10.5: Texterkennung (OCR)

| Lernfeld | Bildungsgang | Ausbildungsjahr |
| :--- | :--- | :---: |
| LF 10c: Werkzeuge des maschinellen Lernens einsetzen | Fachinformatiker für Daten- und Prozessanalyse (FIDP) | 3 |

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
| Rahmenlehrplan für Fachinformatiker für Daten- und Prozessanalyse in der Fassung vom 13.12.2019, S. 27 | LS 10.5: Texterkennung OCR | 8 Unterrichtsstunden |

### Handlungssituation

> Ein lokaler Einzelhändler hat die ChangeIT GmbH (ein innovatives Unternehmen welches sich auf IT-Dienstleistungen spezialisiert hat) damit beauftragt ein Berechtigungssystem für den Firmenparkplatz zu entwickeln. Sie als Auszubildender zum Fachinformatiker für Daten- und Prozessanalyse sind maßgeblich an der Implementierung eines ersten **Prototypen** für den Kunden beteiligt.

### Handlungsergebnis

> Prototyp als Jupyter Notebook zur KFZ Kennzeichen Erkennung.

<div style="page-break-after: always;"></div>

### Vorausgesetzte Fähigkeiten und Kenntnisse

| Handlungsschritt | Handlungskompetenz (Fachkompetenz und Personale Kompetenz) | Inhalte | Sozialform/Methoden |
| :--- | :--- | :--- | :--- |
| **Informieren bzw. Analysieren** | **Fachkompetenz:** Verstehen der Anforderung an das Zutrittssystem. <br> **Personale Kompetenz:** Teamarbeit, Diskussionsfähigkeit | Einführung in die Ist- und Soll-Situation, Identifizierung der benötigten Hardware- und Software-Komponenten, Diskussion und Erstellung einer Mindmap | Plenumsdiskussion, Gruppenarbeit, Mindmap-Erstellung |
| **Planen / Entscheiden** | **Fachkompetenz:** Auswahl geeigneter Technologien zur Kennzeichenerkennung. <br> **Personale Kompetenz:** Entscheidungsfindung, Priorisieren | Evaluierung von OCR-Modellen (EasyOCR vs. vortrainiertes Modell), Besuch der Huggingface-Seite zur Auswahl eines geeigneten Modells | Gruppenarbeit, Internetrecherche, Entscheidungsfindung |
| **Durchführen** | **Fachkompetenz:** Umsetzung eines Prototypen in Python. <br> **Personale Kompetenz:** Problemlösungsfähigkeit, Anwendung technischer Fähigkeiten | Implementierung des Prototyps mittels Python und Jupyter Notebook, Ausführung der beiden Ansätze zur Kennzeichenerkennung | Einzelarbeit oder Kleingruppenarbeit, praktische Programmierarbeit |
| **Kontrollieren / Bewerten** | **Fachkompetenz:** Vergleich der Ergebnisse, Erarbeitung von Bewertungskriterien. <br> **Personale Kompetenz:** Kritische Reflexion, analytisches Denken | Überprüfung der Ergebnisse der beiden OCR-Ansätze, Diskussion der Vor- und Nachteile von ChatGPT für die Kennzeichenerkennung | Gruppenarbeit, Diskussion, kritische Reflexion |
| **Reflektieren** | **Fachkompetenz:** Verständnis rechtlicher Rahmenbedingungen (DSGVO), Verfassen einer rechtlich fundierten Antwort. <br> **Personale Kompetenz:** Verantwortungsbewusstsein, Kommunikationsfähigkeit | Analyse der rechtlichen Implikationen der Kennzeichenerfassung, Verfassen einer E-Mail als Antwort an den Kunden | Einzelarbeit, Recherche, Verfassen einer schriftlichen Antwort |

<div style="page-break-after: always;"></div>

### Arbeitsmaterialien / Links

- Download von KI-Modellen: [Hugging Face](https://huggingface.co/)
- [Link zum Jupyter Notebook](https://github.com/jtuttas/datenanalyse/blob/master/neuronalesNetzwerk/ocr/ocr.ipynb)

### Schulische Entscheidungen

- Zur Entwicklung des Prototypen wird die Programmiersprache Python verwendet und das Jupyter Notebook genutzt.

### Leistungsnachweise

- Fachgespräche während der Realisierung des Prototyps

### Mögliche Verknüpfungen zu anderen Lernfeldern / Fächern

- Politik (Fragestellungen bzgl. Datenschutz)
- Ethik (Fragen zu Persönlichkeitsrechten)
