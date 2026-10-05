# 1.2 Struktur: Schlüsselwörter, Anweisungen, Einrückung, Kommentare

Python legt Blöcke nicht mit Klammern fest, sondern mit der Einrückung. Welche Wörter eine feste Bedeutung haben, steht in der Sprache selbst.

## Schlüsselwörter

Schlüsselwörter sind reserviert. Sie dürfen nicht als Variablenname verwendet werden. In Python 3 gehören dazu unter anderem:

`False`, `None`, `True`, `and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `not`, `or`, `pass`, `return`, `try`, `while`, `with`, `yield`.

Dazu kommen `async`, `await` und `nonlocal`. Die vollständige Liste liefert das Modul `keyword`:

```python
import keyword
keyword.iskeyword("if")    # True
keyword.iskeyword("If")    # False, Großschreibung zählt
keyword.iskeyword("name")  # False
```

`True`, `False` und `None` sind Schlüsselwörter, keine gewöhnlichen Variablen. `if = 1` ist ein Syntaxfehler.

Für PCEP musst du die Wörter wiedererkennen, die im Syllabus vorkommen: `if`, `elif`, `else`, `while`, `for`, `in`, `pass`, `break`, `continue`, `def`, `return`, `global`, `del`, `try`, `except`, `not`, `and`, `or`, `None`, `True`, `False`, `yield`. Die übrigen der Liste solltest du nicht als Namen benutzen.

## Anweisungen

Eine **Anweisung** (instruction) ist ein Schritt, den der Interpreter ausführt: eine Zuweisung, ein Aufruf, `if`, `while`, `return`. Ein Ausdruck wie `1 + 2` hat einen Wert. Steht er allein in der Zeile, ist er eine Ausdrucks-Anweisung.

Mehrere Anweisungen können in einer Zeile stehen, getrennt durch `;`. Das ist gültig und in PEP 8 unerwünscht. Für die Prüfung zählt: auch das sind getrennte Anweisungen.

```python
x = 1
y = 2
print(x + y)
```

Ein **Block** ist die eingerückte Folge von Anweisungen unter `if`, `while`, `for`, `def` oder `try`. Nach dem Doppelpunkt kommt der Block.

## Einrückung

- Der Block beginnt nach dem `:`.
- Üblich und in PEP 8 gefordert sind **vier Leerzeichen** pro Ebene. Tabs und Leerzeichen darf man nicht mischen.
- Alle Zeilen eines Blocks müssen gleich weit eingerückt sein.
- Eine leere Blockstelle ist verboten. Dafür gibt es `pass` (Kapitel 10).

```python
x = 3
if x > 0:
    print("positiv")
    if x > 10:
        print("gross")
print("immer")
```

`print("immer")` steht wieder auf Ebene 0 und gehört nicht zum `if`. Ein `IndentationError` ist ein `SyntaxError`.

## Kommentare

Alles von `#` bis zum Zeilenende ignoriert der Interpreter. Ein Kommentar ändert das Ergebnis nicht.

```python
x = 1  # Startwert
# x = 99
print(x)  # gibt 1 aus
```

Eine Zeichenkette in dreifachen Anführungszeichen ist **kein** Kommentar, sondern ein String. Steht sie als erste Anweisung in einer Funktion, ist sie ein Docstring: ein Wert, den die Funktion trägt, kein auskommentierter Code.

```python
def flaeche(a, b):
    """Gibt das Produkt zurück."""
    return a * b
```

## Prüfungsfallen

- `True` und `true` sind nicht dasselbe. Nur `True` ist das Schlüsselwort.
- Einrückung ist Syntax, kein Stil. Falsche Einrückung startet das Programm nicht.
- `#` kommentiert nur den Rest der Zeile aus, nicht die nächste Zeile.
- `""" ... """` schaltet den Interpreter nicht ab. Es erzeugt einen String.
