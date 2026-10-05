# 3.2 Tupel

Ein Tupel ist eine geordnete Folge wie eine Liste, aber unveränderbar. Nach dem Erzeugen gibt es kein `append`, kein Zuweisen an einen Index und kein `del` eines Elements.

```python
punkt = (1, 2)
einzeln = (1,)      # das Komma macht das Tupel
kein_tupel = (1)    # das ist nur die Zahl 1
leer = ()
auch = 1, 2         # Klammern sind beim Bilden oft optional
```

## Index und Slice

Dieselben Regeln wie bei Listen:

```python
punkt[0]       # 1
punkt[-1]      # 2
punkt[0:1]     # (1,)  ein Slice eines Tupels ist ein Tupel
len(punkt)     # 2
1 in punkt     # True
```

`punkt[0] = 9` wirft `TypeError`.

## Listen und Tupel ineinander

Unveränderbar ist das Tupel selbst, nicht automatisch alles, was darin liegt.

```python
huelle = ([1, 2], 3)
huelle[0].append(9)    # erlaubt, die Liste ist veränderbar
# huelle == ([1, 2, 9], 3)
huelle[1] = 4          # TypeError
```

Eine Liste darf Tupel enthalten, und die Liste darf wachsen:

```python
pfad = [(0, 0)]
pfad.append((1, 0))
```

## Vergleich mit Listen

| | Liste | Tupel |
| --- | --- | --- |
| Schreibweise | `[1, 2]` | `(1, 2)` |
| Ändern | ja | nein |
| Methoden wie `append` | ja | nein |
| Index, Slice, `len`, `in`, `for` | ja | ja |
| Als Dictionary-Schlüssel | nein | ja, wenn alle Elemente selbst hashbar sind |

Ein Tupel mit einer Liste darin ist nicht hashbar, weil die Liste es nicht ist.

Tupel lassen sich zuweisen:

```python
x, y = (1, 2)
a, b = 1, 2
```

Die Anzahl der Namen muss zur Anzahl der Elemente passen, sonst `ValueError`.

## Prüfungsfallen

- `(1)` ist `int`. `(1,)` ist ein Tupel.
- Ein Slice bleibt ein Tupel: `(1, 2, 3)[0:2]` ist `(1, 2)`, nicht `[1, 2]`.
- Die innere Liste eines Tupels bleibt veränderbar.
- `+` und `*` bauen ein **neues** Tupel: `(1,) + (2,)` ist `(1, 2)`. Sie ändern das alte nicht.
