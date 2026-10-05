# Testprüfung 07

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

`if x > 0` ohne Doppelpunkt. Wo liegt der Fehler?

- A) in der Semantik, weil `>` keine Bedeutung hat
- B) in der Syntax, weil nach `if` ein `:` fehlen darf
- C) in der Syntax, weil der Doppelpunkt die Form des `if` abschließt
- D) nirgends, der Doppelpunkt ist nur PEP 8

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

`x = 1; y = 2` in einer Zeile. Was stimmt?

- A) Das ist immer ein Syntaxfehler.
- B) Es sind zwei Anweisungen. PEP 8 will sie trotzdem auf zwei Zeilen.
- C) Der Strichpunkt ist ein Kommentar.
- D) Nur die zweite Zuweisung wird ausgeführt.

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

Welche Punkte sind PEP-8-Empfehlungen und keine Syntaxregel? Wähle alle zutreffenden Antworten.

- A) vier Leerzeichen je Ebene statt eines Tabs
- B) `snake_case` für Funktionen
- C) ein Schlüsselwort darf kein Variablenname sein
- D) eine Anweisung pro Zeile

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

`1.5e-1` hat den Wert ___. Schreibe ihn als Dezimalbruch, zum Beispiel `0.15`.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Ein Programm speichert das Ergebnis einer ganzzahligen Division:

```python
q = -5 // 2
```

Was steht in `q`?

- A) `-2`
- B) `-2.5`
- C) `-3`
- D) `2`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.5 · 3 Punkte

Aus dem Text `"1.5"` soll die Gleitkommazahl werden, nicht der Integer `1`.

```python
zahl = ___("1.5")
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welchen Wert hat `1 << 2 + 1`?

- A) `5`
- B) `8`
- C) `6`
- D) `3`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

```python
name = ""
if name:
    gruss = name
else:
    gruss = "unbekannt"
```

Was steht in `gruss`?

- A) `""`
- B) `"unbekannt"`
- C) `None`
- D) `False`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Zeichenfolgen sind an einem `if` nötig, damit der Block gültig ist? Wähle alle zutreffenden Antworten.

- A) ein Doppelpunkt nach der Bedingung
- B) mindestens eine Anweisung im Körper, notfalls `pass`
- C) immer ein `else`
- D) eine Einrückung für den Körper

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

`s` startet leer. Eine Schleife über `range(3)` überspringt `i == 1` mit `continue` und hängt sonst `str(i)` an. Was steht am Ende in `s`?

- A) `"012"`
- B) `"02"`
- C) `"01"`
- D) `"12"`

### Frage 11 · Sortieren · Block 2 · Ziel 2.1 · 4 Punkte

Ordne von hoher zu niedriger Priorität. Gib die Buchstaben an.

- A) unäres `-`
- B) `**`
- C) `*`
- D) binäres `+`

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt `list(range(2, 8, 3))`?

- A) `[2, 5]`
- B) `[2, 5, 8]`
- C) `[2, 3, 4, 5, 6, 7]`
- D) `[8, 5, 2]`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile setzt `status` nur, wenn die Schleife ohne `break` endet?

```python
for n in range(2, 4):
    if n == 9:
        break
___
    status = "vollstaendig"
```

- A) `else:`
- B) `elif n == 9:`
- C) `continue`
- D) `except:`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Ein `while` zählt `n` herunter und trifft `continue`, bevor `n` kleiner wird. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Dieselbe Bedingung kann immer wieder wahr sein.
- B) `continue` springt zur nächsten Prüfung, ohne den Rest des Körpers auszuführen.
- C) Die Änderung von `n` muss in diesem Muster vor dem `continue` stehen, wenn sie den Abbruch tragen soll.
- D) `continue` beendet das Programm.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

`list(range(3, 1))` ergibt ___. Schreibe das Listen-Literal.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Was passiert bei `[10, 20, 30][1:100]`?

- A) `IndexError`
- B) `[20, 30]`
- C) `[10, 20, 30]`
- D) `[]`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Startliste `[9, 1, 2]`. Welche Aufrufe entfernen den Wert `1`, nicht den Index `1`? Wähle alle zutreffenden Antworten.

- A) `werte.remove(1)`
- B) `del werte[1]`
- C) `werte.pop(1)`
- D) `werte.index(1)`

### Frage 18 · Zuordnen · Block 3 · Ziel 3.4 · 4 Punkte

Ordne zu.

1. `"Ab".lower()`
2. `"  ab ".strip()`
3. `"ab".replace("a", "x")`
4. `"ab".startswith("a")`

- A) `"ab"`, entstanden durch Entfernen von Leerzeichen
- B) `"xb"`
- C) `True`
- D) `"ab"`, entstanden durch Kleinschreibung

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.4 · 4 Punkte

Ergänze die Methode, die an jedem Komma trennt.

```python
teile = "a,b".___(",")
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.1 · 3 Punkte

Welche Konstruktion ergibt drei unabhängige Zeilen?

- A) `[[0, 0]] * 3`
- B) `[[0, 0] for _ in range(3)]`
- C) `[0, 0] * 3`
- D) `[[0] * 2] * 3`

### Frage 21 · Lückentext · Block 3 · Ziel 3.4 · 4 Punkte

`"cdef"[1:3]` ergibt ___.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

Welche Aussagen treffen auf Tupel zu, auf Listen aber nicht? Wähle alle zutreffenden Antworten.

- A) Item-Zuweisung wirft `TypeError`.
- B) Index `0` liest das erste Element.
- C) Es gibt kein `append`.
- D) Ein Slice hat denselben Folge-Typ wie die Quelle, hier also Tupel.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

```python
def zeige():
    print(1)

ergebnis = zeige()
```

Was ist `ergebnis`, nachdem die `1` ausgegeben wurde?

- A) `1`
- B) `"1"`
- C) `None`
- D) `True`

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

`def addiere(a, b): return a + b`. Welcher Aufruf ist gültig und ergibt `3`?

- A) `addiere(1, b=2)`
- B) `addiere(a=1, 2)`
- C) `addiere(1, 2, 0)`
- D) `addiere(b=1, 2)`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
x = 10

def f(x):
    return x + 1
```

Welche Aussagen stimmen für den Aufruf `f(3)`? Wähle alle zutreffenden Antworten.

- A) Der Parameter verdeckt das äußere `x`.
- B) Der Rückgabewert ist `4`.
- C) Das äußere `x` wird `4`.
- D) Das äußere `x` bleibt `10`.

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Ordne so, dass `ValueError` behandelt wird und `Exception` nur übrig bleibt. Gib die Buchstaben in der Quelltext-Reihenfolge an.

- A) `except Exception:`
- B) `except ValueError:`
- C) `try:`

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

Wie viele der beiden Klassen `SystemExit` und `KeyboardInterrupt` sind Unterklassen von `Exception`? Schreibe die Anzahl ___.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

Wann läuft ein `finally`-Block?

- A) nur wenn eine Ausnahme kam
- B) nur wenn keine Ausnahme kam
- C) in beiden Fällen
- D) nur wenn `else` fehlt

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.1 · 4 Punkte

Ergänze das Schlüsselwort, das aus der Funktion einen Generator macht und den aktuellen `i` liefert.

```python
def zaehle(n):
    i = 0
    while i < n:
        ___ i
        i += 1
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Welche `except`-Klauseln fangen `SystemExit`? Wähle alle zutreffenden Antworten.

- A) `except SystemExit`
- B) `except BaseException`
- C) `except Exception`
- D) `except ArithmeticError`

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** C

**Erklärung:** Der Doppelpunkt gehört zur Form von `if`. Ohne ihn ist es ein Syntaxfehler.

### Frage 2

**Antwort:** B

**Erklärung:** Der Strichpunkt trennt Anweisungen. Er ist gültig und im Stil unerwünscht.

### Frage 3

**Antwort:** A, B, D

**Erklärung:** Schlüsselwörter sind Syntax. Einrückungsbreite, `snake_case` und eine Anweisung pro Zeile sind Stil, solange die Einrückung in sich konsistent bleibt.

### Frage 4

**Antwort:** 0.15

**Erklärung:** Der Exponent `-1` teilt `1.5` durch 10. Der Typ ist `float`.

### Frage 5

**Antwort:** C

**Erklärung:** `-5 / 2` liegt bei `-2.5`. `//` geht zur nächsten ganzen Zahl Richtung minus unendlich, also `-3`.

### Frage 6

**Antwort:** `float`

**Erklärung:** `int("1.5")` würde `ValueError` werfen. `float` liest den Punkt.

### Frage 7

**Antwort:** B

**Erklärung:** `+` bindet enger als `<<`. Gerechnet wird `1 << 3`, also `8`.

### Frage 8

**Antwort:** B

**Erklärung:** Der leere String ist falsch. Der `else`-Zweig setzt den Ersatztext.

### Frage 9

**Antwort:** A, B, D

**Erklärung:** `else` ist erlaubt, aber nicht Pflicht.

### Frage 10

**Antwort:** B

**Erklärung:** `0` wird angehängt, `1` übersprungen, `2` angehängt.

### Frage 11

**Antwort:** B, A, C, D

**Erklärung:** Potenz vor unärem Minus, das vor `*`, das vor binärem `+`.

### Frage 12

**Antwort:** A

**Erklärung:** `2` und `5`. Die `8` ist der ausgeschlossene Stopp.

### Frage 13

**Antwort:** A

**Erklärung:** `else` auf der Höhe von `for` gehört zur Schleife. `9` kommt nicht vor, also läuft dieser Zweig.

### Frage 14

**Antwort:** A, B, C

**Erklärung:** Springt man vor der Verkleinerung von `n` weiter, bleibt die Schleife in demselben Zustand.

### Frage 15

**Antwort:** []

**Erklärung:** Der positive Standardschritt kommt von `3` nicht zu `1`. Die Folge ist leer.

### Frage 16

**Antwort:** B

**Erklärung:** Ein Slice schneidet an den vorhandenen Grenzen ab und wirft dafür keinen `IndexError`.

### Frage 17

**Antwort:** A

**Erklärung:** `remove` sucht den Wert. `del` und `pop` mit `1` treffen den Index `1`, an dem hier ebenfalls `1` steht, entfernen also zufällig denselben Eintrag über den Index, nicht über die Suche nach dem Wert. Die Frage verlangt die Suche nach dem Wert. `index` löscht nicht. Nur `remove` sucht den Wert.

### Frage 18

**Antwort:** 1–D, 2–A, 3–B, 4–C

**Erklärung:** `lower` schreibt klein. `strip` entfernt die Leerzeichen. `replace` tauscht `a`. `startswith` liefert einen Bool. Die beiden `"ab"` entstehen auf verschiedenen Wegen und sind deshalb verschiedene Ziele.

### Frage 19

**Antwort:** `split`

**Erklärung:** Das Argument ist das Trennzeichen. Ergebnis ist `["a", "b"]`.

### Frage 20

**Antwort:** B

**Erklärung:** Jeder Durchlauf der Comprehension erzeugt eine neue innere Liste. Die `*`-Formen teilen Referenzen oder bauen eine flache Zahlenliste.

### Frage 21

**Antwort:** de

**Erklärung:** Indizes 1 und 2 von `"cdef"` sind `d` und `e`.

### Frage 22

**Antwort:** A, C, D

**Erklärung:** Lesen per Index können beide. Tupel lassen sich nicht per Item ändern und haben kein `append`. Ihr Slice bleibt ein Tupel.

### Frage 23

**Antwort:** C

**Erklärung:** `print` zeigt die `1`, der Funktionswert ohne `return` ist `None`.

### Frage 24

**Antwort:** A

**Erklärung:** Positionale Argumente stehen vorn. Die anderen drei Aufrufe sind Syntax- oder Typfehler.

### Frage 25

**Antwort:** A, B, D

**Erklärung:** Der Parameter `x` ist lokal und erhält `3`. Das Modul-`x` wird nicht geschrieben.

### Frage 26

**Antwort:** C, B, A

**Erklärung:** `ValueError` muss vor der Oberklasse `Exception` stehen.

### Frage 27

**Antwort:** 0

**Erklärung:** Beide hängen direkt unter `BaseException`.

### Frage 28

**Antwort:** C

**Erklärung:** `finally` räumt auf, ob der `try` durchlief oder eine Ausnahme kam.

### Frage 29

**Antwort:** `yield`

**Erklärung:** `yield` pausiert die Funktion und macht den Aufruf zum Generator.

### Frage 30

**Antwort:** A, B

**Erklärung:** `SystemExit` ist eine `BaseException`, keine `Exception` und keine `ArithmeticError`.
