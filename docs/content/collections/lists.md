# Sammlungen

Derzeit können wir in einer Variablen genau einen Wert speichern.

Wir werden nun Möglichkeiten kennenlernen, wie wir in einer Variable eine große Menge von Daten speichern können.

## Listen

Die wichtigste Möglichkeit zum Speichern großer Datenmengen in einer Variable sind **Listen**.

Eine Liste kann man sich vorstellen, wie eine Variable mit mehrere Schubladen und diese Schubladen sind
durchnummeriert. Die Nummerierung startet mit `0`, geht dann weiter zu `1`, weiter zu `2` usw.

Wir können eine Liste definieren, indem wir die Elemente, die gespeichert werden sollen in eckige Klammern (`[...]`)
schreiben:

```
trinkgeld = [70, 60, 15, 15, 0, 100, 0]
```

Um nun auf die Elemente zuzugreifen geben wir den schreiben wir nach dem Variablennamen in eckigen Klammern,
welchen Eintrag wir haben möchten.

{{ python_tutor("""trinkgeld = [70, 60, 15, 15, 0, 100, 0]
print(f'Montag: {trinkgeld[0]}')
print(f'Dienstag: {trinkgeld[1]}')
print(f'Mittwoch: {trinkgeld[2]}')
print(f'Donnerstag: {trinkgeld[3]}')
print(f'Freitag: {trinkgeld[4]}')
print(f'Samstag: {trinkgeld[5]}')
print(f'Sonntag: {trinkgeld[6]}')
""") }}

Andererseits können wir über die Notation Werte überschreiben:

{{ python_tutor("""supremes = ['Diana', 'Mary', 'Florence']
supremes[2] = 'Cindy'
print(supremes)
""") }}

{{ task(file="tasks/listen_lesen_0.yaml") }}

{{ task(file="tasks/listen_definieren_0.yaml") }}

{{ task(file="tasks/listen_definieren_1.yaml") }}


Zu einer Liste können neue Elemente mit der Methode `append` hinzugefügt werden. Das sieht dann wie folgt aus:

{{ python_tutor("""fragezeichen = ['Justus']
fragezeichen.append('Peter')
fragezeichen.append('Bob')
print(fragezeichen)
""") }}

{{ task(file="tasks/listen_lesen_1.yaml") }}

{{ task(file="tasks/dauernder_input_listen.yaml") }}

{{ task(file="tasks/listen_input_manipulieren.yaml") }}

Ideen Aufgaben:

Gästeliste

inputs in liste notieren

Zugriff auf elemente, die Verboten sind (index out of bound)

Element an einer besimten stelle ersetzen durch nutzereingaben



# Set

Sets (deutsch: _Mengen_ ) sind listen sehr ähnlich, sie haben aber zwei für uns wichtige unterschiede:

* Jedes Element in der Liste darf nur ein mal auftauchen.
* Jedes Mengen haben keine Ordnung, das heißt, wir können nicht auf das `x`-te Element zugreifen.
* Sets werden mit geschweifen Klammern definiert, statt mit eckigen.

Ein Anwendungsfall für Sets ist das finden einmaliger Elementen in Listen.


# Dictionary

