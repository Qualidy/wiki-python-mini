# Variablen

## Was sind Variablen?

In Python können wir **Informationen in Variablen speichern**.

Man kann sich so eine Variable vorstellen, wie einen beschrifteten Schuhkarton in einem Schrank. 
In so einen Schuhkarton kann man zu einem beliebigen Zeitpunkt:

* etwas hineintun; 
* anschauen, was drin ist;
* durch etwas anderes austauschen.

Genauso ist es auch bei Variablen.

Schauen wir uns dazu den folgenden Code an:

```python
a = 1 # (1)!
print(a) # (4)!

a = 2 # (2)!
print(a) # (4)!

a = a + 3 # (3)!
print(a) # (4)!
```

1. In der neuen Variablen `#!python a` ist initial der Wert `#!python 1` gespeichert.
2. In der Variablen `#!python a` ist nun der Wert `#!python 2` gespeichert. Die `#!python 1` wird vergessen.
3. Der Wert von `#!python a` wird zunächst ausgelesen und dann 3 dazuaddiert. Das Ergebnis (`#!python 5`) wird dann wieder in `#!python a` gespeichert.
4. Der Wert der Variablen `#!python a` wird ausgelesen und in mit der `#!python print`-Funktion auf der Konsole ausgegeben.

Wir können uns das obige Beispiel nun noch einmal im Debugger ansehen:

{{ python_tutor("""a = 1
print(a)

a = 2
print(a)

a = a + 3
print(a)""") }}

!!! danger "'"Das Gleichheitszeichen `#!python =` bedeutet nicht <del>"ist gleich"</del> sondern "ist **nun**"!"
    
    Das Gleichheitszeichen `#!python =` in Python ist der sogenannte **Zuordnungsoperator**.
    Er dient dazu, Inhalte in einer Variablen zuzuordnen.
    Auf der linken Seite des `#!python =` steht immer die Variable, in die wir etwas speichern wollen und auf der 
    rechten Seite, _was_ wir in der Variablen speichern wollen.

    Am besten man ließt man Zeilen wie `#!python a = 2` als: **"`#!python a` hat nun den Wert `#!python 2`."**

    Es ist nicht der Gleichheitsoperator, wie wir in aus der Mathematik kennen.

<p style="text-align:center;" markdown>
:fontawesome-solid-box: :fontawesome-solid-box: :fontawesome-solid-box:
</p>

{{ task(file="tasks/variablen_anlegen_1.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_1.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_2.yaml") }}

{{ task(file="tasks/variablenbefüllung_voraussagen_3.yaml") }}

{{ task(file="tasks/variablenbenennung.yaml") }}

{{ task(file="tasks/marsgewicht.yaml") }}

## Nutzereingaben

Mit der `#!python print` Funktion können wir auf der Konsole eine Ausgabe erzeugen.

Andererseits kann mit der Funktion `#!python input` eine Eingabe des Nutzers auf der Konsole erwartet werden.
Wenn die Funktion aufgerufen wird, wartet der Code so lange, bis eine Nutzereingabe getätigt und mit ++enter++ bestätigt wurde.
Die Eingabe des Nutzers wird dann in einer Variablen gespeichert.

{{ python_tutor(title="Nutzereingabe",
code_string="""print('Sei gegrüßt!')
vorname = input('Wie heißt du?')
print('Hallo')
print(vorname)""") }}

{{ task(file="tasks/input_einfügen.yaml") }}

!!! danger "Vorsicht beim Einlesen von Zahlen"
    
    Immer, wenn man Zahlen vom Nutzer einlesen will und mit diesem im Code **rechnen** möchte, so muss
    man Python ganz explizit sagen, dass hier eine Zahl folgt. Verwenden sie daher folgenden Code:

    Bei Ganzzahlen nutze `#!python int(input(...))`:

    ```python
    alter = int(input('Wie alt bist du?'))
    print('In einem Jahr bist du:')
    print(alter + 1)
    ```
    
    Bei Fließkommazahlen nutze `#!python float(input(...))`:

    ```python
    preis = float(input('wie viel kostet das Produkt?))
    print('Die Mehrwehrsteuer des Produktes beträgt:')
    print(preis * 0.18)
    ```


{{ task(file="tasks/marsgewicht_mit_input.yaml") }}

{{ task(file="tasks/bmi.yaml") }}

