# Testprüfung 08

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

CPython erzeugt intern Bytecode. Was gilt für die Prüfungsfrage „Interpreter oder Compiler“?

- A) Die Antwort wird dadurch „Compiler“.
- B) Die Syllabus-Einordnung bleibt Interpreter.
- C) Bytecode ist ein Kommentar.
- D) Python hat weder Interpreter noch Compiler.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Welches Token ist das boolesche Literal für „falsch“?

- A) `false`
- B) `"False"`
- C) `False`
- D) `0`

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welche Ausdrücke ergeben den Integer `2`? Wähle alle zutreffenden Antworten.

- A) `True + True`
- B) `5 & 3`
- C) `6 & 3`
- D) `4 // 2`

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

Rechne das Oktalliteral `0o10` ins Zehnersystem um. Die Zahl ist ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `6 ^ 3`?

- A) `5`
- B) `6`
- C) `2`
- D) `9`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.4 · 3 Punkte

Ergänze die Umwandlung, die aus der Zahl `20` den Text `"20"` macht.

```python
text = ___(20)
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welchen Wert hat `16 >> 2`?

- A) `8`
- B) `4`
- C) `14`
- D) `32`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

Die Schwellen stehen in dieser Reihenfolge: `if punkte >= 90` ergibt `"A"`, `elif punkte >= 80` ergibt `"B"`, sonst `"C"`. Die Punktzahl ist genau `90`. Welcher Buchstabe entsteht?

- A) `"A"`
- B) `"B"`
- C) `"C"`
- D) `"AB"`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

`True or False and False`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der ganze Ausdruck ist `True`.
- B) `and` wird vor `or` gerechnet.
- C) `or` wird vor `and` gerechnet.
- D) `False and False` ist der innere Teil.

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

Äußere Schleife `a` in `range(3)`, innere `b` in `range(3)`. Sobald `b == 0` falsch wird, also ab `b == 1`, bricht nur die innere Schleife ab. Vorher wird ein Zähler um 1 erhöht. Wie oft wird erhöht?

- A) `1`
- B) `3`
- C) `6`
- D) `9`

### Frage 11 · Sortieren · Block 2 · Ziel 2.1 · 4 Punkte

`note` ist `2`. Ordne, was dieses Programm wirklich ausführt, von früh nach spät. Gib die Buchstaben an.

```python
if note == 1:
    text = "sehr gut"
elif note == 2:
    text = "gut"
else:
    text = "andere"
```

- A) der Vergleich `note == 2`
- B) die Zuweisung `"gut"`
- C) der Vergleich `note == 1`
- D) die Zuweisung `"andere"`

Lass den Zweig weg, der nicht läuft.

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

```python
n = 3
summe = 0
while n > 0:
    summe += n
    n -= 1
```

Was steht in `summe`?

- A) `3`
- B) `6`
- C) `0`
- D) die Schleife endet nicht

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Der `if`-Zweig soll absichtlich leer bleiben und gültig sein.

```python
if False:
    ___
```

- A) `pass`
- B) `continue`
- C) `break`
- D) `#`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Eine `for`-Schleife führt im ersten Durchlauf `break` aus. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der Rest der Folge wird nicht besucht.
- B) Das `else` der Schleife läuft.
- C) Das `else` der Schleife läuft nicht.
- D) `break` gilt auch für eine Schleife, die außen herum steht, ohne dass dort ein eigenes `break` steht.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

Nach der Schleife, die jede ungerade Zahl in `range(4)` mit `continue` überspringt und gerade Zahlen als Text anhängt, steht in `s` der Wert ___. `s` startet als `""`. `range(4)` ist `0, 1, 2, 3`.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Was ergibt `[1, 2, 2, 3].count(2)`?

- A) `1`
- B) `2`
- C) `4`
- D) `IndexError`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

`werte = [1]`. Welche Aufrufe lassen am Ende `[1, 2, 3]` entstehen? Wähle alle zutreffenden Antworten.

- A) `werte.append([2, 3])`
- B) `werte.extend([2, 3])`
- C) `werte += [2, 3]`
- D) `werte.insert(0, [2, 3])`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.3 · 4 Punkte

`person = {"name": "Ada"}` und danach `person["jahr"] = 1815`. Ordne zu.

1. `person["name"]`
2. `len(person)`
3. `"jahr" in person`
4. `list(person.keys())`

- A) `2`
- B) `"Ada"`
- C) `True`
- D) `["name", "jahr"]`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.4 · 4 Punkte

Ergänze die Methode, die `"ab"` zu `"AB"` macht.

```python
gross = "ab".___()
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Was ergibt `"zaun"[-1]`?

- A) `"z"`
- B) `"n"`
- C) `"u"`
- D) `IndexError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.2 · 4 Punkte

`(1,) + (2,)` ergibt ___. Schreibe das Tupel-Literal.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Ausdrücke sind wahr? Wähle alle zutreffenden Antworten.

- A) `40 not in [10, 20, 30]`
- B) `20 not in [10, 20, 30]`
- C) `"a" in "ab"`
- D) `"z" in "ab"`

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

`summe_bis` gibt bei `n <= 0` den Wert `0` zurück, sonst `n + summe_bis(n - 1)`. Was liefert `summe_bis(1)`?

- A) `0`
- B) `1`
- C) `2`
- D) `None`

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.4 · 3 Punkte

Welche Zeile im `except` macht aus dem Fehler einen normalen Rückgabewert `None`?

```python
def sicher(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        ___
```

- A) `return None`
- B) `raise`
- C) `return 0`
- D) `return a / b`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

Welche Aufrufe von `def gruss(name, zeichen="!"): return "Hallo " + name + zeichen` ergeben `"Hallo Ada!"`? Wähle alle zutreffenden Antworten.

- A) `gruss("Ada")`
- B) `gruss("Ada", "!")`
- C) `gruss(zeichen="!", name="Ada")`
- D) `gruss("Ada", "?")`

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Ordne die Klauseln so, dass ein `KeyError` im eigenen Zweig landet. Gib die Buchstaben in Quelltext-Reihenfolge an.

- A) `except LookupError:`
- B) `except KeyError:`
- C) `try:`

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

Die abstrakte Oberklasse von `KeyError` im Syllabus heißt ___.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

`innen` führt `1 / 0` aus und fängt nichts. `mitte` ruft `innen` und fängt nichts. `aussen` ruft `mitte` und fängt `ZeroDivisionError`. Wo wird der Fehler behandelt?

- A) in `innen`
- B) in `mitte`
- C) in `aussen`
- D) nirgends, weil zwei Funktionen dazwischen liegen

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze den Typ für einen Index außerhalb von `"ab"`.

```python
try:
    "ab"[5]
except ___:
    return "daneben"
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 3 Punkte

`g = zaehle(3)` und niemand iteriert über `g`. `zaehle` enthält `yield`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `g` ist ein Generator.
- B) Die Werte wurden schon alle berechnet und in einer Liste gespeichert.
- C) `list(g)` würde danach `[0, 1, 2]` liefern, wenn `zaehle` diese Werte yielded.
- D) Der Aufruf `zaehle(3)` ist ein Syntaxfehler, sobald `yield` im Körper steht.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** B

**Erklärung:** Bytecode ist ein Implementierungsdetail. Die Prüfung stellt Python weiter dem Interpreter gegenüber.

### Frage 2

**Antwort:** C

**Erklärung:** Das Literal schreibt man `False`. Klein geschrieben ist es ein gewöhnlicher Name. `"False"` ist Text, `0` eine Zahl.

### Frage 3

**Antwort:** A, C, D

**Erklärung:** `True + True` ist `2`. `6 & 3` ist `2`. `4 // 2` ist `2`. `5 & 3` ist `1`.

### Frage 4

**Antwort:** 8

**Erklärung:** Oktal `10` ist eine Acht.

### Frage 5

**Antwort:** A

**Erklärung:** `6` ist binär `110`, `3` ist `011`. Exklusives Oder ergibt `101`, also `5`.

### Frage 6

**Antwort:** `str`

**Erklärung:** `str(20)` ist der Text `"20"`.

### Frage 7

**Antwort:** B

**Erklärung:** Zwei Stellen nach rechts: `16` wird `8`, dann `4`.

### Frage 8

**Antwort:** A

**Erklärung:** `90 >= 90` ist wahr. Der erste Zweig gewinnt.

### Frage 9

**Antwort:** A, B, D

**Erklärung:** `and` bindet enger. `False and False` ist `False`, und `True or False` bleibt `True`.

### Frage 10

**Antwort:** B

**Erklärung:** Für jedes der drei `a` läuft nur `b == 0`. Das sind drei Erhöhungen.

### Frage 11

**Antwort:** C, A, B

**Erklärung:** Zuerst scheitert `note == 1`, dann trifft `note == 2`, dann die Zuweisung `"gut"`. Der `else`-Zweig läuft nicht.

### Frage 12

**Antwort:** B

**Erklärung:** Addiert werden `3`, `2` und `1`.

### Frage 13

**Antwort:** A

**Erklärung:** Ein leerer Block ist ein Syntaxfehler. `pass` ist die leere Anweisung. `#` allein lässt den Block leer.

### Frage 14

**Antwort:** A, C

**Erklärung:** `break` überspringt das `else` derselben Schleife und gilt nicht für eine äußere Schleife.

### Frage 15

**Antwort:** 02

**Erklärung:** `0` und `2` sind gerade. `1` und `3` werden übersprungen. Als Text entsteht `02`.

### Frage 16

**Antwort:** B

**Erklärung:** Der Wert `2` steht zweimal in der Liste.

### Frage 17

**Antwort:** B, C

**Erklärung:** `append` und `insert` mit einer Liste packen diese Liste als ein Element ein. `extend` und `+=` übernehmen die einzelnen Zahlen.

### Frage 18

**Antwort:** 1–B, 2–A, 3–C, 4–D

**Erklärung:** Nach dem Ergänzen gibt es zwei Paare. Die Schlüssel stehen in Einfügereihenfolge.

### Frage 19

**Antwort:** `upper`

**Erklärung:** `upper` liefert einen neuen String in Großbuchstaben.

### Frage 20

**Antwort:** B

**Erklärung:** `-1` ist das letzte Zeichen.

### Frage 21

**Antwort:** (1, 2)

**Erklärung:** `+` baut ein neues Tupel. Es ändert die beiden kurzen Tupel nicht.

### Frage 22

**Antwort:** A, C

**Erklärung:** `not in` ist wahr, wenn der Wert fehlt. `"a"` steckt in `"ab"`, `"z"` und `20` nicht. `20 not in` wäre falsch, weil `20` enthalten ist.

### Frage 23

**Antwort:** B

**Erklärung:** `1 + summe_bis(0)` ist `1 + 0`.

### Frage 24

**Antwort:** A

**Erklärung:** `return None` behandelt die Ausnahme und liefert `None`. `raise` wirft weiter. `return 0` wäre ein anderer Wert. Die Division im `except` würde wieder scheitern.

### Frage 25

**Antwort:** A, B, C

**Erklärung:** Der Default ist `"!"`. D setzt ein Fragezeichen und ergibt `"Hallo Ada?"`.

### Frage 26

**Antwort:** C, B, A

**Erklärung:** `KeyError` ist spezieller als `LookupError` und muss davor stehen.

### Frage 27

**Antwort:** LookupError

**Erklärung:** Der Syllabus nennt `LookupError` als abstrakte Oberklasse von `KeyError` und `IndexError`.

### Frage 28

**Antwort:** C

**Erklärung:** Nicht gefangene Ausnahmen laufen durch `mitte` hindurch. Der erste `except` sitzt in `aussen`.

### Frage 29

**Antwort:** `IndexError`

**Erklärung:** Ein einzelner Index außerhalb der Länge wirft `IndexError`. Ein Slice täte das nicht.

### Frage 30

**Antwort:** A, C

**Erklärung:** Der Generator rechnet die Werte erst, wenn jemand ihn ausliest. `yield` ist gültige Syntax.
