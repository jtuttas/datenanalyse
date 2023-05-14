# KNN - K Nearest Neighbor

## Handlungssituation

![Teaser](https://upload.wikimedia.org/wikipedia/commons/a/af/Diamantrahmen_Rohrlaengen.png)

>Ein Online Fahrradhändler möchte seinen Kunden stets Fahrräder in der optimale Rahmenhöhe anbieten. Dazu soll eine App inkl. Vorhersagemodell entwickelt werden, so dass der Kunde lediglich ein Foto aufnehmen muss und ihm die optimale Rahmenhöhe empfohlen wird.
>
>Eine Abteilung der ChangeIT GmbH ist bereits damit beauftragt aus einem Bild die Schrittlänge und die Körpergröße (jeweils in cm) zu ermitteln. Sie sollen ein Vorhersagemodell entwickeln, welches dem Kunden die richtige Rahmengröße vorschlägt.
>
>Der Online Fahrradhändler hat bereits Daten in Form von Erfahrungswerten vorliegen und stellt ihnen diese in Form einer CSV Datei zur Verfügung.

## Exploration der Daten

Stelle Sie zunächst die Daten, die Sie vom Online Händler erhalten haben grafisch dar ([CSV Datei](../Data/Rahmenhoehe.csv)). Zur besseren Unterscheidung der Kategorien (Klassen) sollte jede Rahmenhöhe (S,M,L,XL) in einer anderen Farbe dargestellt werden.

![Exploration der Daten](images/knn1.png)

## Erste Überlegungen zum Vorhersagemodell

Angenommen ein Kunde wird ausgemessen und es ergibt sich eine Körpergröße von *163cm* und eine Schrittlänge von *84cm*, welchen Rahmengröße könnte man dem Kunden empfehlen?

![Entwurf eines Vorhersagemodells](images/knn2.png)

Nun man könnte zunächst auf die Idee kommen sich den Datenpunkt zu suchen, der vom gesuchten den geringsten Abstand hat. Also benötigen wir eine Funktion, die und die Entfernung der Datenpunkte bestimmt. 

$$c = \sqrt{a^2 + b^2}$$

bzw.

$$c = \sqrt{(ax-px)^2 + (ay-py)^2}$$

Im n-dimensionalen Raum wird diese Abstand auch als Euklidische Distanz bezeichnet. Für einen n-dimensionalen Raum sieht die Berechnung des Euklidische Distanz wir folgt aus:

$$ \sqrt{\sum_{i=1}^{n}(q_i-p_i)^2} $$

Hierbei beschreibt $n$ die Anzahl der Dimensionen der Punkte $p$ und $q$ und $p_i$ und $q_i$ stellen die Werte der i-ten Dimension der jeweiligen Punkte dar.

Entwickeln sie eine Funktion **distance(ax,ay,px,py)**, die die Entfernung zweier Punkte bestimmt.

Iterieren Sie durch alle gegeben Datenpunkte und bestimmen Sie den Punkt, der vom gesuchten Punkt (Körpergröße=163cm / Schrittlänge=84 cm) den geringsten Abstand hat.

> Diskutieren Sie im Klassenverband, ob wir bereits ein geeignetes Vorhersagemodell gefunden haben? Und wie wir die Qualität unseres gefundenen Modells überprüfen können?