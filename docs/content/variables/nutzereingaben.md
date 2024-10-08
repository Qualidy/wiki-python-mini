# Nutzereingaben

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
