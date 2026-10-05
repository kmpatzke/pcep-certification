# 2.2 Schleifen mit `while`, `for`, `range` und `pass`

## `pass`

`pass` ist eine Anweisung, die nichts tut. Sie füllt einen Block, den die Syntax verlangt, den du aber leer lassen willst.

```python
if False:
    pass
```

## `while`

```python
n = 3
summe = 0
while n > 0:
    summe += n
    n -= 1
# summe == 6, n == 0
```

Die Bedingung wird vor jedem Durchlauf geprüft. Ist sie von Anfang an falsch, läuft der Block nie. Vergisst du, die Bedingung irgendwann falsch zu machen, endet die Schleife nicht.

## `for` und `in`

`for` geht eine Sequenz durch. `in` liefert dabei das nächste Element.

```python
text = ""
for zeichen in "ab":
    text += zeichen
# text == "ab"
```

`in` ist auch ein Operator außerhalb der Schleife: `"a" in "ab"` ist `True`. In `for` hat es die Rolle „nimm nacheinander die Elemente“.

## `range`

`range` erzeugt eine Folge ganzer Zahlen. Das Stopp-Argument gehört **nicht** dazu.

```python
list(range(3))         # [0, 1, 2]
list(range(1, 4))      # [1, 2, 3]
list(range(1, 6, 2))   # [1, 3, 5]
list(range(5, 1, -1))  # [5, 4, 3, 2]
list(range(3, 1))      # [] , Schritt ist +1, Start liegt schon hinter Stopp
```

```python
s = 0
for i in range(1, 4):
    s += i
# s == 6
```

`range` speichert nicht alle Zahlen als Liste. In einer `for`-Schleife ist das egal. `range(n)` sind `n` Durchläufe, die Indizes `0` bis `n - 1`.

## Schleife über eine Sequenz

Listen, Tupel und Strings sind Sequenzen. `for element in folge` besucht jedes Element einmal, von links nach rechts. Währenddessen die Liste zu verändern, über die du gerade iterierst, führt zu überraschenden Sprüngen. Für den Einstieg: erst schleifen, danach ändern, oder über eine Kopie gehen (Kapitel 13).

## Prüfungsfallen

- `range(5)` enthält `5` nicht.
- `range(2, 2)` ist leer.
- Ein `while` ohne Änderung der Bedingung läuft weiter.
- `pass` setzt keine Variable und bricht nichts ab.
- `for i in 3` ist ein `TypeError`. Die 3 ist keine Sequenz. `for i in range(3)` ist richtig.
