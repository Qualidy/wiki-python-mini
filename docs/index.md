---
hide:
  - navigation
  - toc
---

# Python Einsteiger Schulung

{{ youtube_video("https://www.youtube.com/embed/QemlUufBaFs?si=gHpwm7yB-4l_jJk0") }}

<div class="grid cards" markdown>

- [:fontawesome-solid-boxes-stacked: **Variablen**](content/variables/variablen.md)
- [:material-arrow-decision-outline: **Bedingter Code**](content/bedingter_code/bedingter_code.md)
- [:material-rotate-left: **Codewiederholung**](content/loops/loops.md)
- [:fontawesome-solid-table-list: **Collections**](content/collections/lists.md)

</div>

<!-- Laden der model-viewer Bibliothek -->
<script type="module" src="https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js"></script>
<script nomodule src="https://unpkg.com/@google/model-viewer/dist/model-viewer-legacy.js"></script>

<div class="grid cards" markdown>

<div markdown>
<p style="text-align:center;" markdown>**Listen**</p>

---

<model-viewer 
    src="content/collections/list.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="-15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 600px;">
</model-viewer>
```{ .python }
my_list = [5, 8, 5, 1, 0,80]

print(my_list[0]) # (1)!

my_list[0] = 10 # (2)!
```

1. Zugriff auf Element über den Index `#!python 0`.
2. Überschreiben des Elements an dem Index `#!python 0`.

</div>

<div markdown>
<p style="text-align:center;" markdown>**Dictionaries**</p>

---

<model-viewer 
    src="content/collections/dict.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 600px;">
</model-viewer>
```{ .python }
my_dict = {
    'Hunde': 5,
    'Katzen': 8,
    'Hühner': 5,
    'Hähne': 1,
    'Schweine': 0,
    'Kühe': 80
}

print(my_dict['Hunde']) # (1)!

my_dict['Hunde'] = 6 # (2)!
```

1. Über den Schlüssel `Hunde` wird auf das Value `#!python 5` zugegriffen.
2. Ein neuer Value `#!python 6` wird beim Schlüssel `Hunde` gespeichert. 
</div>
<div markdown>
<p style="text-align:center;" markdown>**Variablen**</p>

---

<model-viewer 
    src="content/collections/var.glb" 
    alt="Ein 3D-Modell"
    camera-orbit="-15deg 80deg 2m" 
    disable-zoom 
    camera-controls
    style="width: 100%; height: 600px;">
</model-viewer>
```{ .python }
my_var = 5

print(my_var) # (1)!

my_var = 6 # (2)!
```

1. Zugriff direkt über den Namen der Variablen.
2. Überschreiben der Variablen. 
</div>
</div>

!!! tip "Schneller Navigieren"

    ++p++ oder ++comma++ : Zur vorherigen Seite gehen (**P**revious)

    ++n++ oder ++period++ : Zur nächsten Seite gehen (**N**ext)
 