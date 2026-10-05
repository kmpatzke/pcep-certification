# 1.1 Begriffe: Interpreter, Lexik, Syntax, Semantik

Python-Programme sind Text. Damit aus dem Text ein Ergebnis wird, muss jemand den Text lesen, seine Form prüfen und seine Bedeutung ausführen.

## Interpreter und Compiler

Ein **Compiler** übersetzt ein Programm, bevor es läuft, in eine andere Form. Das klassische Bild ist eine Sprache wie C: erst übersetzen, dann das Ergebnis starten.

Ein **Interpreter** liest das Programm und führt es aus. Python gehört in dieser Gegenüberstellung zum Interpreter. Das Programm, das deinen Quelltext ausführt, heißt Python-Interpreter.

CPython, die übliche Implementierung, erzeugt intern Bytecode und führt den in einer virtuellen Maschine aus. Die Prüfung fragt diese Pipeline nicht ab. Die erwartete Einordnung bleibt: Python wird interpretiert, ein Compiler übersetzt vor dem Lauf.

## Lexik, Syntax, Semantik

Die drei Ebenen trennen, *woraus* der Text besteht, *ob er wohlgeformt ist* und *was er bedeutet*.

- **Lexik:** die zulässigen Bausteine, die Lexeme. Dazu gehören Namen wie `print`, Zahlen wie `42`, Zeichen wie `(` und `:`, Operatoren wie `+`.
- **Syntax:** die zulässige Anordnung dieser Bausteine. `print("hi")` ist ein gültiger Aufruf. `print("hi"` ist es nicht, weil die Klammer fehlt.
- **Semantik:** die Bedeutung. `x = 1 / 0` ist syntaktisch ein normales Programm. Es scheitert erst bei der Ausführung, weil Division durch null keine Zahl ergibt.

```python
print("Hallo")

# Syntaxfehler: schließende Klammer fehlt
# print("Hallo"

print(1 / 0)  # Syntax in Ordnung, zur Laufzeit ZeroDivisionError
```

Ein Programm kann also richtig geschrieben sein und trotzdem abstürzen. Umgekehrt kommt ein Syntaxfehler, bevor die betroffene Anweisung als normale Laufzeitanweisung zu Ende ausgeführt wird.

## Was die Prüfung dazu wissen will

- Compiler übersetzt, Interpreter führt aus. Python: Interpreter.
- Lexik = Bausteine, Syntax = Form, Semantik = Bedeutung.
- `1 / 0` ist kein Tippfehler in der Form. Es ist ein Laufzeitfehler.
- Einrückungsfehler (`IndentationError`) sind Syntaxfehler. `IndentationError` ist eine Unterklasse von `SyntaxError`.

## Prüfungsfallen

- „Python kompiliert nach Bytecode“ ist ein Implementierungsdetail. Die Syllabus-Frage stellt Interpreter und Compiler gegenüber.
- Ein `SyntaxError` und ein `ZeroDivisionError` sind nicht dieselbe Klasse von Problem.
- Kommentare und leere Zeilen ändern die Bedeutung nicht. Ein fehlendes `:` nach `if` schon: das ist Syntax.
