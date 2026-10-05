# Testprüfung 05

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

`IndentationError` gehört zu welcher Klasse von Fehlern?

- A) Er ist ein `SyntaxError`.
- B) Er ist immer ein `ZeroDivisionError`.
- C) Er ist ein reiner Stilhinweis und stoppt das Programm nicht.
- D) Er entsteht nur bei `1 / 0`.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Welcher Name ist erlaubt?

- A) `if`
- B) `None`
- C) `summe`
- D) `for`

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

Welche Ausdrücke sind Strings, keine Zahlen? Wähle alle zutreffenden Antworten.

- A) `bin(10)`
- B) `0b1010`
- C) `hex(255)`
- D) `0xFF`

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

`int("ff", 16)` ergibt ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `8 / 2 / 2`?

- A) `8`
- B) `2`
- C) `2.0`
- D) `1`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.5 · 3 Punkte

Der Text aus der Eingabe liegt in `roh`. Ergänze die Funktion, die daraus eine ganze Zahl macht.

```python
zahl = ___(roh)
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

```python
x = 10
x += 2
x //= 3
x **= 2
```

Was steht am Ende in `x`?

- A) `16`
- B) `12`
- C) `8`
- D) `36`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

An welches `if` bindet das `else`, wenn beide Zweige korrekt eingerückt sind und das `else` auf derselben Spalte steht wie das äußere `if`?

```python
if alter >= 18:
    if karte:
        eintritt = "ja"
else:
    eintritt = "nein"
```

- A) an das innere `if karte`
- B) an das äußere `if alter >= 18`
- C) an beide gleichzeitig
- D) an kein `if`, das ist ein Syntaxfehler

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Werte sind im Booleschen Sinn falsch? Wähle alle zutreffenden Antworten.

- A) `0`
- B) `"0"`
- C) `[]`
- D) `None`

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

Ein Programm geht `range(2, 4)` durch und sucht die Zahl `9`. Findet es sie, führt es `break` aus. Das `else` der Schleife setzt `status = "kein_break"`. Welchen Wert hat `status` danach, wenn es vorher nicht gesetzt war und nur im `else` gesetzt wird?

- A) die Variable bleibt ungebunden
- B) `"kein_break"`
- C) `9`
- D) `None`

### Frage 11 · Sortieren · Block 2 · Ziel 2.1 · 4 Punkte

Ordne die Zeilen so, dass zuerst der Startwert steht, dann die Entscheidung, dann der eine Zweig, dann die Anweisung danach. Gib die Buchstaben an.

- A) `print(text)`
- B) `text = "klein"`
- C) `if wert > 12:`
- D) `text = "ok"`

`wert` ist bereits `15`. Der `if`-Körper soll nur die eine Zuweisung `"ok"` enthalten. `print` steht wieder auf der äußeren Ebene.

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was passiert bei `for i in 3:`?

- A) Die Schleife läuft dreimal mit `i` gleich `0`, `1` und `2`.
- B) `TypeError`, weil `3` keine Folge ist.
- C) Die Schleife läuft einmal mit `i` gleich `3`.
- D) `SyntaxError`, weil `in` kein Schlüsselwort ist.

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile lässt die äußere Schleife weiterlaufen, beendet aber die innere, sobald `b` den Wert `1` hat? Der schon geschriebene `break` sitzt im inneren Körper.

```python
for a in range(2):
    for b in range(3):
        if b == 1:
            ___
```

- A) `break`
- B) `continue`
- C) `return`
- D) `pass`

Es geht um das Schlüsselwort, das nur die innere Schleife verlässt.

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Aussagen über `pass` stimmen? Wähle alle zutreffenden Antworten.

- A) Es ist eine eigene Anweisung.
- B) Es kommentiert den Block aus.
- C) Es kann den Körper eines `if` füllen.
- D) Es setzt die Variable `pass` auf `True`.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

`list(range(1, 6, 2))` ergibt eine Liste mit den Werten ___. Schreibe sie als Python-Literal, zum Beispiel `[1, 2]`.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

```python
werte = [10, 20, 30]
kopie = werte[:]
```

Welche Aussage stimmt?

- A) `kopie is werte` ist wahr.
- B) `kopie == werte` ist wahr, `kopie is werte` ist falsch.
- C) `kopie` ist ein Tupel.
- D) Der Slice wirft `IndexError`, weil die Grenzen fehlen.

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.3 · 3 Punkte

Welche Objekte dürfen ein Dictionary-Schlüssel sein? Wähle alle zutreffenden Antworten.

- A) `"name"`
- B) `(1, 2)`
- C) `[1, 2]`
- D) `1815`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.4 · 4 Punkte

Ordne jedes Literal dem zu, was in seinem Wert wirklich steht.

1. `"a\\b"`
2. `"a\nb"`
3. `"Ada's"`
4. `"oben\nunten"`

- A) ein Backslash zwischen zwei Buchstaben
- B) ein Zeilenumbruch zwischen `a` und `b`
- C) ein Apostroph, ohne Escape geschrieben
- D) ein Zeilenumbruch zwischen zwei Wörtern

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze die Methode, die `3` ans Ende hängt.

```python
werte = [1, 2]
werte.___(3)
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.1 · 3 Punkte

`20 in [10, 20, 30]` ergibt was?

- A) `1`
- B) `True`
- C) `20`
- D) `IndexError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.2 · 4 Punkte

`(10, 20, 30)[1:]` ergibt ___. Schreibe das Tupel-Literal.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `"ab".find("z")` ist `-1`.
- B) `"ab".index("z")` wirft `ValueError`.
- C) `"ab".find("z")` wirft `ValueError`.
- D) `len("ab")` ist ein Funktionsaufruf, keine Methode.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

```python
def flaeche(a, b):
    return a * b

wert = flaeche
```

Was ist `wert`?

- A) das Ergebnis `None`, weil die Klammern fehlen
- B) das Funktionsobjekt, noch ohne Aufruf
- C) die Zahl `0`
- D) ein Generator

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Die Funktion soll das äußere `x` nur lesen. Welche Zeile ist der komplette Körper?

```python
x = 1

def lesen():
    ___
```

- A) `return x`
- B) `global x`
- C) `x = x + 1`
- D) `x = 2`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
def merke(wert, stand=0):
    stand += wert
    return stand
```

Zweimal aufgerufen als `merke(1)` und danach noch einmal `merke(1)`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Beide Aufrufe geben `1` zurück.
- B) Der zweite Aufruf gibt `2` zurück, weil der Default sich merkt.
- C) Zahlen-Defaults werden nicht an Ort und Stelle verändert. `+=` bindet einen lokalen Namen.
- D) `stand` in der Funktion ist lokal.

### Frage 26 · Sortieren · Block 4 · Ziel 4.3 · 3 Punkte

Ordne von der Wurzel zu `KeyboardInterrupt`. Gib die Buchstaben an.

- A) `KeyboardInterrupt`
- B) `BaseException`
- C) `Exception`

Nicht jeder Name liegt auf dem Weg. Lass die Klasse weg, die nicht zwischen Wurzel und `KeyboardInterrupt` steht. Die Antwort enthält nur die Klassen auf diesem Weg, von oben nach unten.

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`(1, 2)[9]` wirft ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

`except Exception` steht über `except ValueError`. Was passiert bei `int("x")`?

- A) Der `ValueError`-Zweig läuft, weil er genauer ist.
- B) Der `Exception`-Zweig läuft, der `ValueError`-Zweig ist unerreichbar.
- C) Beide Zweige laufen.
- D) `SyntaxError`, weil zwei `except` verboten sind.

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze so, dass gewöhnliche Fehler gefangen werden, `KeyboardInterrupt` aber nicht.

```python
try:
    risky()
except ___:
    return "gefangen"
```

`risky` ist irgendeine Funktion, die eine gewöhnliche Exception werfen kann.

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 3 Punkte

Welche Aussagen über Rekursion stimmen? Wähle alle zutreffenden Antworten.

- A) Jeder Aufruf hat eigene lokale Namen.
- B) Ein fehlender Basisfall endet mit `RecursionError`.
- C) Rekursion ist nur mit `yield` erlaubt.
- D) Der Basisfall darf `return` benutzen.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** A

**Erklärung:** `IndentationError` ist eine Unterklasse von `SyntaxError`. Das Programm startet nicht.

### Frage 2

**Antwort:** C

**Erklärung:** `if`, `None` und `for` sind Schlüsselwörter. `summe` nicht.

### Frage 3

**Antwort:** A, C

**Erklärung:** `bin` und `hex` liefern Text mit Präfix. Die Literale `0b1010` und `0xFF` sind `int`.

### Frage 4

**Antwort:** 255

**Erklärung:** Die Basis steht im zweiten Argument. `ff` hexadezimal ist 255.

### Frage 5

**Antwort:** C

**Erklärung:** `/` bindet nach links und liefert in Python 3 immer `float`. `(8 / 2) / 2` ist `2.0`.

### Frage 6

**Antwort:** `int`

**Erklärung:** `int` liest einen Ganzzahl-String. `input` selbst hätte nur Text geliefert.

### Frage 7

**Antwort:** A

**Erklärung:** `10 + 2` ist `12`, ganzzahlig durch `3` ist `4`, hoch `2` ist `16`.

### Frage 8

**Antwort:** B

**Erklärung:** Die Einrückung entscheidet. Dieses `else` steht auf der Höhe des äußeren `if`.

### Frage 9

**Antwort:** A, C, D

**Erklärung:** `"0"` ist ein nicht leerer String und damit wahr.

### Frage 10

**Antwort:** B

**Erklärung:** `9` liegt nicht in `range(2, 4)`. Es gibt kein `break`, also läuft `else`.

### Frage 11

**Antwort:** B, C, D, A

**Erklärung:** Ein Startwert wird überschrieben, wenn das `if` wahr ist. `print` steht dahinter. Mit `wert` gleich `15` ist das Ergebnis trotzdem `"ok"`. Die gefragte Zeilenfolge bleibt B, C, D, A.

### Frage 12

**Antwort:** B

**Erklärung:** `for` braucht eine Folge. Eine nackte Zahl ist keine. `range(3)` wäre die richtige Form.

### Frage 13

**Antwort:** A

**Erklärung:** `break` an dieser Stelle verlässt nur die innere `for`-Schleife.

### Frage 14

**Antwort:** A, C

**Erklärung:** `pass` ist kein Kommentar und keine Variable.

### Frage 15

**Antwort:** [1, 3, 5]

**Erklärung:** Start `1`, Stopp `6` ausgeschlossen, Schritt `2`.

### Frage 16

**Antwort:** B

**Erklärung:** `[:]` baut eine neue Liste mit denselben Elementen.

### Frage 17

**Antwort:** A, B, D

**Erklärung:** Listen sind veränderbar und deshalb nicht hashbar. Strings, Zahlen und Tupel aus hashbaren Werten schon.

### Frage 18

**Antwort:** 1–A, 2–B, 3–C, 4–D

**Erklärung:** `\\` ist ein Backslash. `\n` ist der Zeilenumbruch, auch in einem mehrzeiligen Literal. `"Ada's"` braucht dafür keine Escape-Sequenz.

### Frage 19

**Antwort:** `append`

**Erklärung:** `append` hängt ein Element an und gibt `None` zurück.

### Frage 20

**Antwort:** B

**Erklärung:** `in` antwortet mit einem Bool, nicht mit dem Index.

### Frage 21

**Antwort:** (20, 30)

**Erklärung:** Ein Slice eines Tupels ist ein Tupel. Index 0 fällt weg.

### Frage 22

**Antwort:** A, B, D

**Erklärung:** `find` wirft nicht. `len` wird um den String herum aufgerufen.

### Frage 23

**Antwort:** B

**Erklärung:** Ohne Klammern findet kein Aufruf statt. Der Name zeigt auf die Funktion.

### Frage 24

**Antwort:** A

**Erklärung:** Nur lesen findet das äußere `x`. Eine Zuweisung ohne `global` wäre lokal und bei `x = x + 1` sogar ein `UnboundLocalError`.

### Frage 25

**Antwort:** A, C, D

**Erklärung:** `+=` auf einer Zahl erzeugt lokal ein neues `int`. Der Default `0` bleibt für den nächsten Aufruf unverändert.

### Frage 26

**Antwort:** B, A

**Erklärung:** `KeyboardInterrupt` hängt direkt unter `BaseException`, nicht unter `Exception`. `Exception` gehört nicht in diese Kette.

### Frage 27

**Antwort:** IndexError

**Erklärung:** Der Index liegt außerhalb des Tupels. Das Nachschlagen scheitert, das Tupel wird nicht verändert.

### Frage 28

**Antwort:** B

**Erklärung:** Der erste passende Zweig gewinnt. `ValueError` ist eine `Exception`, also kommt es nie beim zweiten Zweig an.

### Frage 29

**Antwort:** `Exception`

**Erklärung:** `KeyboardInterrupt` erbt nicht von `Exception`. Ein nacktes `except` würde es mitfangen.

### Frage 30

**Antwort:** A, B, D

**Erklärung:** Rekursion braucht kein `yield`. Sie braucht einen Zweig, der nicht wieder aufruft.
