# Bedingter Code

In unseren ersten Beispielen haben wir bereits gesehen, dass man über das `if` Keyword und 
Einrückungen bestimmen kann, dass Code nur unter bestimmten Bedingungen ausgeführt wird.

Eine **Bedingung** ist ein Ausdruck, der schließlich zu einem booleschen Wert `True` oder `False`.

Wenn die Bedingung zu `True` auswertet, dann wird der eingerückte Code ausgeführt.

```python
name = input("Wie ist dein Name?")
if 'q' in name:
    print("Wow, das ist ja ein seltener Name!")

print(f"Auf jeden Fall ist dein Name {name}")
```

## `else` Keyword

Das Schlüsselwort `else` erlaubt codeabschnitte zu definieren, die ausgeführt werden, wenn die Bedingung beim
`if` **nicht** erfüllt sind.

```python
temperatur = 22

if temperatur > 25:
    print("Es ist warm.")
else:
    print("Es ist kühl.")
```

## `elif` Keyword

Bei jedem `if`-Block können auch mit `elif` (kurz für "else if") weitere Bedingungen angegeben werden,
die nur geprüpft werden, wenn die vorherigen Bedingungen falsch waren:

```python
punktzahl = 85  # Angenommene Punktzahl

if punktzahl >= 90:
    print("Ausgezeichnet!")
elif punktzahl >= 70:
    print("Gut gemacht!")
elif punktzahl >= 50:
    print("Bestanden!")
else:
    print("Leider nicht bestanden. Mehr Glück beim nächsten Mal!")

```

### Aufgabe: Einfache Bedingungen schreiben🌶🌶🌶
* Gegeben sei das Alter über `input`. Schreibe Code, die prüft, ob das Alter größer oder gleich 18 ist.

* Wenn ja, drucke "Volljährig". Andernfalls drucke "Minderjährig".

* Schreibe Code, die die Geschwindigkeit bewertet. Über `input` seien zwei Variablen gegeben:`speed` und `max_speed`.
  Wenn die Geschwindigkeit mehr als 20 km/h über dem Limit liegt, drucke "Hohes Bußgeld".
  Wenn die Geschwindigkeit bis zu 20 km/h über dem Limit liegt, drucke "Bußgeld".
  Andernfalls drucke "Geschwindigkeit im Limit".


# Komplexe Bedingungen
Es ist auch möglich if-Bedingungen zu verschachteln:

```python
alter = 25
begleitperson = False
film_genre = "Horror"

if film_genre == "Horror":
    if alter >= 18:
        print("Viel Spaß beim Film!")
    else:  # Alter unter 18
        if begleitperson:
            print("Film erlaubt mit Begleitung.")
        else:
            print("Zugang zum Film nicht gestattet.")
else:
    print("Viel Spaß beim Film!")

```

# Vergleichsoperatoren setzen

In Python, wie in anderen Programmiersprachen, gibt es dir folgenden Vergleichsoperatoren:

| Operator | Name                |
|----------|---------------------|
| `==`     | Gleich              |
| `!=`     | Ungleich            |
| `>`      | (echt) Größer als   |
| `<`      | (echt) Kleiner als  |
| `>=`     | Größer oder gleich  |
| `<=`     | Kleiner oder gleich |


Dazu sind noch die booleschen Vergleichsoperatoren wichtig.

| Operator | Beschreibung                                                   | Beispiel           |
|----------|----------------------------------------------------------------|--------------------|
| `and`    | Gibt `True` zurück, wenn **alle** Parameter `True` sind.       | `x < 5 and y > 10` |
| `or`     | Gibt `True` zurück, wenn **eines** der Parameter `True` ist.   | `x < 5 or y > 10`  |
| `not`    | Invertiert die Eingabe. Aus `True` wird `False` und umbekehrt. | `not x >= 6`       |


### Aufgabe: Bahnkarten🌶🌶
Gegeben seien die Variablen
```python
alter = 65
student = True
wochentag = "Samstag"
```
Schreibe Code, der den Fahrkartenpreis basierend auf Alter, Studentenstatus und Wochentag berechnet.

* Standardpreis: 10 Euro.
* Ermäßigung für Senioren (über 60 Jahre) oder Studenten: 5 Euro.
* Am Wochenende zahlen alle Personen nur den halben Preis.




### Aufgabe: Qualifizierung🌶🌶
Gegeben seien die Variablen
```python
alter = 20
hatErfahrung = True
wohnort = "Berlin"
```
Schreibe Code, der entscheidet, ob eine Person für einen Wettbewerb qualifiziert ist.
Die Qualifikationskriterien sind:

* Alter zwischen 18 und 30 Jahren.
* Muss Erfahrung haben.
* Wohnort muss "Berlin" oder "München" sein.

### Aufgabe: Kinokarten🌶🌶🌶
Gegeben seien die Variablen
```python
alter = 35
mitglied = True
wochentag = "Freitag"
```
Schreibe Code, der den Preis einer Kinokarte bestimmt.
Die Preise sind wie folgt:

* Kinder (unter 12 Jahre): 5 Euro
* Jugendliche (12 bis 18 Jahre): 7 Euro
* Erwachsene (über 18 Jahre): 10 Euro
* Senioren (über 65 Jahre): 6 Euro
* Mitglieder des Kinos erhalten auf jeden Preis 2 Euro Rabatt.
* Am Wochenende (Samstag und Sonntag) kostet jede Karte zusätzlich 3 Euro mehr.

Drucke den Endpreis der Kinokarte.
