# Testprüfung 03

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

Welche Beschreibung trifft die Syntax, nicht die Semantik?

- A) `1 / 0` hat keine ausführbare Bedeutung.
- B) `print("hi"` verletzt die Form, weil eine Klammer fehlt.
- C) Ein Name zeigt nach der Zuweisung auf ein Objekt.
- D) `len` liefert die Anzahl der Elemente.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Wie viele Leerzeichen je Ebene empfiehlt PEP 8 für die Einrückung?

- A) 2
- B) 4
- C) 8
- D) Ein Tab ist vorgeschrieben, Leerzeichen sind verboten.

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

Welche Aussagen über `True` stimmen? Wähle alle zutreffenden Antworten.

- A) `True` ist ein Schlüsselwort.
- B) `True == 1` ist wahr.
- C) `true` mit kleinem t ist dasselbe Literal.
- D) `bool` ist eine Unterklasse von `int`.

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

`2e3` hat den Zahlenwert ___. Schreibe ihn als Dezimalzahl mit Nachkomma, so wie `float` ihn darstellt, zum Beispiel `2000.0`.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `2 + 3 * 4`?

- A) `20`
- B) `14`
- C) `24`
- D) `9`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.4 · 3 Punkte

Ergänze den Operator, der aus `"ab"` den String `"ababab"` macht.

```python
text = "ab" ___ 3
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.5 · 3 Punkte

Was liefert `input()`, wenn die Person die Zeichen `42` eintippt?

- A) den Integer `42`
- B) den Float `42.0`
- C) den String `"42"`
- D) `None`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
alter = 20
karte = False
if alter >= 18:
    if karte:
        eintritt = "ja"
    else:
        eintritt = "ausweis_fehlt"
else:
    eintritt = "nein"
```

Was steht in `eintritt`?

- A) `"ja"`
- B) `"ausweis_fehlt"`
- C) `"nein"`
- D) die Variable bleibt ungebunden

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

`name = ""`. Welche Bedingungen sind in diesem Zustand falsch? Wähle alle zutreffenden Antworten.

- A) `if name:`
- B) `if not name:`
- C) `if name == "":`
- D) `if name == "Ada":`

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

Eine innere Schleife läuft `b` über `range(3)` und bricht ab, sobald `b == 1` ist. Die äußere Schleife läuft `a` über `range(2)` und hängt vor dem Abbruch `str(a) + str(b)` an einen anfangs leeren String. Welcher String entsteht?

- A) `"0010"`
- B) `"0110"`
- C) `"00011011"`
- D) `""`

### Frage 11 · Sortieren · Block 2 · Ziel 2.2 · 4 Punkte

Ordne die Bausteine so, dass eine funktionierende `for`-Schleife von oben nach unten entsteht. Gib die Buchstaben an.

- A) `s += i`
- B) `s = 0`
- C) `for i in range(1, 4):`

Die Zeile `s = 0` muss vor der Schleife stehen. Der Körper ist eingerückt und kommt in der Antwort nach der `for`-Zeile.

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt `list(range(2, 2))`?

- A) `[2]`
- B) `[2, 2]`
- C) `[]`
- D) `range` wirft `ValueError`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile sammelt die Zeichen vor dem ersten `d` und bricht dann ab?

```python
ergebnis = ""
for zeichen in "abcde":
    ___
    ergebnis += zeichen
```

- A) `if zeichen == "d": break`
- B) `if zeichen == "d": continue`
- C) `if zeichen == "a": break`
- D) `pass`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Aussagen über `break` stimmen? Wähle alle zutreffenden Antworten.

- A) Es verlässt die innerste Schleife.
- B) Es beendet automatisch auch die äußere Schleife.
- C) Ein `else` derselben Schleife läuft danach nicht.
- D) Es ist nur innerhalb von `if` erlaubt, nie in einer Schleife.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

`range(1, 4)` erzeugt die Summe ___, wenn man alle Werte addiert.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Was ergibt `[[0, 0]] * 2` nach der Zuweisung `m[0][0] = 1` an dieses `m`?

- A) `[[1, 0], [0, 0]]`
- B) `[[1, 0], [1, 0]]`
- C) `[[1, 0]]`
- D) `TypeError`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Ausdrücke liefern eine neue Liste und lassen `[3, 1, 2]` unverändert, wenn das die Quelle ist? Wähle alle zutreffenden Antworten.

- A) `sorted(quelle)`
- B) `quelle.sort()`
- C) `quelle[:]`
- D) `quelle.reverse()`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.3 · 4 Punkte

`person = {"name": "Ada", "jahr": 1815}`. Ordne zu.

1. `"name" in person`
2. `"Ada" in person`
3. `person["jahr"]`
4. `len(person)`

- A) `1815`
- B) `True`
- C) `False`
- D) `2`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.4 · 4 Punkte

Ergänze die Methode, die bei fehlendem Teil `-1` liefert und nicht wirft.

```python
stelle = "ab".___("z")
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.2 · 3 Punkte

Was ist der Typ von `(1)`?

- A) `tuple`
- B) `int`
- C) `list`
- D) `str`

### Frage 21 · Lückentext · Block 3 · Ziel 3.4 · 4 Punkte

`"abc"[::-1]` ergibt ___.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Operationen entfernen etwas aus `[9, 1, 2]` so, dass am Ende `[2]` dasteht, wenn zuerst der Wert `1` und danach der dann vordere Eintrag `9` entfernt wird? Wähle alle nötigen Arten, die in dieser Reihenfolge passen.

- A) `remove` sucht einen Wert
- B) `del` an einem Index entfernt diesen Eintrag
- C) `index` allein löscht den Eintrag
- D) `sorted` löscht Duplikate an Ort und Stelle

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

```python
def vorzeichen(n):
    if n > 0:
        return "plus"
    if n < 0:
        return "minus"
    return "null"
```

Was liefert `vorzeichen(0)`?

- A) `"plus"`
- B) `"minus"`
- C) `"null"`
- D) `None`

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Zeile verhindert, dass zwei Aufrufe ohne zweites Argument dieselbe Liste teilen?

```python
def sammeln(wert, folge=None):
    ___
    folge.append(wert)
    return folge
```

- A) `if folge is None: folge = []`
- B) `folge = folge`
- C) `global folge`
- D) `folge.append(wert)`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
x = 1

def falle():
    print(x)
    x = 2
```

Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der Aufruf wirft `UnboundLocalError`.
- B) `x = 2` macht `x` in der ganzen Funktion lokal.
- C) `print(x)` liest zuverlässig das äußere `x`.
- D) Das äußere `x` bleibt `1`, weil der Aufruf vorher scheitert.

### Frage 26 · Sortieren · Block 4 · Ziel 4.3 · 3 Punkte

Ordne von der Wurzel zu `ZeroDivisionError`. Gib die Buchstaben an.

- A) `ArithmeticError`
- B) `BaseException`
- C) `ZeroDivisionError`
- D) `Exception`

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`[1][3]` wirft ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

```python
def innen():
    return 1 / 0

def aussen():
    try:
        return innen()
    except ZeroDivisionError:
        return None
```

Was liefert `aussen()`?

- A) `ZeroDivisionError` bis zum Interpreter, `aussen` fängt nichts
- B) `None`
- C) `0`
- D) `1`

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze den Typ, der zu `int("x")` passt.

```python
try:
    int("x")
except ___:
    art = "wert"
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 3 Punkte

Welche Aussagen über `return` stimmen? Wähle alle zutreffenden Antworten.

- A) Es beendet die Funktion.
- B) `return` ohne Ausdruck liefert `None`.
- C) `print(1)` ist dasselbe wie `return 1`.
- D) Nach einem ausgeführten `return` laufen weitere Zeilen derselben Funktion nicht mehr.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** B

**Erklärung:** Die fehlende Klammer ist Form, also Syntax. `1 / 0` ist Bedeutung zur Laufzeit.

### Frage 2

**Antwort:** B

**Erklärung:** PEP 8 nennt vier Leerzeichen. Ein Tab ist nicht vorgeschrieben.

### Frage 3

**Antwort:** A, B, D

**Erklärung:** Nur die Schreibweise `True` ist das Literal. `bool` erbt von `int`, deshalb gilt `True == 1`.

### Frage 4

**Antwort:** 2000.0

**Erklärung:** `2e3` ist `2 * 10**3` und hat den Typ `float`.

### Frage 5

**Antwort:** B

**Erklärung:** `*` bindet enger als `+`. `3 * 4` wird zuerst `12`.

### Frage 6

**Antwort:** `*`

**Erklärung:** Ein String mal eine ganze Zahl wiederholt den String.

### Frage 7

**Antwort:** C

**Erklärung:** `input` liefert immer Text. Die Zahl entstünde erst durch `int`.

### Frage 8

**Antwort:** B

**Erklärung:** Das äußere `if` ist wahr, das innere ist falsch, also der innere `else`-Zweig.

### Frage 9

**Antwort:** A, D

**Erklärung:** Der leere String ist falsch und ungleich `"Ada"`. `not name` und der Vergleich mit `""` sind wahr. Gefragt sind die falschen Bedingungen.

### Frage 10

**Antwort:** A

**Erklärung:** Für `a` gleich `0` und `1` wird nur `b` gleich `0` angehängt, danach bricht die innere Schleife ab.

### Frage 11

**Antwort:** B, C, A

**Erklärung:** Erst der Startwert, dann die Schleife, dann der eingerückte Körper.

### Frage 12

**Antwort:** C

**Erklärung:** Start und Stopp sind gleich, der Schritt ist positiv. Die Folge ist leer.

### Frage 13

**Antwort:** A

**Erklärung:** `break` vor dem Anhängen lässt `"d"` draußen. `continue` würde es nur überspringen und danach `"e"` noch nehmen.

### Frage 14

**Antwort:** A, C

**Erklärung:** `break` gilt nur für eine Schleife, und das `else` dieser Schleife entfällt.

### Frage 15

**Antwort:** 6

**Erklärung:** `1 + 2 + 3`. Die `4` ist ausgeschlossen.

### Frage 16

**Antwort:** B

**Erklärung:** `*` wiederholt die Referenz auf dieselbe innere Liste. Beide Zeilen sehen die Änderung.

### Frage 17

**Antwort:** A, C

**Erklärung:** `sort` und `reverse` ändern an Ort und Stelle und liefern `None`. `sorted` und `[:]` bauen neue Listen.

### Frage 18

**Antwort:** 1–B, 2–C, 3–A, 4–D

**Erklärung:** `in` trifft den Schlüssel `"name"`, nicht den Wert `"Ada"`.

### Frage 19

**Antwort:** `find`

**Erklärung:** `find` liefert `-1`. `index` würde `ValueError` werfen.

### Frage 20

**Antwort:** B

**Erklärung:** Klammern ohne Komma gruppieren nur den Ausdruck. Das Komma macht das Tupel.

### Frage 21

**Antwort:** cba

**Erklärung:** Schritt `-1` über den ganzen String dreht die Reihenfolge um.

### Frage 22

**Antwort:** A, B

**Erklärung:** `remove(1)` löscht den Wert, `del` am Index `0` danach den verbliebenen Neuner. `index` und `sorted` löschen nichts.

### Frage 23

**Antwort:** C

**Erklärung:** Beide Vergleiche sind falsch, also der letzte `return`.

### Frage 24

**Antwort:** A

**Erklärung:** `None` als Standard markiert „keine Liste übergeben“. Die neue Liste entsteht im Körper.

### Frage 25

**Antwort:** A, B, D

**Erklärung:** Durch die spätere Zuweisung ist `x` lokal. Das Lesen davor findet noch kein lokales Objekt. Das äußere `x` wird nicht geschrieben.

### Frage 26

**Antwort:** B, D, A, C

**Erklärung:** `ZeroDivisionError` liegt unter `ArithmeticError`, das unter `Exception`, das unter `BaseException`.

### Frage 27

**Antwort:** IndexError

**Erklärung:** Der Index `3` liegt außerhalb der einelementigen Liste.

### Frage 28

**Antwort:** B

**Erklärung:** `innen` fängt nichts. `aussen` übernimmt `ZeroDivisionError` und gibt `None` zurück.

### Frage 29

**Antwort:** `ValueError`

**Erklärung:** `"x"` ist ein String, aber keine Ganzzahl in Basis 10.

### Frage 30

**Antwort:** A, B, D

**Erklärung:** `print` zeigt einen Wert und liefert selbst `None`. Es ersetzt kein `return`.
