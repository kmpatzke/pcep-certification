# Testprüfung 02

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

`print(1 / 0)` steht in einer sonst gültigen Datei. Welche Einordnung passt?

- A) Lexikfehler, weil `/` kein erlaubtes Zeichen ist.
- B) Syntaxfehler, weil die Null nicht in Klammern steht.
- C) Die Form ist gültig, die Bedeutung scheitert zur Laufzeit.
- D) PEP-8-Verstoß, das Programm läuft mit Warnung weiter.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Was bewirkt `#` in einer Zeile?

- A) Der Rest der Zeile wird ignoriert.
- B) Die nächsten zwei Zeilen werden ignoriert.
- C) Die Zeile wird zum Docstring.
- D) Der Interpreter führt die Zeile zweimal aus.

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

Welche Namen sind als Variable syntaktisch verboten? Wähle alle zutreffenden Antworten.

- A) `summe`
- B) `for`
- C) `2wert`
- D) `_zahl`

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

`0b1010` hat den Dezimalwert ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `-7 // 2`?

- A) `-3`
- B) `-3.5`
- C) `-4`
- D) `3`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.5 · 3 Punkte

Ergänze den Parameternamen, damit die Ausgabe `1-2` ist und danach der normale Zeilenumbruch kommt.

```python
print(1, 2, ___="-")
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Warum ist `0.1 + 0.2 == 0.3` in Python falsch?

- A) `==` vergleicht nur Strings.
- B) `float` kann viele Dezimalbrüche nicht exakt speichern.
- C) `+` hängt bei Floats Text an.
- D) Der Vergleich ist ein Syntaxfehler.

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
note = 1
if note == 1:
    text = "sehr gut"
elif note == 2:
    text = "gut"
else:
    text = "andere"
```

Was steht in `text`?

- A) `"gut"`
- B) `"andere"`
- C) `"sehr gut"`
- D) `None`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Schleifen enden? Wähle alle zutreffenden Antworten.

- A) `n = 2` und `while n > 0:` mit `n -= 1` im Körper
- B) `while True:` mit `pass` als einzigem Körper
- C) `for i in range(3):`
- D) `for zeichen in "ab":`

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

Ein Zähler sucht die erste `4` in `range(2, 6)`. Er addiert jede besuchte Zahl auf `summe` und bricht bei `4` ab, bevor er sie addiert. `else` der Schleife setzt `summe` auf `-1`, falls kein `break` kam. Welchen Wert hat `summe` am Ende?

- A) `-1`
- B) `2`
- C) `5`
- D) `9`

### Frage 11 · Sortieren · Block 2 · Ziel 2.2 · 4 Punkte

Ordne die Ereignisse nach dem Zeitpunkt ihres ersten Auftretens. Gib die Buchstaben in dieser Reihenfolge an.

```python
n = 0
while n < 2:
    n += 1
print(n)
```

- A) `print` läuft
- B) `n` wird auf `0` gesetzt
- C) die Bedingung `n < 2` wird zum ersten Mal geprüft und ist wahr
- D) `n += 1` läuft zum ersten Mal

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt `list(range(5, 1, -1))`?

- A) `[5, 4, 3, 2, 1]`
- B) `[5, 4, 3, 2]`
- C) `[4, 3, 2, 1]`
- D) `[]`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile überspringt nur die ungeraden Werte und lässt die Summe der geraden Werte `6` entstehen (`4 + 2`, Start `n = 5`, `n` wird am Anfang jedes Durchlaufs um 1 kleiner)?

```python
n = 5
summe = 0
while True:
    n -= 1
    if n == 0:
        break
    ___
    summe += n
```

- A) `if n % 2 != 0: continue`
- B) `if n % 2 == 0: break`
- C) `if n % 2 != 0: break`
- D) `pass`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was stimmt über `continue`? Wähle alle zutreffenden Antworten.

- A) Der Rest dieses Durchlaufs wird übersprungen.
- B) Alle umgebenden Schleifen enden sofort.
- C) Die Schleife prüft danach die nächste Runde.
- D) `continue` ist ein Kommentar.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

Das Schlüsselwort, das einen syntaktisch nötigen Block füllt und dabei keinen Wert ändert, heißt ___.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Was ergibt `[10, 20, 30, 40][1:3]`?

- A) `[10, 20]`
- B) `[20, 30]`
- C) `[20, 30, 40]`
- D) `[30, 40]`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

`huelle = ([1], 3)`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `huelle[0].append(9)` ist erlaubt.
- B) `huelle[1] = 4` ist erlaubt.
- C) Das Tupel selbst bekommt keine neue Länge durch `append` an der inneren Liste.
- D) `huelle[0]` bleibt eine Liste.

### Frage 18 · Zuordnen · Block 3 · Ziel 3.1 · 4 Punkte

Ordne den Ausdruck dem Ergebnis zu. Startliste jeweils `[1, 2]`, außer wo der Ausdruck selbst die Liste baut.

1. `[1, 2].index(2)`
2. `len([1, 2, 2])`
3. `2 in [1, 2]`
4. `[0] * 3`

- A) `True`
- B) `1`
- C) `3`
- D) `[0, 0, 0]`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze die Methode, die `9` an Index `0` einfügt.

```python
werte = [1, 2]
werte.___(0, 9)
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Was passiert bei `text = "ab"` und danach `text[0] = "z"`?

- A) `text` wird `"zb"`.
- B) `TypeError`
- C) `text` wird `"z"`.
- D) `IndexError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.3 · 4 Punkte

Nach `buch = {"a": 1, "a": 2}` hat `buch["a"]` den Wert ___.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Welche Ausdrücke ergeben `"ab"`? Wähle alle zutreffenden Antworten.

- A) `"a" + "b"`
- B) `"a" * "b"`
- C) `"ab" * 1`
- D) `"  ab ".strip()`

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.2 · 4 Punkte

Welcher Aufruf ist ein Syntaxfehler?

- A) `addiere(1, 2)` bei `def addiere(a, b)`
- B) `addiere(b=2, a=1)`
- C) `addiere(1, b=2)`
- D) `addiere(a=1, 2)`

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Zeile sorgt dafür, dass die Zuweisung das `x` auf Modul-Ebene trifft?

```python
x = 1

def setzen():
    ___
    x = 4
```

- A) `global x`
- B) `nonlocal x`
- C) `x = global`
- D) `return x`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
def haenge_an(wert, folge=[]):
    folge.append(wert)
    return folge
```

Es wird zweimal aufgerufen: zuerst `haenge_an(1)`, dann `haenge_an(2)`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der zweite Aufruf sieht die Liste, die der erste schon gefüllt hat.
- B) Jeder Aufruf bekommt garantiert eine neue Liste, weil der Default in der Signatur steht.
- C) Der Default wird beim Definieren der Funktion erzeugt, nicht bei jedem Aufruf neu.
- D) Der zweite Rückgabewert ist `[1, 2]`.

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Ein `try` wirft `ValueError`. Die Zweige stehen in dieser Absicht, der erste passende gewinnt. Welche Reihenfolge prüft zuerst den konkreten Typ und erst danach die Oberklasse? Gib die Buchstaben an.

- A) `except Exception`
- B) `except ValueError`
- C) Körper von `try`

Die gesuchte Ausführungsreihenfolge ist: zuerst der Körper, dann der konkrete Zweig, dann käme die Oberklasse nur bei einem anderen Fehler dran. Ordne so, wie der Interpreter die Klauseln ansehen muss, damit `ValueError` nicht von `Exception` geschluckt wird: Körper, dann `ValueError`, dann `Exception`.

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`"a" + 1` wirft ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.1 · 3 Punkte

```python
def zaehle(n):
    i = 0
    while i < n:
        yield i
        i += 1

wert = zaehle(3)
```

Was ist `wert` unmittelbar nach dieser Zuweisung, bevor jemand darüber iteriert?

- A) die Liste `[0, 1, 2]`
- B) ein Generator-Objekt
- C) `None`
- D) die Zahl `3`

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze so, dass ein negativer `n` nicht zurückgegeben, sondern als `ValueError` gemeldet wird.

```python
def pruefe(n):
    if n < 0:
        ___ ValueError("negativ")
    return n
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Welche Typen fängt `except LookupError`? Wähle alle zutreffenden Antworten.

- A) `IndexError`
- B) `KeyError`
- C) `TypeError`
- D) `ZeroDivisionError`

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** C

**Erklärung:** Die Division ist syntaktisch gültig und wirft zur Laufzeit `ZeroDivisionError`.

### Frage 2

**Antwort:** A

**Erklärung:** Ein Kommentar gilt bis zum Ende derselben Zeile.

### Frage 3

**Antwort:** B, C

**Erklärung:** `for` ist ein Schlüsselwort. Ein Name darf nicht mit einer Ziffer beginnen.

### Frage 4

**Antwort:** 10

**Erklärung:** `1010` im Zweiersystem ist acht plus zwei.

### Frage 5

**Antwort:** C

**Erklärung:** `//` rundet in Richtung minus unendlich. `-4 * 2` liegt unter `-7`, der Rest wird `1`.

### Frage 6

**Antwort:** `sep`

**Erklärung:** `sep` steht zwischen den Argumenten. `end` stünde danach.

### Frage 7

**Antwort:** B

**Erklärung:** Binäre Gleitkommazahlen treffen `0.1` und `0.2` nicht exakt.

### Frage 8

**Antwort:** C

**Erklärung:** Der erste wahre Zweig gewinnt. `elif` und `else` laufen nicht mehr.

### Frage 9

**Antwort:** A, C, D

**Erklärung:** `while True` mit nur `pass` ändert die Bedingung nie.

### Frage 10

**Antwort:** C

**Erklärung:** Besucht und addiert wird nur `2` und `3`. Bei `4` kommt `break`, deshalb läuft `else` nicht. `2 + 3` ist `5`.

### Frage 11

**Antwort:** B, C, D, A

**Erklärung:** Zuerst die Zuweisung, dann die erste wahre Prüfung, dann der erste Schleifenkörper. `print` kommt erst, wenn die Schleife fertig ist.

### Frage 12

**Antwort:** B

**Erklärung:** Stopp `1` gehört nicht zur Folge. Schritt `-1`.

### Frage 13

**Antwort:** A

**Erklärung:** Ungerade Werte werden übersprungen, gerade addiert: `4` und `2`.

### Frage 14

**Antwort:** A, C

**Erklärung:** `continue` gilt nur für die innerste Schleife und nur für den aktuellen Durchlauf.

### Frage 15

**Antwort:** pass

**Erklärung:** `pass` ist die leere Anweisung. Sie erfüllt die Syntax und ändert keine Daten.

### Frage 16

**Antwort:** B

**Erklärung:** Index 1 inklusive, Index 3 exklusiv.

### Frage 17

**Antwort:** A, C, D

**Erklärung:** Die innere Liste bleibt veränderbar. Eine Zuweisung an `huelle[1]` würde das Tupel selbst ändern und ist verboten.

### Frage 18

**Antwort:** 1–B, 2–C, 3–A, 4–D

**Erklärung:** `index` findet die `2` an Position `1`. Drei Elemente, Mitgliedschaft, und `[0] * 3` wiederholt die Zahl.

### Frage 19

**Antwort:** `insert`

**Erklärung:** `insert(index, wert)` schiebt an dieser Stelle ein. `append` hängt nur an.

### Frage 20

**Antwort:** B

**Erklärung:** Strings sind unveränderbar. Item-Zuweisung wirft `TypeError`.

### Frage 21

**Antwort:** 2

**Erklärung:** Derselbe Schlüssel wird ersetzt, nicht doppelt gespeichert.

### Frage 22

**Antwort:** A, C, D

**Erklärung:** Zwei Strings kann man nicht multiplizieren. `strip` entfernt das umgebende Leerzeichen.

### Frage 23

**Antwort:** D

**Erklärung:** Ein positionales Argument darf nicht hinter einem Schlüsselwortargument stehen.

### Frage 24

**Antwort:** A

**Erklärung:** `global x` meint das Modul-`x`. Ohne diese Zeile wäre `x = 4` lokal.

### Frage 25

**Antwort:** A, C, D

**Erklärung:** Die Default-Liste entsteht einmal. Der zweite Aufruf hängt an dieselbe Liste an.

### Frage 26

**Antwort:** C, B, A

**Erklärung:** Zuerst läuft `try`. Die konkrete Klasse muss vor `Exception` stehen, sonst ist sie unerreichbar.

### Frage 27

**Antwort:** TypeError

**Erklärung:** String und Zahl lassen sich mit `+` nicht verbinden. Der Typ passt nicht.

### Frage 28

**Antwort:** B

**Erklärung:** Der Aufruf startet den Körper nicht bis zum Ende. Er liefert den Generator.

### Frage 29

**Antwort:** `raise`

**Erklärung:** `raise ValueError(...)` wirft die Ausnahme absichtlich.

### Frage 30

**Antwort:** A, B

**Erklärung:** `IndexError` und `KeyError` liegen unter `LookupError`. `TypeError` und `ZeroDivisionError` nicht.
