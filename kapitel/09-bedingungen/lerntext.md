# 2.1 Entscheidungen mit `if`

`if` führt einen Block nur aus, wenn die Bedingung wahr ist.

```python
note = 2
if note == 1:
    text = "sehr gut"
elif note == 2:
    text = "gut"
elif note == 3:
    text = "befriedigend"
else:
    text = "andere"
```

Formen, die der Syllabus nennt:

- `if`
- `if` / `else`
- `if` / `elif`
- `if` / `elif` / `else`
- mehrere Bedingungen hintereinander
- verschachtelte Bedingungen

`elif` wird nur geprüft, wenn alle vorherigen Bedingungen falsch waren. `else` gehört zum letzten offenen `if` und hat keine eigene Bedingung.

## Mehrere Bedingungen

```python
alter = 20
if alter >= 18 and alter < 65:
    status = "erwachsen"
```

Zwei getrennte `if` sind etwas anderes als `elif`: beide können laufen.

```python
x = 5
spur = ""
if x > 0:
    spur += "a"
if x > 3:
    spur += "b"
# spur == "ab"

spur = ""
if x > 0:
    spur += "a"
elif x > 3:
    spur += "b"
# spur == "a", der zweite Zweig ist unerreichbar, weil der erste schon wahr war
```

## Verschachtelung

```python
if alter >= 18:
    if karte:
        eintritt = "ja"
    else:
        eintritt = "ausweis_fehlt"
else:
    eintritt = "nein"
```

Das `else` bindet an das `if` derselben Einrückung. Ein falsch eingerücktes `else` gehört zu einem anderen `if` oder ist ein Syntaxfehler.

Die Bedingung muss kein Vergleich sein. Jeder Wert hat einen Wahrheitswert (Kapitel 06). `if name:` ist falsch für den leeren String.

## Prüfungsfallen

- `=` in der Bedingung ist Zuweisung und hier ein Syntaxfehler. Es muss `==` sein.
- Reihenfolge der `elif`: der erste wahre Zweig gewinnt, die restlichen werden nicht geprüft.
- `else` ohne Doppelpunkt ist ein Syntaxfehler.
- Ein `if` ohne Block ist ein Syntaxfehler. Mindestens eine Anweisung oder `pass`.
- `elif` darf nicht vor `if` stehen und nicht nach `else`.
