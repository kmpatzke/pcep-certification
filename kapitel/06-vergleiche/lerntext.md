# 1.4 Vergleiche und Boolesche Operatoren

## Vergleiche

| Operator | Bedeutung |
| --- | --- |
| `==` | gleich (Wert) |
| `!=` | ungleich |
| `>` | größer |
| `>=` | größer oder gleich |
| `<` | kleiner |
| `<=` | kleiner oder gleich |

```python
3 == 3      # True
3 != 4      # True
"a" < "b"   # True, lexikografisch
```

`==` vergleicht Werte. `is` vergleicht, ob es dasselbe Objekt ist. `is` steht nicht in der Operatorliste von 1.4, ist aber ein Schlüsselwort. Für Zahlen und Strings in der Prüfung `==` verwenden. `is` nur für `None`: `x is None`.

Ketten sind erlaubt und bedeuten „beide Vergleiche“:

```python
1 < 2 < 3          # True, das ist 1 < 2 and 2 < 3
(1 < 2) < 3        # True < 3, und True == 1, also ebenfalls True
3 < 2 < 1          # False
```

`True == 1` und `False == 0` sind wahr, weil `bool` eine Unterklasse von `int` ist. `True + True` ist `2`.

## `not`, `and`, `or`

`not` liefert immer `True` oder `False`.

```python
not True     # False
not 0        # True
not ""       # True
not "0"      # False, der String ist nicht leer
not []       # True
```

Falsch sind: `False`, `None`, `0`, `0.0`, `""`, leere Liste, leeres Tupel, leeres Dictionary. Alles andere ist in Booleschem Kontext wahr. Auch `"0"` und `[0]`.

`and` und `or` liefern nicht immer einen Bool. Sie liefern den Operanden, der das Ergebnis entscheidet.

- `a and b`: wenn `a` falsch ist, `a`, sonst `b`.
- `a or b`: wenn `a` wahr ist, `a`, sonst `b`.

```python
1 and 2      # 2
0 and 2      # 0
0 or 5       # 5
3 or 5       # 3
```

Priorität: `not` vor `and` vor `or`.

```python
True or False and False    # True, weil and zuerst False ergibt, dann True or False
not 1 and 0                # False
```

## Prüfungsfallen

- `=` ist Zuweisung, `==` ist Vergleich. `if x = 1` ist ein Syntaxfehler.
- `1 < 2 < 3` ist nicht dasselbe Muster wie `(1 < 2) < 3`, auch wenn beide hier `True` sind. Bei anderen Zahlen kippt es: `(3 < 2) < 1` ist `False < 1` und damit `True`. `3 < 2 < 1` ist `False`.
- `and` / `or` können Zahlen und Strings zurückgeben, nicht nur `True` und `False`.
- `not "0"` ist `False`.
