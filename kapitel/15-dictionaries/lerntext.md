# 3.3 Dictionaries

Ein Dictionary bildet Schlüssel auf Werte ab. Seit Python 3.7 bleibt die Einfügereihenfolge erhalten. Die Prüfungsseiten nennen keine Nebenversion. Verlasse dich in Prüfungsaufgaben nicht darauf, dass eine alte Laufzeit die Schlüssel mischt, und verlasse dich ebenso wenig darauf, dass eine Aufgabe die Reihenfolge als einziges Kriterium ohne `sorted` abfragt, wenn die Reihenfolge nicht aus dem Aufbau klar ist. In diesem Kurs gilt die Reihenfolge von Python 3.7 und neuer.

## Aufbau, Lesen, Ändern

```python
person = {"name": "Ada", "jahr": 1815}
person["name"]           # "Ada"
person["stadt"] = "London"    # neuer Schlüssel
person["jahr"] = 1816          # vorhandener Schlüssel, Wert ersetzt
del person["stadt"]
```

Ein fehlender Schlüssel beim Lesen wirft `KeyError`. `len(person)` zählt Paare.

Schlüssel müssen hashbar sein: Zahlen, Strings, Tupel aus hashbaren Werten. Eine Liste kann kein Schlüssel sein.

## Existenz und Iteration

`in` prüft **Schlüssel**, nicht Werte.

```python
"name" in person         # True
"Ada" in person          # False
"Ada" in person.values() # True
```

```python
for schluessel in person:
    wert = person[schluessel]
```

Die Schleife über das Dictionary liefert die Schlüssel. Methoden:

```python
person.keys()     # Sicht der Schlüssel
person.values()   # Sicht der Werte
person.items()    # Sicht der Paare (schlüssel, wert)
```

```python
for schluessel, wert in person.items():
    pass
```

Die Sichten sind keine Listen. `list(person.keys())` macht eine Liste daraus, wenn du eine brauchst.

Entfernen und dabei den Wert bekommen:

```python
person.pop("jahr")     # liefert den Wert und löscht den Schlüssel
```

`pop` steht nicht wörtlich im Syllabus. `del` schon, über „removing keys“. `pop` ist die übliche Methode dazu und darf dir begegnen. Beide entfernen einen Schlüssel.

## Prüfungsfallen

- `in` trifft Schlüssel, nicht Werte.
- `person["fehlt"]` wirft `KeyError`. Ein Default holst du mit `person.get("fehlt", 0)`. `get` ist praktisch, aber nicht in der Zielzeile genannt. Für die Prüfung reicht: Existenz mit `in` prüfen, dann zugreifen.
- Zwei Namen auf dasselbe Dictionary sehen dieselben Änderungen, genau wie bei Listen.
- `{"a": 1, "a": 2}` hat einen Schlüssel. Der spätere Wert ersetzt den früheren.
