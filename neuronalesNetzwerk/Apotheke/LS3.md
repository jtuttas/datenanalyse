# FIDP - Lernfeld 10c

## LS 10.3: Neuronale Netze zur Vorhersage modellieren

| Lernfeld                                                             | Bildungsgang                                          | Ausbildungsjahr |
| :------------------------------------------------------------------- | :---------------------------------------------------- | :-------------: |
| LF 10c:</br>Werkzeuge des maschinellen Lernens einsetzen | Fachinformatiker für Daten- und Prozessanalyse (FIDP) |        3        |

### Kompetenzformulierung

"**Die Schülerinnen und Schüler verfügen über die Kompetenz, maschinelles Lernen zur Problemlösung anzuwenden und den Lernfortschritt des Entscheidungssystems zu begleiten**".

Die Schülerinnen und Schüler **stellen** Einsatzmöglichkeiten des maschinellen Lernens **dar**.
Auf dieser Basis entscheiden sie über die betriebswirtschaftlich sinnvolle Eignung maschinellen Lernens bezüglich kundenspezifischer Problemstellungen.

Sie führen die benötigten Daten zusammen. Dazu analysieren sie freie und kommerzielle Datenquellen und **wählen** diese nach Eignung zur Lösung der Aufgabe durch maschinelles Lernen aus. Die Schülerinnen und Schüler berücksichtigen datenschutzrechtliche, moralische und wirtschaftliche Aspekte.

Sie **legen** für die Aufgabenstellung maschinellen Lernens adäquate Werkzeuge und Systeme **fest**.
Sie bereiten das ausgewählte System technisch vor und **implementieren** die Schnittstellen zum Datenimport.

Die Schülerinnen und Schüler **überwachen** die technische Funktionsfähigkeit im Hinblick auf den Lernfortschritt des Systems.
Sie **reflektieren** die Wirksamkeit des angelernten Entscheidungssystems. Dabei diskutieren sie auch datenschutzrechtliche, moralische und wirtschaftliche Aspekte.

| Curricularer Bezug                                                                                     | Titel der Lernsituation (Kurzfassung)               | Geplanter Zeitrichtwert |
| :----------------------------------------------------------------------------------------------------- | :-------------------------------------------------- | :---------------------: |
| Rahmenlehrplan für Fachinformatiker für Daten- und Prozessanalyse in der Fassung vom 13.12.2019, S. 27 | LS 10.3: Neuronale Netze zur Vorhersage modellieren |   8 Unterrichtsstunden  |

<div style="page-break-after: always;"></div>


### Handlungssituation

Die Auszubildenden entwickeln für die **Eulen Apotheke in Hannover** ein **Vorhersagemodell für den Personalbedarf**.
Auf Basis historischer Verkaufszahlen sollen die Lernenden ein neuronales Netz trainieren, das Stoßzeiten und Flauten vorhersagt, um die Personalplanung zu optimieren. Dabei gilt es, sowohl Kundenservice (Wartezeiten, Belastung der Mitarbeiter) als auch Kosten (Über- und Unterbesetzung) zu berücksichtigen.

---

### Handlungsergebnis

* Ein trainiertes Vorhersagemodell (Keras, neuronales Netz) zur Prognose der Verkaufszahlen / Personalbedarfe.
* Dokumentierte Datenvorbereitung und Explorationsschritte.
* Präsentation der Ergebnisse und Diskussion der Aussagekraft des Modells.
* Reflexion zu Einsatzmöglichkeiten, Grenzen und Integrationsoptionen in die IT-Infrastruktur der Apotheke.

---

### Vorausgesetzte Fähigkeiten und Kenntnisse

|                                  | Handlungskompetenz</br>(Fachkompetenz und Personale Kompetenz)                     | Inhalte                                                                         | Sozialform/Methoden                        |
| :------------------------------- | :--------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------------- |
| **Informieren bzw. Analysieren** | Datenquellen identifizieren, Hypothesen bilden, Einflussfaktoren analysieren       | Einfluss von Tageszeit, Wochentag, saisonalen Schwankungen, Wetter, Feiertagen  | Klassengespräch, Brainstorming             |
| **Planen / Entscheiden**         | Vorgehen strukturieren, Variablen auswählen, Datenaufbereitung planen              | Extraktion von Zeitmerkmalen, Überlegungen zur Skalierung, Auswahl der Features | Gruppenarbeit, Austausch im Plenum         |
| **Durchführen**                  | Daten aufbereiten, Modell implementieren und trainieren                            | Pandas-Datenvorbereitung, Min-Max-Skalierung, Keras-Neural-Netz                 | Partnerarbeit am PC, angeleitetes Arbeiten |
| **Kontrollieren / Bewerten**     | Modellgüte überprüfen, Ergebnisse interpretieren                                   | Training/Validierung, MSE, Vorhersagebeispiele                                  | Vergleich im Klassenverband, Diskussion    |
| **Reflektieren**                 | Modell kritisch hinterfragen, ethische und wirtschaftliche Aspekte berücksichtigen | Grenzen des Modells, mögliche Verbesserungen, Integration in IT-Systeme         | Reflexionsgespräch, Kurzberichte           |

<div style="page-break-after: always;"></div>


### Arbeitsmaterialien / Links

* CSV-Datensatz *apotheke\_sales\_filled.csv*
* Jupyter Notebook mit Code-Vorlagen (Pandas, sklearn, Keras)
* Hintergrundtexte zu neuronalen Netzen (Begriffe: Neuronen, Schichten, Aktivierungsfunktionen, Lossfunktion, Backpropagation)

---

### Schulische Entscheidungen

* Durchführung mit **VS Code** mit Python-Umgebung (Jupyter, TensorFlow/Keras).
* Arbeiten überwiegend in **Partnerarbeit** zur gegenseitigen Unterstützung.
* Präsentation und Diskussion der Ergebnisse im Plenum.

---

### Leistungsnachweise

Reflexionsberichte oder kurze Dokumentationen der Datenvorbereitung können bewertet werden.

---

### Mögliche Verknüpfungen zu anderen Lernfeldern / Fächern

* **Mathematik/Statistik**: Normalisierung, trigonometrische Funktionen (sin/cos für zyklische Features).
* **Betriebswirtschaft**: Personalplanung, Kostenoptimierung, Wirtschaftlichkeit.
* **Informatik / LF 9**: Datenbanken (Datenquellen, Schnittstellen).
* **Projektmanagement**: Planungs- und Reflexionsphasen, Präsentation.

