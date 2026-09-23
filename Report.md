1. Da wir es mit Namen zu tun haben, können wir nicht sagen, wie groß der Abstand zwischen zwei Namen ist. Deswegen müssen wir schauen bzw. berechnen, wie gleichmäßig die einzelnen Namen vorkommen.

Ich habe geschaut, wie oft jeder Vorname vorkommt, und dabei die minimale Anzahl an gleichen Namen sowie die maximal vorkommende Anzahl und den Durchschnitt ermittelt. Da die Spannbreite jedoch nicht gleichmäßig, sondern extrem ist, gehe ich davon aus, dass manche Namen öfter vorkommen als andere.

2. Ohne Index dauerte sie konstant ca. 0,048s, mit Index war der erste Abruf mit ca. 0,232s auffällig langsam, da der Index erst von der Festplatte geladen werden musste. Danach pendelte sich die Zeit bei ca. 0,033s ein. Der Speicherbedarf stieg dabei von 10,6MB ohne Index auf 17,8MB mit Index.

3. Bei der Bias-Datenbank war die Abfrage mit Index viel langsamer (~0,6–0,79s) als ohne Index (~0,024s). Das liegt daran, dass die Datenbank bei so vielen Treffern für jede gefundene Zeile einzeln nachschlagen muss, statt einfach die ganze Tabelle am Stück durchzugehen.