# Testprüfung 04

Übungssatz für **PCEP-30-02**. Alle Aufgaben sind selbst geschrieben. Es sind keine offiziellen Prüfungsitems.

| | |
| --- | --- |
| Aufgaben | 30 |
| Zeit | 40 Minuten |
| Bestehen | 70 von 100 Punkten |
| Block 1 | Aufgaben 1–7, zusammen 18 Punkte |
| Block 2 | Aufgaben 8–15, zusammen 29 Punkte |
| Block 3 | Aufgaben 16–22, zusammen 25 Punkte |
| Block 4 | Aufgaben 23–30, zusammen 28 Punkte |

Eine Aufgabe zählt nur, wenn sie vollständig stimmt. Mehrfachauswahl, Zuordnung und Sortierung geben hier keinen Teilpunkt.

Bearbeite nur den Frageteil. Der Lösungsteil steht unter dem Trenner.

## Frageteil

### Frage 1 · Einzelauswahl · Block 1 · Ziel 1.1 · 2 Punkte

Welche Aufgabe hat ein Compiler in der Syllabus-Gegenüberstellung?

- A) Er führt jede Zeile sofort aus und speichert nichts.
- B) Er übersetzt das Programm, bevor es läuft.
- C) Er prüft nur PEP 8 und bricht bei Stilfehlern ab.
- D) Er ersetzt `print` durch `return`.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Was ist ein Docstring am Anfang einer Funktion?

- A) Ein Kommentar, den der Interpreter vor dem Parsen löscht.
- B) Ein String-Literal, kein Kommentar.
- C) Ein Syntaxfehler, sobald drei Anführungszeichen vorkommen.
- D) Eine Zuweisung an `None`.

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welche Ausdrücke haben den Wert `1`? Wähle alle zutreffenden Antworten.

- A) `-7 % 2`
- B) `7 % 2`
- C) `5 & 3`
- D) `int(True)`

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

Welche ganze Zahl bezeichnet das oktale Literal `0o17`? Schreibe nur die Zahl im Zehnersystem: ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `3 * 2 ** 3`?

- A) `24`
- B) `48`
- C) `216`
- D) `18`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.5 · 3 Punkte

Ergänze den Parameternamen, damit nach den Werten ein Ausrufezeichen steht und kein zusätzliches Trennzeichen zwischen `1` und `2` neben dem normalen Leerzeichen geändert wird. Die Ausgabe soll mit `1 2!` enden, ohne weiteren Zeilenumbruch aus `end`.

```python
print(1, 2, ___="!")
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welchen Wahrheitswert hat `bool("False")`?

- A) `False`, weil der Text das Wort false enthält
- B) `True`, weil der String nicht leer ist
- C) `None`
- D) der Aufruf wirft `ValueError`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
x = 5
spur = ""
if x > 0:
    spur += "a"
elif x > 3:
    spur += "b"
```

Was steht in `spur`?

- A) `"ab"`
- B) `"b"`
- C) `"a"`
- D) `""`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche `range`-Aufrufe sind leer? Wähle alle zutreffenden Antworten.

- A) `range(0)`
- B) `range(3, 1)`
- C) `range(2, 5)`
- D) `range(1, 1)`

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

```python
s = ""
for i in range(3):
    s += str(i)
else:
    s += "E"
```

Die Schleife enthält kein `break`. Was steht am Ende in `s`?

- A) `"012"`
- B) `"012E"`
- C) `"E"`
- D) `"01E2"`

### Frage 11 · Sortieren · Block 2 · Ziel 2.1 · 4 Punkte

Ordne die Operatoren von hoher zu niedriger Priorität. Gib die Buchstaben an.

- A) `and`
- B) `*`
- C) `==`
- D) `not`

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt `list(range(4, 0, -2))`?

- A) `[4, 2, 0]`
- B) `[4, 2]`
- C) `[4, 3, 2, 1]`
- D) `[2, 0]`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile lässt aus `"abca"` den String `"bc"` entstehen?

```python
ergebnis = ""
for zeichen in "abca":
    ___
    ergebnis += zeichen
```

- A) `if zeichen == "a": continue`
- B) `if zeichen == "a": break`
- C) `if zeichen == "b": continue`
- D) `if zeichen == "a": ergebnis = ""`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Ein `while` soll die Summe `1 + 2 + 3 + 4` berechnen und dann aufhören. Welche Bestandteile gehören dazu? Wähle alle zutreffenden Antworten.

- A) eine Bedingung, die irgendwann falsch wird
- B) eine Änderung des Zählers im Körper
- C) `break` ist die einzige zulässige Art, ein `while` zu beenden
- D) `range` ist für jedes `while` vorgeschrieben

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

Wie viele Durchläufe hat `for i in range(3)`? Schreibe die Anzahl ___.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.4 · 4 Punkte

Was ergibt `"Python"[1:4]`?

- A) `"Pyt"`
- B) `"yth"`
- C) `"ytho"`
- D) `"Pyth"`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

Welche Ausdrücke sind Tupel mit genau zwei Elementen? Wähle alle zutreffenden Antworten.

- A) `(1, 2)`
- B) `1, 2`
- C) `(1)`
- D) `(1,) + (2,)`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.4 · 4 Punkte

Ordne zu.

1. `"  Ab ".strip().lower()`
2. `"aba".count("a")`
3. `",".join(["x", "y"])`
4. `"x-y".split("-")`

- A) `2`
- B) `"ab"`
- C) `"x,y"`
- D) `["x", "y"]`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze die Anweisung, die den Index `0` entfernt. Das Wort vor der Liste ist kein Methodenaufruf.

```python
werte = [9, 1, 2]
___ werte[0]
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.1 · 3 Punkte

`a = [1, 2]` und `b = a` und danach `b += [3]`. Was steht in `a`?

- A) `[1, 2]`
- B) `[1, 2, 3]`
- C) `[3]`
- D) `None`

### Frage 21 · Lückentext · Block 3 · Ziel 3.3 · 4 Punkte

`{}["a"]` wirft ___. Schreibe den Ausnahmenamen.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Aussagen über Listen-Comprehensions stimmen? Wähle alle zutreffenden Antworten.

- A) `[n * n for n in range(4)]` ergibt `[0, 1, 4, 9]`.
- B) Ein `if` am Ende filtert Elemente.
- C) Die Comprehension ändert die Quelle, über die sie iteriert, an Ort und Stelle.
- D) Links vom `for` steht der Wert, der in die neue Liste kommt.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

Was liefert `summe_bis(0)`, wenn die Funktion bei `n <= 0` sofort `0` zurückgibt und sonst `n + summe_bis(n - 1)` rechnet?

- A) `0`
- B) `1`
- C) `None`
- D) `RecursionError`

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Signatur ist gültig?

- A) `def gruss(name, zeichen="!"):`
- B) `def gruss(name="Ada", zeichen):`
- C) `def gruss(name, zeichen): return`
- D) sowohl A als auch C

Die Frage ist eine Einzelzuordnung im Stil „Code einsetzen“: welche der drei Signaturen darf so stehen? Wähle die eine richtige Option. Option D meint, dass A und C beide gültig sind.

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 4 Punkte

Welche Aufrufe gehören zu einer Funktion `def addiere(a, b): return a + b` und ergeben `7`? Wähle alle zutreffenden Antworten.

- A) `addiere(3, 4)`
- B) `addiere(a=3, b=4)`
- C) `addiere(b=4, a=3)`
- D) `addiere(3, b=4, a=3)`

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Ordne die Teile eines behandelten Fehlers so, wie sie zeitlich ablaufen, wenn `int("x")` im `try` steht und ein passendes `except ValueError` folgt. Gib die Buchstaben an.

- A) der `except`-Block
- B) der Fehler entsteht im `try`
- C) die Funktion gibt den Ersatzwert zurück, der im `except` steht

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`~(0)` hat den Wert ___. Schreibe die ganze Zahl.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Von welcher Klasse erbt `SystemExit` direkt im Syllabus-Bild?

- A) `Exception`
- B) `BaseException`
- C) `KeyboardInterrupt`
- D) `ArithmeticError`

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze das Schlüsselwort, das im `except` dieselbe Ausnahme erneut wirft.

```python
except ValueError:
    gesehen = True
    ___
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `IndexError` ist eine Unterklasse von `KeyError`.
- B) `IndexError` ist eine Unterklasse von `LookupError`.
- C) `KeyError` ist eine Unterklasse von `LookupError`.
- D) `except IndexError` fängt auch `KeyError`.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** B

**Erklärung:** Der Compiler übersetzt vor dem Lauf. Ausführen ist die Rolle des Interpreters.

### Frage 2

**Antwort:** B

**Erklärung:** Drei Anführungszeichen bauen einen String. Ein `#` wäre der Kommentar.

### Frage 3

**Antwort:** A, B, C, D

**Erklärung:** Der Rest von `-7 // 2` ist `1`. `7 % 2` ist `1`. `5 & 3` ist `1`. `int(True)` ist `1`.

### Frage 4

**Antwort:** 15

**Erklärung:** Oktal `17` ist `1 * 8 + 7`.

### Frage 5

**Antwort:** A

**Erklärung:** `**` bindet enger als `*`. `2 ** 3` ist `8`, mal `3` ist `24`.

### Frage 6

**Antwort:** `end`

**Erklärung:** `end` ersetzt den abschließenden Zeilenumbruch. `sep` bliebe das Leerzeichen.

### Frage 7

**Antwort:** B

**Erklärung:** Jeder nicht leere String ist wahr, auch wenn sein Text `False` lautet.

### Frage 8

**Antwort:** C

**Erklärung:** Das erste `if` ist wahr. `elif` wird nicht mehr geprüft, obwohl `x > 3` ebenfalls wahr wäre.

### Frage 9

**Antwort:** A, B, D

**Erklärung:** `range(0)`, `range(3, 1)` mit positivem Schritt und `range(1, 1)` enthalten keine Werte. `range(2, 5)` ist `2, 3, 4`.

### Frage 10

**Antwort:** B

**Erklärung:** Ohne `break` läuft das Schleifen-`else` nach `0`, `1` und `2`.

### Frage 11

**Antwort:** B, C, D, A

**Erklärung:** `*` vor Vergleich, Vergleich vor `not`, `not` vor `and`.

### Frage 12

**Antwort:** B

**Erklärung:** Start `4`, Schritt `-2`, Stopp `0` ausgeschlossen: `4` und `2`.

### Frage 13

**Antwort:** A

**Erklärung:** Beide `a` werden übersprungen. `break` beim ersten `a` würde gar nichts mehr anhängen.

### Frage 14

**Antwort:** A, B

**Erklärung:** Ein `while` endet, wenn die Bedingung falsch wird. `break` ist möglich, aber nicht die einzige Art. `range` gehört zu `for`.

### Frage 15

**Antwort:** 3

**Erklärung:** Die Indizes sind `0`, `1` und `2`.

### Frage 16

**Antwort:** B

**Erklärung:** Indizes 1, 2 und 3 von `"Python"` sind `y`, `t` und `h`.

### Frage 17

**Antwort:** A, B, D

**Erklärung:** Das Komma baut das Tupel, die Klammern sind dabei optional. `(1,)` plus `(2,)` ist `(1, 2)`.

### Frage 18

**Antwort:** 1–B, 2–A, 3–C, 4–D

**Erklärung:** `strip` und `lower` ergeben `"ab"`. `count` zählt zwei `a`. `join` und `split` sind Gegenstücke.

### Frage 19

**Antwort:** `del`

**Erklärung:** `del` ist eine Anweisung. Dahinter steht das Ziel, kein Methodenpunkt.

### Frage 20

**Antwort:** B

**Erklärung:** `b` ist kein zweites Listenobjekt. `+=` mit einer Liste verändert dasselbe Objekt.

### Frage 21

**Antwort:** KeyError

**Erklärung:** Der Schlüssel fehlt. Das ist kein `IndexError`.

### Frage 22

**Antwort:** A, B, D

**Erklärung:** Die Comprehension baut eine neue Liste. Sie schreibt nicht in die durchlaufene Quelle zurück.

### Frage 23

**Antwort:** A

**Erklärung:** Der Basisfall liefert sofort `0` und ruft sich nicht auf.

### Frage 24

**Antwort:** D

**Erklärung:** Standardwerte müssen hinten stehen. A erfüllt das. C hat keine Standards und ist ebenfalls gültig. B ist ein Syntaxfehler.

### Frage 25

**Antwort:** A, B, C

**Erklärung:** D übergibt `a` zweimal, einmal positional und einmal als Name. Das ist ein `TypeError`.

### Frage 26

**Antwort:** B, A, C

**Erklärung:** Zuerst scheitert der `try`-Körper, dann läuft der passende `except`, und dessen `return` wird zum Ergebnis.

### Frage 27

**Antwort:** -1

**Erklärung:** `~n` ist `-n - 1`. Für `0` bleibt `-1`.

### Frage 28

**Antwort:** B

**Erklärung:** `SystemExit` hängt nicht unter `Exception`. Deshalb fängt `except Exception` es nicht.

### Frage 29

**Antwort:** `raise`

**Erklärung:** `raise` ohne Argument im `except` wirft dieselbe Ausnahme weiter.

### Frage 30

**Antwort:** B, C

**Erklärung:** Beide Nachschlagen-Fehler liegen unter `LookupError`, aber nicht untereinander.
