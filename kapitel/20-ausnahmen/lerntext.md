# 4.4 Ausnahmen behandeln

`try` und `except` fangen einen Fehler, statt das Programm zu beenden.

```python
def sicher(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

Läuft der `try`-Block ohne Fehler, werden die `except`-Zweige übersprungen. Tritt ein Fehler auf, sucht Python den ersten passenden `except`.

`except Exception` fängt alles unter `Exception`. Ein nacktes `except:` fängt auch `BaseException`, also `KeyboardInterrupt` und `SystemExit`. Das verschluckt einen Abbruch. Für normale Fehler `except Exception` oder, besser, den konkreten Typ.

## Reihenfolge

Der erste passende Zweig gewinnt. Eine Oberklasse vor der Unterklasse macht den späteren Zweig unerreichbar.

```python
try:
    wert = int("x")
except ArithmeticError:
    art = "arithmetik"
except ValueError:
    art = "wert"
except Exception:
    art = "sonst"
# art == "wert"
```

Stünde `except Exception` oben, käme `ValueError` dort an und nie im eigenen Zweig.

## Weiterreichen

Fängt niemand, läuft die Ausnahme aus der Funktion hinaus, dann aus der aufrufenden Funktion, bis zum Interpreter.

```python
def innen():
    return 1 / 0

def aussen():
    return innen()

# aussen() wirft ZeroDivisionError
```

Das ist das Weiterreichen über Funktionsgrenzen. Die Verantwortung liegt bei dem, der fängt. Wer nicht fängt, gibt sie ab.

```python
def aussen():
    try:
        return innen()
    except ZeroDivisionError:
        return None
```

Hier übernimmt `aussen` die Verantwortung. `innen` bleibt ohne `try`.

## `raise`

`raise ValueError("Text")` wirft absichtlich. Im `except` reicht `raise` ohne Argument: dieselbe Ausnahme läuft weiter, nachdem du etwas getan hast.

```python
def pruefe(n):
    if n < 0:
        raise ValueError("negativ")
    return n
```

`else` am `try` läuft nur, wenn kein Fehler kam. `finally` läuft in jedem Fall, ob Fehler oder nicht, auch wenn du `return` sagst. Beides gehört zur `try`-Anweisung. Der Syllabus nennt ausdrücklich `try-except`. `finally` ist die Stelle für Aufräumen, das immer passieren soll.

## Prüfungsfallen

- Konkrete Klasse vor der Oberklasse.
- `except Exception` fängt kein `KeyboardInterrupt`.
- Ein gefangener Fehler verschwindet. Wer ihn nur anzeigen und weiterwerfen will, braucht `raise`.
- `return` im `except` ist ein normaler Rückgabewert. Die Ausnahme gilt dann als behandelt.
- Zwei `except` für denselben Fall: nur der erste läuft.
