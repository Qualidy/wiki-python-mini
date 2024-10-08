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

