# 1.3 Literale, Variablen und PEP 8

Ein **Literal** ist ein Wert, der direkt im Quelltext steht. Eine **Variable** ist ein Name, der auf ein Objekt zeigt.

## Die Literale aus dem Syllabus

```python
True          # Boolesch, Schlüsselwort
False
42            # int, beliebig groß
3.5           # float
2e3           # float, wissenschaftliche Schreibweise: 2000.0
"Hallo"       # str
'Hallo'       # derselbe Typ, andere Anführungszeichen
```

`2e3` bedeutet 2 mal 10 hoch 3. Das Ergebnis ist immer ein `float`, auch wenn die Zahl mathematisch ganz ist. `1.5e-1` ist `0.15`. Der Exponent kann `e` oder `E` sein.

Boolesche Literale schreibt man `True` und `False`, nicht `true`.

Strings behandelt Kapitel 16 im Detail. Hier reicht: ein String-Literal steht in einfachen oder doppelten Anführungszeichen. `"42"` ist Text, nicht die Zahl 42.

Zahlensysteme (`0b`, `0o`, `0x`) sind ebenfalls Teil von 1.3 und liegen in Kapitel 04.

## Variablen

```python
alter = 20
alter = alter + 1   # derselbe Name, neues Objekt
```

Die Zuweisung bindet den Namen neu. Sie kopiert nicht automatisch eine Liste (das wird in Kapitel 13 wichtig).

Regeln für Namen:

- Erstes Zeichen: Buchstabe oder `_`. Danach Buchstaben, Ziffern und `_`.
- Groß- und Kleinschreibung sind verschieden: `Wert` und `wert` sind zwei Namen.
- Schlüsselwörter sind verboten.
- Ein Name darf nicht mit einer Ziffer beginnen: `2wert` ist Syntax.

Konvention, nicht Syntax: sprechende Namen, `snake_case` für Variablen und Funktionen, `GROSSBUCHSTABEN` für Konstanten. Ein einzelner Buchstabe `l`, `O` oder `I` ist leicht mit Ziffern zu verwechseln. PEP 8 rät davon ab.

## PEP 8, soweit es die Prüfung braucht

PEP 8 ist der Stil-Leitfaden, keine zusätzliche Syntax. Der Interpreter führt auch hässlichen Code aus. Die Prüfung erwartet, dass du die Empfehlungen erkennst.

- Einrückung: 4 Leerzeichen, keine Tabs.
- Eine Anweisung pro Zeile. Kein `;`, um Zeilen zu stapeln.
- Leerzeichen um Operatoren: `a = b + c`, nicht `a=b+c`.
- Nach einem Komma ein Leerzeichen: `print(1, 2)`.
- Funktions- und Variablennamen: `klein_mit_unterstrich`.
- Zwischen zwei Funktionen auf Modul-Ebene zwei Leerzeilen.
- Zeilen möglichst nicht länger als 79 Zeichen.

Kein Stilfehler, sondern ein Syntaxfehler: falsche Einrückung, Schlüsselwort als Name, fehlender Doppelpunkt.

## Typ ist eine Eigenschaft des Objekts

```python
x = 1
x = "eins"   # erlaubt, der Name zeigt jetzt auf einen str
```

Python ist dynamisch getypt. `type(1)` ist `int`, `type(1.0)` ist `float`, `type(True)` ist `bool`, `type("a")` ist `str`. `bool` ist eine Unterklasse von `int`. Das wird bei Vergleichen in Kapitel 06 wichtig: `True == 1` ist wahr.

## Prüfungsfallen

- `2e2` ist `200.0`, Typ `float`, nicht `int`.
- `"True"` ist ein String. `True` ist ein Bool.
- `variable` und `Variable` sind zwei Namen.
- PEP-8-Verstöße lassen das Programm laufen. Syntaxfehler nicht.
