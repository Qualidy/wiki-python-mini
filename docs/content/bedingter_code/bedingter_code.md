# Bedingter Code

Mit dem `if` Keyword und Einrückungen kann man festlegen, dass Code nur unter bestimmten Bedingungen ausgeführt wird.


``` { .python }
name = input("Wie ist dein Name?") # (1)!
if 'q' in name: # (2)!
    print("Wow, das ist ja ein seltener Name!") # (3)!
print(f"Auf jeden Fall ist dein Name {name}") # (4)!
```

1.  Der Nutzer wird nach seinem Namen gefragt. Die Eingabe wird in der Variable `#!python name` gespeichert.
2.  Es wird geprüft, ob der Buchstabe `#!python 'q'` in `#!python name` auftaucht.
3.  Wenn `#!python 'q'` in `#!python name` auftaucht, wird der **eingerückte** Code ausgeführt. Hier können auch noch mehr Zeilen eingerückter Code stehen, die nur ausgeführt werden, wenn die Bedingung erfüllt ist.
4.  Diese Zeile ist nicht eingerückt und wird daher auf jeden Fall wieder ausgeführt.

{{ python_tutor_button("""name = input('Wie ist dein Name?')
if 'q' in name:
    print('Wow, das ist ja ein seltener Name!')
print(f'Auf jeden Fall ist dein Name {name}')
""")}}

Wenn die Bedingung, die neben dem `if` steht, wahr ist, dann werden die nächsten Zeilen Code, die eingerückt sind ausgeführt.
Wenn die Bedingung aber falsch ist, werden die eingerückten Zeilen einfach übersprungen.

{{ task(file="tasks/if_einfügen.yaml") }}

# Was ist eine Bedingung?

Eine **Bedingung** ist ein Ausdruck, der schließlich zu einem booleschen Wert `True` oder `False` ausgewertet wird.
Solche Bedingungen können wir leicht verstehen, indem wir sie laut vorlesen.

``` { .python .pytutor_button }
print("a ist kleiner als 5:")
print(a < 5)

print("a ist größer als 10:")
print(a > 10)

print("a ist größer als 1 und kleiner oder gleich 4:")
print(a > 1 and a <= 4)
```

Hier ist eine Liste mit den wichtigsten Operatoren für uns:

| Operator | Name                |
|----------|---------------------|
| `==`     | Gleich              |
| `!=`     | Ungleich            |
| `>`      | (echt) Größer als   |
| `<`      | (echt) Kleiner als  |
| `>=`     | Größer oder gleich  |
| `<=`     | Kleiner oder gleich |
| `in`     | ist enthalten       |

{{ task(file="tasks/bedingungen_voraussagen_1.yaml") }}

{{ task(file="tasks/bedingungen_voraussagen_2.yaml") }}

{{ task(file="tasks/input_korrigieren.yaml") }}

{{ task(file="tasks/verschachtelte_ifs.yaml")}}


# Bedingungen verknüpfen

Wir können mehrere Bedingungen auch miteinander verknüpfen.

| Operator | Beschreibung                                                   | Beispiel           |
|----------|----------------------------------------------------------------|--------------------|
| `and`    | Gibt `True` zurück, wenn **alle** Parameter `True` sind.       | `x < 5 and y > 10` |
| `or`     | Gibt `True` zurück, wenn **eines** der Parameter `True` ist.   | `x < 5 or y > 10`  |
| `not`    | Invertiert die Eingabe. Aus `True` wird `False` und umbekehrt. | `not x >= 6`       |

{{ task(file="tasks/bedingungen_voraussagen_3.yaml") }}

{{ task(file="tasks/bedingungen_voraussagen_4.yaml") }}

{{ task(file="tasks/bedingungen_programmieren.yaml") }}
