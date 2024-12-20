# Datentypen

{{ youtube_video("https://www.youtube.com/embed/gEy1XRQ9mC4?si=1OuIdziMzDnSt3Pz") }}

Die Daten, die in einer Variable gespeichert sind, haben einen Typ. In Python ist dies wichtig, um zu wissen,
was man mit den Daten eigentlich tun kann. Zahlen zum Beispiel kann man multiplizieren und addieren.
Zeichenketten kann man miteinander zu längeren Zeichenketten verbinden (1).
{ .annotate }

1.  Der Fachbegriff für das Verknüpfen zweier Zeichenketten zu einem größeren heißt "__konkatenieren__".

Eigentlich gibt es in Python eine ganze Reihe von Datentypen und man kann sogar eigene definieren.
Wir wollen hier jedoch nur vier Datentypen vorstellen, die für diese Schulung von uns von Bedeutung sind:

| Datentyp | Englisch | Deutsch               | Beispiele                                                 |
|----------|----------|-----------------------|-----------------------------------------------------------|
| `int`    | Integer  | Ganzzahlen            | `0`, `1`, `-1`, `12353`, ...                              |
| `float`  | Float    | Fließkommazahlen      | `1.23`, `0.0001`, `1234.5`, `0.0`, ...                    |
| `str`    | String   | Zeichenketten         | `'Hallo'`, `"Menschen"`, `'''mehrzeilige Strings'''`, ... |
| `bool`   | Boolean  | Binäre Wahrheitswerte | `True`, `False`                                           |

Noch ein paar Zusatzinformationen:

=== "Integer"
    
    In Python können Ganzzahlen beliebig groß bzw. klein werden. Das ist sehr angenehm, da man mit ihnen also sicher
    addieren, subtrahieren, multiplizieren und ganz-zahl-dividieren (`%` bzw `//`) kann, ohne dass man sich verrechnet,
    weil man den Raum der Ganzen Zahlen verlässt.

    `int` und `float` kannst du immer daran unterscheiden, dass bei `float` ein `.` in der Darstellung der Zahl ist:

    ```python
    a = 1 # a speichert einen int
    b = 1.0 # b speichert einen float
    ```

=== "Float"
    
    Es gibt unendlich viele Zahlen mit Stellen nach dem Komma. Und schlimmer noch: Zischen zwei verschiedenen Kommazahlen gibt es
    immer eine, die dazwischen liegt! Da wir außerdem noch für jede Kommazahl nur den gleichen endlichen Speicherplatz
    zur Verfügung stellen um sie zu speichern, egal wie groß sie ist (`1` zu speichern verbraucht genau so viel Speicher
    wie `1000000`), ist das Speichern von Kommazahlen ein echtes Problem.

    In Python ermöglicht der Datentyp `float` das Speichern von Kommazahlen, jedoch nicht perfekt:
    
    * Nicht jede Kommazahl ist exakt darstellbar.
    * Es gibt (aus Sicht von Python) eine größte und eine kleinste Fließkommazahl
    * Wenn zwei Kommazahlen addiert/multipliziert/... werden, kann es zu Rechenfehlern kommen. 

    Schau dir [dieses Beispiel zum letzten Punkt](https://pythontutor.com/render.html#code=print%280.1%2B0.1%2B0.1%29%0A%0A%23%20Seid%20wann%20ist%20denn%200.1%20%2B%200.1%20%2B%200.1%20%3E%200.3%20%3F&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
    an.

=== "String"

    Zeichenketten können sowohl mit doppelten, als auch mit einfachen Anführungsstrichen geschrieben werden.

=== "Boolean"

    Der Datentyp Boolean hat genau diese zwei Ausprägungen,
    denn er beschreibt den binären Wahrheitsgehalt einer Aussage. Etwas stimmt, oder es stimmt nicht, da gibt es kein "vielleicht"!
