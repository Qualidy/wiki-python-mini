# Set

Sets (deutsch: _Mengen_ ) sind listen sehr ähnlich, sie haben aber zwei für uns wichtige unterschiede:

* Jedes Element in der Liste darf nur ein mal auftauchen.
* Jedes Mengen haben keine Ordnung, das heißt, wir können nicht auf das `x`-te Element zugreifen.
* Sets werden mit geschweifen Klammern definiert, statt mit eckigen.

Ein Anwendungsfall für Sets ist das finden einmaliger Elementen in Listen.

```python
my_list = [1, 1, 2, 1, 2, 3] # (1)!
my_set = set(my_list) # (2)!
print(my_set) # (3)!
```

1. Liste `my_list` wird erstellt. Manche Elemente sind doppelt und dreifach vorhanden.
2. Aus der Liste wird ein Set (Menge) gemacht.
3. In der Liste sind nun alle Elemente einmalig.

{{ python_tutor("""my_list = [1, 1, 2, 1, 2, 3]
my_set = set(my_list)
print(my_set)""") }}

# Tupel

Tupel sind fast identisch zu listen. Hier sind die für uns entscheidenden Unterschiede:

* Tupel werden mit runden `()` statt mit eckigen Klammern `[]` definiert.
* Tupel lassen sich im Nachhinein nicht mehr ändern.

```python
my_tuple = (1, 2, 3) # (1)!
print(f"Erstes Element: {my_tuple[0]}") # (2)!

my_tuple[0] = 4 # (3)! 
```

1. Ein Tupel wird hier definiert.
2. Der Zugriff auf die Elemente des Tupels sieht genau so aus, wie bei Listen.
3. Hier kommt es bei der Ausführung zu einem Fehler, denn der Inhalt eines Tupels kann im Nachhinein nicht mehr geändert werden. Auch Methoden wie `append` exitieren nicht bei Tupeln.

# Dictionary

Dictionaries sind eine häufig verwendete Datenstruktur, die man als eine Liste mit speziellen Zugriffsmöglichkeiten betrachten kann.
Bei einer Liste greift man auf die Werte immer über Zahlen zu. Bei einem Dictionary werden auf die Werte (Values) über 
vorher definierte Schlüssel (Keys) zugegriffen.

Wir können uns also vorstellen, dass die Schubladen in unseren Schränken nicht durchnummeriert sind, sondern eine Aufschrift haben.