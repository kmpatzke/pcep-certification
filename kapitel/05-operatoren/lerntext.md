# 1.4 Zahlenoperatoren, Zuweisung, Priorität, Gleitkomma

## Arithmetik

| Operator | Name | Beispiel | Ergebnis |
| --- | --- | --- | --- |
| `**` | Potenz | `2 ** 3` | `8` |
| `*` | Mal | `3 * 4` | `12` |
| `/` | Division | `7 / 2` | `3.5` (immer `float`) |
| `//` | ganzzahlige Division | `7 // 2` | `3` |
| `%` | Rest | `7 % 2` | `1` |
| `+` | Plus | `1 + 2` | `3` |
| `-` | Minus | `5 - 2` | `3` |

In Python 3 liefert `/` auch bei ganzen Zahlen einen Float: `4 / 2` ist `2.0`, nicht `2`.

`//` rundet in Richtung minus unendlich, nicht zur Null.

```python
7 // 2     # 3
-7 // 2    # -4
7 % 2      # 1
-7 % 2     # 1
```

Es gilt `dividend == (dividend // divisor) * divisor + (dividend % divisor)`. Der Rest übernimmt das Vorzeichen des **Divisors**.

## Unär und binär

Unär: ein Operand. `+x`, `-x`. Binär: zwei Operanden. `a + b`. Das Minus hat beide Rollen: `-3` ist unär, `5 - 3` ist binär.

## Strings: `+` und `*`

```python
"ab" + "c"    # "abc"
"ab" * 3      # "ababab"
3 * "ab"      # "ababab"
```

`"ab" + 3` ist ein `TypeError`. Ein String lässt sich nicht mit einer Zahl addieren. Multiplizieren geht nur mit einem `int`.

## Zuweisung und Kurzformen

```python
x = 10
x += 2    # x = x + 2
x -= 1
x *= 3
x //= 2
x %= 2
x **= 2
```

Die Kurzform liest den alten Wert, rechnet und bindet den Namen neu. `+=` bei einer Liste hängt an (Kapitel 13). Bei Zahlen entsteht ein neues Zahlenobjekt.

## Priorität und Bindung

Von hoch nach niedrig, soweit es dieser Block braucht:

1. `**`
2. unäres `+`, unäres `-`
3. `*`, `/`, `//`, `%`
4. binäres `+`, binäres `-`
5. Vergleiche (Kapitel 06)
6. `not`
7. `and`
8. `or`
9. Zuweisung

`*` und `+` binden nach links: `8 / 2 / 2` ist `(8 / 2) / 2` = `2.0`.

`**` bindet nach rechts: `2 ** 3 ** 2` ist `2 ** (3 ** 2)` = `512`, nicht `(2 ** 3) ** 2` = `64`.

```python
2 + 3 * 4      # 14, nicht 20
(2 + 3) * 4    # 20
```

## Genauigkeit von Gleitkommazahlen

`float` ist eine binäre Näherung. Viele Dezimalbrüche sind nicht exakt speicherbar.

```python
0.1 + 0.2 == 0.3   # False
0.1 + 0.2          # 0.30000000000000004
```

Für die Prüfung: `==` auf solche Floats nicht blind vertrauen. Zum Vergleich einen kleinen Abstand zulassen oder mit ganzen Zahlen rechnen.

## Prüfungsfallen

- `/` und `//` verwechseln. `7 / 2` ist `3.5`, `7 // 2` ist `3`.
- Negative `//`: `-7 // 2` ist `-4`, nicht `-3`.
- `2 ** 3 ** 2` ist `512`.
- `"2" + 2` wirft `TypeError`.
- `0.1 + 0.2` ist nicht exakt `0.3`.
