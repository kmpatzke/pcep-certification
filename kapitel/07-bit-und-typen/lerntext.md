# 1.4 Bitoperatoren und Typumwandlung

Bitoperatoren arbeiten auf der Zweierdarstellung ganzer Zahlen. Typumwandlung baut aus einem Wert einen Wert eines anderen Typs.

## Bitoperatoren

| Operator | Name | Beispiel | Ergebnis |
| --- | --- | --- | --- |
| `&` | und | `5 & 3` | `1` |
| `&#124;` | oder | `5 &#124; 2` | `7` |
| `^` | exklusives oder | `5 ^ 1` | `4` |
| `~` | Komplement | `~0` | `-1` |
| `<<` | links schieben | `5 << 1` | `10` |
| `>>` | rechts schieben | `5 >> 1` | `2` |

`5` ist binär `101`, `3` ist `011`. Stelle für Stelle und: `001`, also `1`.

`~n` ist gleich `-n - 1`. `~5` ist `-6`. `~` ist unär und hat hohe Priorität, höher als die binären Bitoperatoren.

`<< 1` verdoppelt eine nichtnegative ganze Zahl, `>> 1` halbiert sie ganzzahlig. Das ist eine Merkhilfe, keine Definition für negative Zahlen. In der Prüfung reichen kleine nichtnegative Beispiele.

Priorität unter den Bitoperatoren: `~`, dann `<<` und `>>`, dann `&`, dann `^`, dann `|`. Arithmetik (`+`, `*`) bindet enger als die Schiebeoperatoren.

```python
1 << 2 + 1    # 1 << 3 == 8, nicht (1 << 2) + 1
```

## Typumwandlung

```python
int(3.9)         # 3, zur Null hin, nicht runden
int(-3.9)        # -3
int("42")        # 42
int(" 42 ")      # 42, Whitespace an den Enden ist erlaubt
int(True)        # 1
float(2)         # 2.0
float("1.5")     # 1.5
float("2e1")     # 20.0
str(20)          # "20"
bool(0)          # False
bool("False")    # True, der String ist nicht leer
```

`int("1.5")` wirft `ValueError`. Erst `float`, dann `int`: `int(float("1.5"))` ist `1`.

`int("ff")` wirft `ValueError`. `int("ff", 16)` ist `255` (Kapitel 04).

`int()` erwartet keinen leeren String. `float("abc")` ist `ValueError`. `int("42.0")` ist ebenfalls `ValueError`, weil der Punkt keine Ganzzahl-Ziffer ist.

Runden ist nicht `int`. `int` schneidet den Nachkommateil ab, Richtung 0.

## Prüfungsfallen

- `~5` ist `-6`, nicht `5` mit umgedrehtem Vorzeichen allein und nicht `0`.
- `1 << 2 + 1` ist `8`.
- `int(2.9)` ist `2`, `int(-2.9)` ist `-2`.
- `int("2.9")` stürzt ab. `float("2.9")` nicht.
- `bool("False")` ist `True`.
