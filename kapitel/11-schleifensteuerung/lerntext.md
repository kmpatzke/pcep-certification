# 2.2 `break`, `continue`, `else` und Verschachtelung

## `break`

`break` verlässt die **innerste** Schleife sofort.

```python
text = ""
for zeichen in "abcde":
    if zeichen == "d":
        break
    text += zeichen
# text == "abc"
```

## `continue`

`continue` überspringt den Rest des aktuellen Durchlaufs und prüft die nächste Runde.

```python
text = ""
for zeichen in "abca":
    if zeichen == "a":
        continue
    text += zeichen
# text == "bc"
```

Bei `while` muss die Variable, die die Schleife beendet, **vor** `continue` verändert werden. Sonst wiederholst du denselben Zustand.

## `for-else` und `while-else`

Der `else`-Block einer Schleife läuft, wenn die Schleife **nicht** mit `break` verlassen wurde. Er läuft auch, wenn der Körper nie lief.

```python
gefunden = False
for n in range(2, 5):
    if n == 4:
        gefunden = True
        break
else:
    gefunden = False
# break ist passiert, else läuft nicht, gefunden bleibt True
```

```python
for n in range(2, 4):
    if n == 9:
        break
else:
    status = "kein_break"
# status == "kein_break"
```

`else` an einer Schleife ist kein „wenn leer“, sondern „wenn vollständig durchgelaufen“.

## Verschachtelung

`break` und `continue` gelten nur für die Schleife, in der sie stehen. Eine innere `break` lässt die äußere weiterlaufen.

```python
text = ""
for a in range(2):
    for b in range(3):
        if b == 1:
            break
        text += str(a) + str(b)
# text == "0010"
```

Bedingungen und Schleifen dürfen ineinander stehen. Achte auf die Einrückung: sie legt fest, welche Schleife `break` trifft.

## Prüfungsfallen

- `else` nach `for` läuft bei `break` nicht.
- `continue` überspringt nicht die ganze Schleife, nur den Rest dieser Runde.
- `break` in der inneren Schleife beendet die äußere nicht.
- `else` gehört zur Schleife derselben Einrückung, nicht zu einem inneren `if`, wenn die Einrückung so gesetzt ist. Das ist die häufigste Lese-Falle.
