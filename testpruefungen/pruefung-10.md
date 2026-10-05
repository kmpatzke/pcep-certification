# Testprüfung 10

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

`alter = alter + 1` ist syntaktisch gültig, `alter` wurde vorher gebunden. Welche Ebene beschreibt, dass der Name danach auf ein neues Zahlenobjekt zeigt?

- A) Lexik
- B) Semantik
- C) nur der Kommentar
- D) die Prüfung zählt das als Compilerlauf

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Warum scheitert `yield = 1`?

- A) `yield` ist ein Schlüsselwort.
- B) Zuweisungen brauchen zwei Gleichheitszeichen.
- C) `yield` ist nur in Strings erlaubt, sonst ein `NameError`.
- D) PEP 8 verbietet die Ziffer `1`.

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `4 / 2` ist `2.0`.
- B) `4 / 2` ist der Integer `2`.
- C) `0.1 + 0.2 == 0.3` ist `False`.
- D) `//` und `/` sind derselbe Operator.

### Frage 4 · Lückentext · Block 1 · Ziel 1.4 · 3 Punkte

`~6` ergibt ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Potenzen binden nach rechts. Was gibt dieses Programm aus?

```python
basis = 2
print(basis ** 2 ** 3)
```

- A) `64`
- B) `256`
- C) `12`
- D) `128`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.5 · 3 Punkte

Ergänze so, dass zwischen `3` und `4` kein Zeichen steht. Der Zeilenumbruch am Ende bleibt der Standard.

```python
print(3, 4, ___="")
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Was ergibt `int(float("1.5"))`?

- A) `1.5`
- B) `1`
- C) `"1.5"`
- D) `ValueError`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
namen = []
if namen:
    status = "voll"
else:
    status = "leer"
```

Was steht in `status`?

- A) `"voll"`
- B) `"leer"`
- C) `[]`
- D) `None`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Werte lassen ein `if wert:` nicht in den Körper laufen? Wähle alle zutreffenden Antworten.

- A) `None`
- B) `{}`
- C) `[0]`
- D) `0.0`

### Frage 10 · Szenario · Block 2 · Ziel 2.1 · 4 Punkte

Dieselben Schwellen wie in einem Notenprogramm: ab `90` der Text `"A"`, sonst ab `80` der Text `"B"`, sonst `"C"`. Die erreichte Punktzahl ist `79`. Welcher Text entsteht?

- A) `"A"`
- B) `"B"`
- C) `"C"`
- D) `""`

### Frage 11 · Sortieren · Block 2 · Ziel 2.2 · 4 Punkte

Ordne die Wirkung von früh nach spät in diesem Fragment. Gib die Buchstaben an.

```python
text = ""
for zeichen in "abca":
    if zeichen == "a":
        continue
    text += zeichen
```

- A) `"b"` wird angehängt
- B) das erste `"a"` wird übersprungen
- C) `"c"` wird angehängt
- D) das letzte `"a"` wird übersprungen

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Wie viele Werte hat `range(1, 1)`?

- A) `1`
- B) `0`
- C) `2`
- D) der Aufruf wirft `ValueError`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile gehört an die Markierung, damit `status` zu `"fertig"` wird? Im Körper steht kein `break`.

```python
for n in range(2):
    n = n
___
    status = "fertig"
```

- A) `else:`
- B) `elif True:`
- C) `except:`
- D) `case:`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Aussagen über verschachtelte Schleifen stimmen? Wähle alle zutreffenden Antworten.

- A) Die innere Schleife läuft für jeden Schritt der äußeren neu an.
- B) `continue` in der inneren Schleife startet sofort den nächsten Schritt der äußeren.
- C) `break` in der inneren Schleife lässt die äußere in ihren nächsten Schritt gehen, wenn der innere Körper damit endet.
- D) Beide Schleifen müssen dieselbe Laufvariable benutzen.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

Welche drei Zahlen erzeugt `range`, wenn es bei 1 beginnt, vor 8 aufhört und in Dreierschritten geht? Schreibe sie als Python-Liste: ___.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

`werte = [1, 2]` und `werte.insert(1, 9)`. Was steht danach in `werte`?

- A) `[9, 1, 2]`
- B) `[1, 9, 2]`
- C) `[1, 2, 9]`
- D) `[1, 2]`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

Welche Ausdrücke haben den Typ `tuple`? Wähle alle zutreffenden Antworten.

- A) `(5,)`
- B) `(5)`
- C) `()`
- D) `(5, 6)[0:1]`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.4 · 4 Punkte

Ordne zu.

1. `"aba".count("a")`
2. `"ab".find("b")`
3. `"ab".replace("b", "c")`
4. `"ab".endswith("b")`

- A) `2`
- B) `1`
- C) `"ac"`
- D) `True`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze die Methode, die eine flache Kopie liefert. `werte[:]` wäre auch eine, hier ist der Methodenname gefragt.

```python
kopie = werte.___()
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.3 · 3 Punkte

`"Ada" in {"name": "Ada"}.values()` ergibt was?

- A) `False`
- B) `True`
- C) `"Ada"`
- D) `KeyError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.3 · 4 Punkte

`hex(255)` ergibt ___. Schreibe den String inklusive Präfix, so wie Python ihn liefert, in einfachen Anführungszeichen nicht nötig: die Zeichen `0xff`.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Welche Zugriffe werfen eine Ausnahme? Wähle alle zutreffenden Antworten.

- A) `"ab"[5]`
- B) `"ab"[1:50]`
- C) `"ab".index("z")`
- D) `"ab".find("z")`

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

Was ist der Unterschied zwischen `zaehle(3)` und `list(zaehle(3))`, wenn `zaehle` die Werte per `yield` liefert?

- A) Beides sind sofort Listen.
- B) Der erste Ausdruck ist ein Generator, der zweite eine Liste der gelieferten Werte.
- C) Beides ist `None`.
- D) `list(...)` löscht die Funktion.

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Zeile lässt `setzen` das äußere `stand` von `0` auf den Parameter ändern?

```python
stand = 0

def setzen(wert):
    ___
    stand = wert
```

- A) `global stand`
- B) `stand = global`
- C) `nonlocal wert`
- D) `return global`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
def haenge_an(wert, folge=[]):
    folge.append(wert)
    return folge
```

Dreimal hintereinander `haenge_an(1)`, `haenge_an(2)`, `haenge_an(3)`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der dritte Rückgabewert ist `[1, 2, 3]`.
- B) Jeder Aufruf gibt eine Liste der Länge `1` zurück.
- C) Alle drei Rückgabewerte sind dasselbe Listenobjekt.
- D) Der Default entsteht einmal, beim Anlegen der Funktion.

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Ordne die Klauseln so, dass `"a" + 1` im `TypeError`-Zweig landet. Gib die Buchstaben in Quelltext-Reihenfolge an.

- A) `except Exception:`
- B) `except TypeError:`
- C) `try:`

### Frage 27 · Lückentext · Block 4 · Ziel 4.1 · 4 Punkte

Eine Rekursion ohne Basisfall endet mit ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

`except ArithmeticError` steht über `except ZeroDivisionError`. Was passiert bei `1 / 0`?

- A) Der Zweig `ZeroDivisionError` läuft.
- B) Der Zweig `ArithmeticError` läuft, der speziellere Zweig ist unerreichbar.
- C) Beide Zweige laufen nacheinander.
- D) Es ist ein Syntaxfehler, Oberklassen zu fangen.

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze das Schlüsselwort, das eine Ausnahme auslöst, statt sie zu fangen.

```python
if n < 0:
    ___ ValueError("negativ")
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.4 · 3 Punkte

Welche Aussagen über `try` stimmen? Wähle alle zutreffenden Antworten.

- A) `else` an `try` läuft nur, wenn kein Fehler kam.
- B) `finally` läuft auch nach einem `return` im `try`, bevor die Funktion wirklich zurückkehrt.
- C) `finally` läuft nur, wenn ein `except` gefehlt hat.
- D) Mehrere `except` sind erlaubt.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** B

**Erklärung:** Was die Zuweisung bewirkt, ist Bedeutung. Die Bausteine und die Form sind damit schon in Ordnung.

### Frage 2

**Antwort:** A

**Erklärung:** `yield` ist reserviert. Es kann keine Variable heißen.

### Frage 3

**Antwort:** A, C

**Erklärung:** `/` liefert einen Float, auch wenn das Ergebnis ganzzahlig aussieht. `//` ist ein anderer Operator. Die Summe der beiden Floats trifft `0.3` nicht exakt.

### Frage 4

**Antwort:** -7

**Erklärung:** `~n` ist `-n - 1`. Für `6` ist das `-7`.

### Frage 5

**Antwort:** B

**Erklärung:** `**` bindet nach rechts. `2 ** (2 ** 3)` ist `2 ** 8`, also `256`. `print` zeigt genau diese Zahl.

### Frage 6

**Antwort:** `sep`

**Erklärung:** Ein leeres `sep` klebt die Argumente aneinander. `end` würde das Ende der Zeile ändern.

### Frage 7

**Antwort:** B

**Erklärung:** `float` liest `"1.5"`, `int` schneidet danach Richtung `0` auf `1`.

### Frage 8

**Antwort:** B

**Erklärung:** Eine leere Liste ist falsch. Der `else`-Zweig setzt `"leer"`.

### Frage 9

**Antwort:** A, B, D

**Erklärung:** `None`, das leere Dictionary und `0.0` sind falsch. `[0]` enthält ein Element und ist wahr.

### Frage 10

**Antwort:** C

**Erklärung:** `79` verfehlt `90` und `80`. Der `else`-Zweig setzt `"C"`.

### Frage 11

**Antwort:** B, A, C, D

**Erklärung:** Erst fällt das erste `"a"` weg, dann kommen `"b"` und `"c"`, dann fällt das letzte `"a"` weg.

### Frage 12

**Antwort:** B

**Erklärung:** Start und Stopp sind gleich. Bei positivem Schritt entsteht keine Zahl.

### Frage 13

**Antwort:** A

**Erklärung:** Ohne `break` läuft das Schleifen-`else`. `elif` und `except` gehören hier nicht hin. `case` ist keine PCEP-Anweisung dieses Blocks.

### Frage 14

**Antwort:** A, C

**Erklärung:** `continue` und `break` gelten für die Schleife, in der sie stehen. Die innere `break` beendet nicht die äußere Schleife. Die Laufvariablen dürfen verschieden sein.

### Frage 15

**Antwort:** [1, 4, 7]

**Erklärung:** Start `1`, Schritt `3`, Stopp `8` ausgeschlossen.

### Frage 16

**Antwort:** B

**Erklärung:** `insert(1, 9)` schiebt vor den alten Index `1`. `append` hätte ans Ende gehängt, `insert(0, 9)` an den Anfang.

### Frage 17

**Antwort:** A, C, D

**Erklärung:** `(5)` ist ein `int`. Das leere Tupel und der Slice `(5,)` sind Tupel. Das Komma in `(5,)` macht das einelementige Tupel.

### Frage 18

**Antwort:** 1–A, 2–B, 3–C, 4–D

**Erklärung:** Zwei Treffer für `"a"`, die Position `1` für `"b"`, der neue String `"ac"`, und `endswith` als Bool.

### Frage 19

**Antwort:** `copy`

**Erklärung:** `list.copy` ist flach, wie `[:]`. Innere Listen werden nicht tief kopiert.

### Frage 20

**Antwort:** B

**Erklärung:** `in` auf dem Dictionary träfe den Schlüssel nicht. `values()` enthält `"Ada"`.

### Frage 21

**Antwort:** 0xff

**Erklärung:** `hex` liefert einen String mit Präfix und kleinen Buchstaben, keine Zahl.

### Frage 22

**Antwort:** A, C

**Erklärung:** Ein Index außerhalb wirft `IndexError`. `index` wirft `ValueError`. Slice und `find` werfen in diesen beiden Fällen nicht.

### Frage 23

**Antwort:** B

**Erklärung:** Der Aufruf allein startet die Iteration nicht. `list` zieht alle `yield`-Werte heraus.

### Frage 24

**Antwort:** A

**Erklärung:** `global stand` muss so heißen. Die anderen drei Zeilen sind keine gültige Erklärung des Namens.

### Frage 25

**Antwort:** A, C, D

**Erklärung:** Dieselbe Default-Liste wächst über die drei Aufrufe. Darum sind die Rückgaben dasselbe Objekt, und die letzte enthält alle drei Zahlen.

### Frage 26

**Antwort:** C, B, A

**Erklärung:** `"a" + 1` ist ein `TypeError`. Der konkrete Zweig muss vor `Exception` stehen.

### Frage 27

**Antwort:** RecursionError

**Erklärung:** Jeder Aufruf legt einen weiteren Rahmen an, bis die Grenze erreicht ist. Das ist kein unendliches `while` im selben Rahmen.

### Frage 28

**Antwort:** B

**Erklärung:** `ZeroDivisionError` ist eine `ArithmeticError`. Der erste passende Zweig gewinnt.

### Frage 29

**Antwort:** `raise`

**Erklärung:** `raise` wirft. `except` würde an dieser Stelle nicht passen.

### Frage 30

**Antwort:** A, B, D

**Erklärung:** `finally` läuft unabhängig davon, ob ein `except` existiert. Es läuft auch, wenn der `try` mit `return` verlassen wird.
