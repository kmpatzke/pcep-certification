# 3.1 Listen: Aufbau, Index, Slice

Eine Liste speichert Werte in einer festen Reihenfolge und darf gemischte Typen enthalten. Sie ist veränderbar.

```python
zahlen = [1, 2, 3]
leer = []
gemischt = [1, "a", True]
```

Der Syllabus sagt „constructing vectors“. Gemeint sind Listen als geordnete Folgen, nicht ein besonderes Vektor-Modul.

## Index

Der erste Index ist `0`. Negative Indizes zählen vom Ende: `-1` ist das letzte Element.

```python
werte = [10, 20, 30]
werte[0]     # 10
werte[-1]    # 30
werte[3]     # IndexError
```

Zuweisen ändert die Liste:

```python
werte[1] = 99    # [10, 99, 30]
```

## Slice

`liste[start:stopp]` enthält `start` und schließt `stopp` aus. Fehlende Grenzen sind Anfang bzw. Ende.

```python
werte = [10, 20, 30, 40]
werte[1:3]     # [20, 30]
werte[:2]      # [10, 20]
werte[2:]      # [30, 40]
werte[:]       # neue Liste mit denselben Elementen
werte[::2]     # [10, 30]
werte[::-1]    # [40, 30, 20, 10]
```

Ein Slice wirft bei zu großen Grenzen keinen `IndexError`. Er liefert, was noch da ist, notfalls `[]`. Ein einzelner Index außerhalb wirft.

Ein drittes Argument ist die Schrittweite. `werte[::2]` nimmt jedes zweite Element.

## `len`, `in`, `for`

```python
len([10, 20, 30])          # 3
20 in [10, 20, 30]         # True
40 not in [10, 20, 30]     # True

text = ""
for zahl in [1, 2]:
    text += str(zahl)
# text == "12"
```

`for i in range(len(werte))` liefert die Indizes. `for zahl in werte` liefert die Elemente. Beides ist gültig.

## Prüfungsfallen

- Der letzte gültige Index ist `len(liste) - 1`, nicht `len(liste)`.
- `liste[1:1]` ist `[]`.
- Ein Slice ist eine neue Liste. `werte[:]` ist nicht dasselbe Objekt wie `werte` (`is` ist falsch), enthält aber dieselben Elemente.
- `in` prüft die Elemente, nicht die Indizes.
