# 4.1 Funktionen, `return`, `None`, Rekursion, Generatoren

## Definieren und aufrufen

```python
def flaeche(a, b):
    return a * b

flaeche(2, 3)    # 6
```

`def` legt die Funktion an. Der Aufruf schreibt Klammern, auch wenn keine Argumente nötig sind: `f()`. Ohne Klammern bekommst du das Funktionsobjekt, nicht das Ergebnis.

## `return` und `None`

`return` beendet die Funktion und gibt den Wert zurück. Ohne `return`, oder mit `return` ohne Ausdruck, ist das Ergebnis `None`.

```python
def nichts():
    x = 1

nichts() is None    # True

def auch():
    return

auch() is None      # True
```

`None` ist ein Schlüsselwort und der einzige Wert seines Typs. Vergleiche mit `is None`, nicht mit `==`, auch wenn `==` hier ebenfalls wahr ist.

Mehrere `return`-Zeilen sind erlaubt. Es wird nur eine erreicht.

```python
def vorzeichen(n):
    if n > 0:
        return "plus"
    if n < 0:
        return "minus"
    return "null"
```

`print` ist kein `return`. Eine Funktion, die nur druckt, liefert `None`.

## Rekursion

Eine Funktion darf sich selbst aufrufen. Es braucht einen Zweig, der nicht mehr aufruft, sonst wächst der Stapel, bis `RecursionError` kommt.

```python
def summe_bis(n):
    if n <= 0:
        return 0
    return n + summe_bis(n - 1)

summe_bis(3)    # 6
```

Jeder Aufruf hat eigene lokale Namen.

## Generatoren

Eine Funktion mit `yield` ist ein Generator. Der Aufruf liefert ein Generator-Objekt und führt den Körper noch nicht aus. Erst die Iteration läuft bis zum nächsten `yield` und pausiert dort.

```python
def zaehle(n):
    i = 0
    while i < n:
        yield i
        i += 1

list(zaehle(3))    # [0, 1, 2]
```

`return` in einem Generator beendet ihn. Der zurückgegebene Wert ist nicht das, was `list()` sammelt. Gesammelt werden die `yield`-Werte.

## Prüfungsfallen

- Fehlende Klammern: `f` ist nicht `f()`.
- Vergessenes `return` ergibt `None`, auch wenn du den Wert vorher ausgerechnet hast.
- `print(x)` zeigt `x`, gibt ihn aber nicht an den Aufrufer zurück.
- Rekursion ohne Abbruch endet mit `RecursionError`, nicht mit einer Endlosschleife im selben Rahmen. Es ist trotzdem ein Lauf ohne Ende bis zum Fehler.
- `yield` macht aus dem Aufruf einen Generator. `zaehle(3)` ist nicht die Liste `[0, 1, 2]`, solange niemand iteriert.
