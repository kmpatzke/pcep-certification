# 4.3 Eingebaute Ausnahmehierarchie

Wenn etwas zur Laufzeit scheitert, erzeugt Python ein Ausnahmeobjekt. Der Typ sagt, was schiefging. Die Typen hängen in einer Hierarchie.

```text
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── TypeError
      └── ValueError
```

`ArithmeticError` hat außerdem `OverflowError` und `FloatingPointError`. Für PCEP reicht: `ZeroDivisionError` liegt unter `ArithmeticError`.

## Was die Namen bedeuten

- `BaseException` ist die Wurzel. Fast alles, was `raise` erzeugen kann, hängt hier.
- `Exception` ist die Wurzel der gewöhnlichen Fehler. Eigene und die meisten eingebauten Fehler erben von hier.
- `SystemExit` entsteht, wenn der Interpreter beendet werden soll (`sys.exit()`). Es erbt von `BaseException`, nicht von `Exception`.
- `KeyboardInterrupt` entsteht, wenn die Ausführung von außen unterbrochen wird (Strg+C). Ebenfalls direkt unter `BaseException`.
- `ArithmeticError` und `LookupError` nennt der Syllabus abstrakte Ausnahmen. Du fängst sie, um eine ganze Gruppe zu treffen. Die konkreten Fälle sind die Unterklassen.
- `IndexError`: Index außerhalb einer Sequenz.
- `KeyError`: fehlender Dictionary-Schlüssel.
- `TypeError`: Operation passt nicht zum Typ, zum Beispiel `"a" + 1`.
- `ValueError`: Typ passt, Wert nicht, zum Beispiel `int("ff")` oder `int("1.5")`.

`except Exception` fängt `ZeroDivisionError`, `IndexError`, `KeyError`, `TypeError` und `ValueError`. Es fängt **nicht** `KeyboardInterrupt` und **nicht** `SystemExit`.

```python
isinstance(IndexError(), LookupError)          # True
isinstance(KeyError(), LookupError)            # True
isinstance(ZeroDivisionError(), ArithmeticError)  # True
isinstance(KeyboardInterrupt(), Exception)     # False
isinstance(SystemExit(), Exception)            # False
```

## Welcher Fehler wann

| Situation | Typ |
| --- | --- |
| `1 / 0` | `ZeroDivisionError` |
| `[1][3]` | `IndexError` |
| `{}["a"]` | `KeyError` |
| `"a" + 1` | `TypeError` |
| `int("x")` | `ValueError` |
| `(1, 2)[0] = 9` | `TypeError` |

`IndexError` und `KeyError` sind beides Nachfahren von `LookupError`, aber nicht voneinander. Ein `except IndexError` fängt keinen `KeyError`.

## Prüfungsfallen

- `KeyboardInterrupt` hängt nicht unter `Exception`.
- `IndexError` ist kein `KeyError`. Beide sind `LookupError`.
- `int("1.5")` ist `ValueError`, nicht `TypeError`. Der Typ `str` ist für `int` zulässig, der Inhalt nicht.
- `"a" + 1` ist `TypeError`, nicht `ValueError`.
- Abstrakt heißt hier: Oberklasse einer Gruppe, nicht „kann man nicht fangen“.
