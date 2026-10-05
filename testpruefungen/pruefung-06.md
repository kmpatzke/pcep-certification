# Testprüfung 06

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

Was gehört zur Lexik, nicht zur Syntax?

- A) die erlaubten Bausteine, zum Beispiel der Name `print` oder die Zahl `42`
- B) die Regel, dass eine geöffnete Klammer wieder geschlossen wird
- C) die Bedeutung der Division durch null
- D) die Einrückung eines Blocks

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

```python
x = 1  # x = 99
print(x)
```

Was wird ausgegeben?

- A) `99`
- B) `1`
- C) nichts, weil `#` die ganze Datei abschaltet
- D) `x = 99`

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welche Ausdrücke ergeben `True`? Wähle alle zutreffenden Antworten.

- A) `1 < 2 < 3`
- B) `3 < 2 < 1`
- C) `(3 < 2) < 1`
- D) `not 0`

### Frage 4 · Lückentext · Block 1 · Ziel 1.4 · 3 Punkte

`5 << 1` ergibt ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Was passiert bei `"ab" + 3`?

- A) `"ab3"`
- B) `"ababab"`
- C) `TypeError`
- D) `"ab ab ab"`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.4 · 3 Punkte

Ergänze den unären Operator, der aus `5` den Wert `-6` macht.

```python
wert = ___5
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.5 · 3 Punkte

Was gibt `print(1, 2, "-")` aus?

- A) `1-2`
- B) `1 2 -`
- C) `1 2-`
- D) einen `TypeError`, weil drei Argumente verboten sind

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
def bewertung(note):
    if note == 1:
        return "sehr gut"
    elif note == 2:
        return "gut"
    else:
        return "andere"
```

Was liefert `bewertung(4)`?

- A) `"sehr gut"`
- B) `"gut"`
- C) `"andere"`
- D) `None`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Folgen beschreibt `range` richtig? Wähle alle zutreffenden Antworten.

- A) `range(3)` enthält `0`, `1` und `2`.
- B) `range(3)` enthält `3`.
- C) `range(1, 4)` enthält `1`, `2` und `3`.
- D) `range(5, 1, -1)` enthält `1`.

### Frage 10 · Szenario · Block 2 · Ziel 2.1 · 4 Punkte

Ein Programm prüft das Alter. Unter 18 liefert es `"nein"`. Ab 18 und mit Karte `"ja"`, ab 18 ohne Karte `"ausweis_fehlt"`. Die Person ist 17 und hat eine Karte. Welcher Text entsteht?

- A) `"ja"`
- B) `"ausweis_fehlt"`
- C) `"nein"`
- D) `"ja"` und `"nein"` gleichzeitig

### Frage 11 · Sortieren · Block 2 · Ziel 2.2 · 4 Punkte

Ordne die Ereignisse beim ersten Durchlauf von `for zeichen in "ab":`, wenn der Körper das Zeichen an einen String hängt. Gib die Buchstaben an.

- A) der Körper hängt `"a"` an
- B) die Schleife ist fertig und es geht nach dem Block weiter
- C) das erste Element `"a"` wird gebunden
- D) das zweite Element `"b"` wird gebunden

Gemeint ist die Reihenfolge des ersten Bindens, des ersten Körpers, des zweiten Bindens. Das Weitergehen nach der Schleife steht am Schluss. Der zweite Körper ist hier kein eigener Buchstabe.

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt dieser Ablauf?

```python
text = ""
for zeichen in "ab":
    text += zeichen + zeichen
```

- A) `"ab"`
- B) `"aabb"`
- C) `"abab"`
- D) `"aann"`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Bedingung lässt die `while`-Schleife die Summe `10` für `n = 4` bilden, wenn der Körper `summe += n` und `n -= 1` enthält und `summe` bei `0` startet?

```python
while ___:
    summe += n
    n -= 1
```

- A) `n > 0`
- B) `n >= 0`
- C) `n < 0`
- D) `False`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

`for` und `while` dürfen `else` tragen. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Das `else` läuft auch, wenn der Körper nie betreten wurde und kein `break` kam.
- B) Das `else` läuft zusätzlich, wenn `break` kam.
- C) `while-else` und `for-else` folgen derselben `break`-Regel.
- D) `else` an einer Schleife ist dasselbe wie `else` an `if`.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

`list(range(5, 1, -1))` hat ___ Elemente.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Was gibt `werte.append(1)` zurück, nachdem `werte = [0]` war?

- A) `[0, 1]`
- B) `None`
- C) `1`
- D) `[1]`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

`t = ([1],)`. Welche Aussagen stimmen nach `t[0].append(2)`? Wähle alle zutreffenden Antworten.

- A) `t` ist `([1, 2],)`.
- B) Die Länge von `t` wird `2`.
- C) Die innere Liste wurde verändert.
- D) `t[0] = [1, 2]` wäre ebenfalls ohne Fehler möglich gewesen.

### Frage 18 · Zuordnen · Block 3 · Ziel 3.3 · 4 Punkte

`buch = {"b": 2, "a": 1}`. Ordne zu.

1. `sorted(buch.keys())`
2. `list(buch.values())`
3. `list(buch.items())`
4. `"a" in buch`

- A) `["a", "b"]`
- B) `[2, 1]`
- C) `[("b", 2), ("a", 1)]`
- D) `True`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze den Aufruf, der eine Matrix aus drei getrennten Zeilen `[0, 0]` baut.

```python
matrix = [[0, 0] for _ in ___(3)]
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.4 · 3 Punkte

`"12".isdigit()` und `"ab".isalpha()` ergeben zusammen welches Paar?

- A) `(False, False)`
- B) `(True, False)`
- C) `(True, True)`
- D) `(False, True)`

### Frage 21 · Lückentext · Block 3 · Ziel 3.4 · 4 Punkte

`",".join(["a", "b"])` ergibt ___. Schreibe den String mit den Anführungszeichen, die ein Python-Literal braucht, also so: `"a,b"`.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Aussagen über `sorted` und `sort` stimmen? Wähle alle zutreffenden Antworten.

- A) `sorted([3, 1, 2])` ist `[1, 2, 3]`.
- B) Die Quelle bleibt bei `sorted` unverändert.
- C) `[3, 1, 2].sort()` gibt `[1, 2, 3]` zurück.
- D) `sort` ändert die Liste an Ort und Stelle.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

```python
def nichts():
    return

nichts() is None
```

Welchen Wert hat der Vergleich?

- A) `False`
- B) `True`
- C) `None`
- D) der Vergleich ist ein Syntaxfehler

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Zeile setzt das Modul-`stand` auf `5`? `stand` wurde auf Modul-Ebene mit `0` angelegt.

```python
def setzen(wert):
    ___
    stand = wert
```

- A) `global stand`
- B) `stand = 0`
- C) `nonlocal stand`
- D) `return stand`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.4 · 4 Punkte

`innen` führt `1 / b` aus und hat kein `try`. `aussen` ruft `innen` in einem `try` auf und gibt bei `ZeroDivisionError` den Wert `None` zurück, sonst das Ergebnis. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `aussen(0)` ist `None`.
- B) `aussen(2)` ist `0.5`.
- C) `innen` muss den Fehler selbst fangen, sonst kommt er nie bei `aussen` an.
- D) Die Verantwortung liegt hier bei `aussen`.

### Frage 26 · Sortieren · Block 4 · Ziel 4.3 · 3 Punkte

Ordne die Namen so, wie ein `except` sie prüfen sollte, damit ein `ZeroDivisionError` im eigenen Zweig landet und nicht schon von der Oberklasse geschluckt wird. Der `try` steht zuerst. Gib die Buchstaben an.

- A) `except ArithmeticError`
- B) `except ZeroDivisionError`
- C) `try`

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`(1, 2)[0] = 9` wirft ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.1 · 3 Punkte

Was sammelt `list(zaehle(3))`, wenn `zaehle` mit `yield` die Werte `0`, `1` und `2` liefert?

- A) `[]`
- B) `[0, 1, 2]`
- C) `3`
- D) `None`

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.2 · 4 Punkte

Ergänze den Identitätsoperator. `folge` hat den Default `None`, und genau dieses Objekt soll erkannt werden.

```python
if folge ___ None:
    folge = []
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Welche Fehler fängt `except ArithmeticError`? Wähle alle zutreffenden Antworten.

- A) `ZeroDivisionError`
- B) `IndexError`
- C) `KeyError`
- D) eine selbst geworfene `ArithmeticError`, falls jemand sie direkt erzeugt

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** A

**Erklärung:** Lexik sind die Bausteine. Klammern und Einrückung sind Form, Division durch null ist Bedeutung.

### Frage 2

**Antwort:** B

**Erklärung:** Ab `#` ist der Rest der Zeile inaktiv. Die Zuweisung `x = 1` bleibt gültig.

### Frage 3

**Antwort:** A, C, D

**Erklärung:** Die Kette `3 < 2 < 1` ist falsch. `(3 < 2) < 1` ist `False < 1` und damit wahr. `not 0` ist wahr.

### Frage 4

**Antwort:** 10

**Erklärung:** Eine Stelle nach links schieben verdoppelt die nichtnegative Zahl. `5` wird `10`.

### Frage 5

**Antwort:** C

**Erklärung:** `+` verbindet String nur mit String. Die Zahl hat den falschen Typ.

### Frage 6

**Antwort:** `~`

**Erklärung:** `~5` ist `-5 - 1`, also `-6`.

### Frage 7

**Antwort:** B

**Erklärung:** Das dritte Argument ist positional und wird mit dem Standard-`sep` ausgegeben. `sep` müsste benannt sein.

### Frage 8

**Antwort:** C

**Erklärung:** `4` trifft keinen der beiden Vergleiche. Der `else`-Zweig läuft.

### Frage 9

**Antwort:** A, C

**Erklärung:** `range(3)` endet vor `3`. `range(5, 1, -1)` endet vor `1`, enthält also `5, 4, 3, 2`.

### Frage 10

**Antwort:** C

**Erklärung:** Das äußere Kriterium Alter scheitert. Die Karte wird nicht mehr gefragt.

### Frage 11

**Antwort:** C, A, D, B

**Erklärung:** Zuerst `"a"`, dann der Körper, dann `"b"`. Danach ist die Folge zu Ende.

### Frage 12

**Antwort:** B

**Erklärung:** Jedes Zeichen wird zweimal angehängt: `aa` und danach `bb`.

### Frage 13

**Antwort:** A

**Erklärung:** Bei `n >= 0` würde nach der `0` noch einmal addiert. `n > 0` nimmt `4, 3, 2, 1`.

### Frage 14

**Antwort:** A, C

**Erklärung:** Schleifen-`else` hängt am Ausbleiben von `break`, nicht an der `if`-Logik. Ein leerer Lauf ohne `break` führt das `else` trotzdem aus.

### Frage 15

**Antwort:** 4

**Erklärung:** Die Werte sind `5, 4, 3, 2`.

### Frage 16

**Antwort:** B

**Erklärung:** `append` verändert die Liste und liefert `None`. Wer den Rückgabewert zuweist, verliert die Liste.

### Frage 17

**Antwort:** A, C

**Erklärung:** Verändert wird die Liste im Tupel, nicht die Länge des Tupels. Eine Zuweisung an `t[0]` bleibt `TypeError`.

### Frage 18

**Antwort:** 1–A, 2–B, 3–C, 4–D

**Erklärung:** `sorted` sortiert die Schlüssel. `values` und `items` folgen der Einfügereihenfolge. `in` trifft `"a"`.

### Frage 19

**Antwort:** `range`

**Erklärung:** Drei Durchläufe von `range(3)` bauen drei neue Zeilen. `[[0, 0]] * 3` würde dieselbe Zeile dreimal verwenden.

### Frage 20

**Antwort:** C

**Erklärung:** `"12"` besteht aus Ziffern, `"ab"` aus Buchstaben.

### Frage 21

**Antwort:** "a,b"

**Erklärung:** `join` setzt das Trennzeichen zwischen die Teile, nicht dahinter.

### Frage 22

**Antwort:** A, B, D

**Erklärung:** `sort` gibt `None` zurück. Die sortierte Liste liegt danach im Objekt selbst.

### Frage 23

**Antwort:** B

**Erklärung:** `return` ohne Ausdruck ergibt `None`. `is None` ist dann wahr.

### Frage 24

**Antwort:** A

**Erklärung:** Ohne `global` würde `stand = wert` eine lokale Variable anlegen.

### Frage 25

**Antwort:** A, B, D

**Erklärung:** Ein nicht gefangener Fehler läuft aus `innen` hinaus. Genau dort übernimmt `aussen` ihn. `1 / 2` ist `0.5`.

### Frage 26

**Antwort:** C, B, A

**Erklärung:** Zuerst der `try`. Die Unterklasse muss vor `ArithmeticError` stehen.

### Frage 27

**Antwort:** TypeError

**Erklärung:** Item-Zuweisung ändert das Tupel. Das ist kein `IndexError`, der Index `0` existiert.

### Frage 28

**Antwort:** B

**Erklärung:** `list` zieht den Generator leer und sammelt jeden `yield`-Wert.

### Frage 29

**Antwort:** `is`

**Erklärung:** `is` prüft, ob es dasselbe Objekt `None` ist. Das ist die Form aus dem Kapitel über Standardwerte.

### Frage 30

**Antwort:** A, D

**Erklärung:** `ArithmeticError` ist die Oberklasse der Rechenfehler, nicht der Nachschlagefehler. Wer sie direkt wirft, wird von diesem `except` gefangen.
