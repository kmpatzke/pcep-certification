# Testprüfung 09

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

Der Name `print` als erlaubtes Wort im Quelltext gehört zu welcher Ebene?

- A) Lexik
- B) nur zur Semantik, weil Namen keine Form haben
- C) nur zu PEP 8
- D) zu den Kommentaren

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

```python
# print("aus")
print("an")
```

Was erscheint auf der Konsole?

- A) nichts
- B) `aus`
- C) `an`
- D) `aus` und `an`

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

`wert` zeigt zuerst auf `10`, dann auf `wert + 5`, dann auf den String `"ok"`, weil das Zwischenergebnis größer als `12` ist. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Ein Name darf nacheinander auf verschiedene Typen zeigen.
- B) Nach der letzten Zuweisung ist `wert` der String `"ok"`.
- C) Die zweite Zuweisung ist ein Syntaxfehler, weil `wert` schon ein `int` war.
- D) `15 > 12` entscheidet den letzten Zweig.

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

Die Bits `1`, `0`, `0` stehen als Python-Literal `0b100` im Quelltext. Welche Zahl zur Basis 10 ist das? ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `0 or "" or "x"`?

- A) `0`
- B) `""`
- C) `"x"`
- D) `False`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.4 · 3 Punkte

Ergänze die Kurzform, die ganzzahlig durch `4` teilt.

```python
x = 9
x ___ 4
```

`x` soll danach `2` sein.

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.4 · 3 Punkte

Welchen Wahrheitswert hat `bool(" ")`?

- A) `False`, weil kein Buchstabe darin steht
- B) `True`, weil der String nicht leer ist
- C) `None`
- D) `ValueError`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

Was ist an diesem Fragment falsch?

```python
if note == 1:
    text = "sehr gut"
else:
    text = "andere"
elif note == 2:
    text = "gut"
```

- A) nichts, `elif` darf auf `else` folgen
- B) `elif` nach `else` ist ein Syntaxfehler
- C) `else` darf keinen Block haben
- D) `note` muss ein String sein

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Ausdrücke sind wahr? Wähle alle zutreffenden Antworten.

- A) `(5 < 1) < 2`
- B) `5 < 1 < 2`
- C) `not ""`
- D) `1 and 2`

### Frage 10 · Szenario · Block 2 · Ziel 2.2 · 4 Punkte

Eine Schleife über `range(5)` bricht ab, sobald `i == 3` ist, und hängt vorher `str(i)` an. Es gibt kein `else`. Welcher Text entsteht?

- A) `"012"`
- B) `"0123"`
- C) `"01234"`
- D) `"3"`

### Frage 11 · Sortieren · Block 2 · Ziel 2.2 · 4 Punkte

Ordne die Argumente von `range(1, 6, 2)` von links nach rechts ihrer Rolle nach. Gib die Buchstaben an.

- A) Stopp `6`
- B) Schritt `2`
- C) Start `1`

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Was ergibt `list(range(0))`?

- A) `[0]`
- B) `[]`
- C) `None`
- D) `ValueError`

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile beendet diese Schleife, nachdem drei Körperläufe `n` von `3` auf `0` gebracht haben?

```python
n = 3
while n > 0:
    n -= 1
___
```

Die Schleife soll nicht zusätzlich abgebrochen werden, sondern durch die Bedingung enden. Welche Zeile lässt die Bedingung ihre Arbeit tun?

- A) `pass`
- B) `n += 1`
- C) `n = 3`
- D) `break`

`break` würde auch enden, aber schon im ersten Durchlauf, bevor `n` bei `0` ankommt, wenn es ganz oben stünde. Hier steht die Lücke nach `n -= 1`. Ein `break` an dieser Stelle würde ebenfalls nach dem ersten Durchlauf enden. Gefragt ist die Zeile, die den Zähler nicht wieder anhebt und nicht selbst abbricht.

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Einrückungen sind für dieses Muster richtig? Wähle alle zutreffenden Aussagen.

- A) Der Körper von `if` steht weiter rechts als das `if`.
- B) Ein `else` auf derselben Spalte wie das `if` gehört zu diesem `if`.
- C) Ein `else` weiter rechts als das äußere `if` kann zum inneren `if` gehören.
- D) Alle Zeilen einer Datei müssen gleich weit eingerückt sein.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

Die Summe der Werte von `range(2, 6)` ist ___.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

```python
a = [1, 2, 3]
b = a
c = a[:]
```

Welche Aussage stimmt?

- A) `b is a` und `c is a`
- B) `b is a`, aber `c is a` ist falsch
- C) beide Kopien sind Tupel
- D) `c.append(4)` ändert `a`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.3 · 3 Punkte

`{"a": 1, "a": 2, "b": 1}`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Es gibt zwei Schlüssel.
- B) `buch["a"]` ist `2`.
- C) `1 in buch` ist wahr.
- D) `len(buch)` ist `2`.

### Frage 18 · Zuordnen · Block 3 · Ziel 3.1 · 4 Punkte

`werte = [10, 20, 30, 40]`. Ordne zu.

1. `werte[0]`
2. `werte[-2]`
3. `len(werte)`
4. `werte[::2]`

- A) `10`
- B) `30`
- C) `4`
- D) `[10, 30]`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze den Operator, der wahr ist, weil `9` fehlt.

```python
fehlt = 9 ___ werte
```

`werte` ist `[1, 2, 3]`. `fehlt` soll `True` werden. Es sind zwei Wörter.

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.4 · 3 Punkte

Was ergibt `"a" * 0`?

- A) `0`
- B) `""`
- C) `"a"`
- D) `TypeError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.4 · 4 Punkte

`"x-y-z".split("-")` ergibt ___. Schreibe das Listen-Literal.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

`falsch = [[0] * 2] * 2` und danach `falsch[0][0] = 1`. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Beide Zeilen zeigen `1` an Index `0`.
- B) Nur die erste Zeile ändert sich.
- C) Die Ursache ist eine geteilte innere Liste.
- D) `[0] * 2` allein, als Zahlenliste, teilt keine veränderbare Innenliste.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

Was ist `None`?

- A) ein gewöhnlicher Variablenname, den man neu zuweisen darf
- B) ein Schlüsselwort und der Wert einer Funktion ohne `return`
- C) dasselbe wie `0`
- D) ein Operator

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.2 · 3 Punkte

Welche Definition ist gültig?

- A) `def f(a=1, b):`
- B) `def f(a, b=1):`
- C) `def f(a=1, b=2, c):`
- D) `def f(a, b): global`

`global` ohne Namen ist kein gültiger Körper. Es geht um die Parameterliste. Wähle die eine gültige Definition.

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
x = 1

def setzen():
    global x
    x = x + 4
    return x
```

Nach `setzen()`: welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Der Rückgabewert ist `5`.
- B) Das äußere `x` ist `5`.
- C) `global` wäre überflüssig, weil jede Zuweisung automatisch nach außen schreibt.
- D) `x + 4` liest den Wert, der vor der Zuweisung außen lag.

### Frage 26 · Sortieren · Block 4 · Ziel 4.4 · 3 Punkte

Der Fehler entsteht in `innen`, läuft durch `mitte` und wird in `aussen` gefangen. Ordne den Weg von der Entstehung bis zur Behandlung. Gib die Buchstaben an.

- A) `aussen` fängt
- B) `innen` wirft
- C) `mitte` reicht weiter

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`int` bekommt einen String, in dem nur ein Leerzeichen steht. Welcher Ausnahmetyp entsteht? Schreibe den Namen: ___.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.4 · 3 Punkte

Ein nacktes `except:` ohne Typ fängt welches der folgenden Ereignisse mit?

- A) nur `ValueError`
- B) auch `KeyboardInterrupt`
- C) nur Stilwarnungen
- D) keine Ausnahme, es ist ein Kommentar

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.3 · 4 Punkte

Ergänze die Wurzelklasse, unter der `SystemExit` hängt.

```python
issubclass(SystemExit, ___)
```

Der Ausdruck soll `True` ergeben. `Exception` wäre falsch.

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 3 Punkte

Welche Aussagen über einen rekursiven Aufruf stimmen? Wähle alle zutreffenden Antworten.

- A) Der innere Aufruf hat eigene lokale Namen.
- B) Der äußere Aufruf sieht die lokalen Namen des inneren Aufrufs unter denselben Namen automatisch.
- C) Der innere Aufruf muss einen Wert mit `return` oder einen Fehler liefern, damit der äußere weiterrechnen kann.
- D) Zwei Aufrufe dürfen dieselbe Funktion sein.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** A

**Erklärung:** Ein erlaubter Name ist ein Lexem. Ob der Aufruf wohlgeformt ist, ist eine spätere Frage der Syntax.

### Frage 2

**Antwort:** C

**Erklärung:** Die erste Zeile ist komplett auskommentiert. Die zweite `print`-Anweisung läuft.

### Frage 3

**Antwort:** A, B, D

**Erklärung:** Python bindet den Namen neu. `10 + 5` ist `15`, und `15 > 12` führt zum String `"ok"`.

### Frage 4

**Antwort:** 4

**Erklärung:** Binär `100` ist vier.

### Frage 5

**Antwort:** C

**Erklärung:** `or` liefert den ersten wahren Operanden. `0` und `""` sind falsch, `"x"` ist wahr.

### Frage 6

**Antwort:** `//=`

**Erklärung:** `9 // 4` ist `2`. Die Kurzform schreibt das Ergebnis nach `x` zurück.

### Frage 7

**Antwort:** B

**Erklärung:** Ein Leerzeichen ist ein Zeichen. Der String ist nicht leer.

### Frage 8

**Antwort:** B

**Erklärung:** `elif` muss vor `else` stehen. Danach ist die Verzweigung zu Ende.

### Frage 9

**Antwort:** A, C

**Erklärung:** `(5 < 1)` ist `False`, und `False < 2` ist wahr. Die Kette `5 < 1 < 2` ist falsch. `not ""` ist wahr. `1 and 2` ist `2`, nicht `True`.

### Frage 10

**Antwort:** A

**Erklärung:** `0`, `1` und `2` werden angehängt. Bei `3` kommt `break`, bevor angehängt wird.

### Frage 11

**Antwort:** C, A, B

**Erklärung:** Die Reihenfolge im Aufruf ist Start, Stopp, Schritt.

### Frage 12

**Antwort:** B

**Erklärung:** `range(0)` hat null Durchläufe.

### Frage 13

**Antwort:** A

**Erklärung:** `n -= 1` macht die Bedingung nach drei Durchläufen falsch. `pass` ändert daran nichts. Die anderen Zeilen heben den Zähler wieder an oder brechen zu früh ab.

### Frage 14

**Antwort:** A, B, C

**Erklärung:** Gleich weit eingerückt müssen die Zeilen eines Blocks sein, nicht die ganze Datei.

### Frage 15

**Antwort:** 14

**Erklärung:** `2 + 3 + 4 + 5`. Die `6` gehört nicht mehr dazu.

### Frage 16

**Antwort:** B

**Erklärung:** `b` ist ein zweiter Name. `c` ist eine flache Kopie. Anhängen an `c` lässt `a` in Ruhe.

### Frage 17

**Antwort:** A, B, D

**Erklärung:** Der zweite Wert für `"a"` ersetzt den ersten. `in` prüft Schlüssel, also nicht die `1`.

### Frage 18

**Antwort:** 1–A, 2–B, 3–C, 4–D

**Erklärung:** Index `0` ist `10`, Index `-2` ist `30`, die Länge ist `4`, jeder zweite Wert ist `10` und `30`.

### Frage 19

**Antwort:** `not in`

**Erklärung:** `9 not in [1, 2, 3]` ist wahr. `in` allein wäre falsch.

### Frage 20

**Antwort:** B

**Erklärung:** Ein String nullmal wiederholt ergibt den leeren String, nicht die Zahl `0`.

### Frage 21

**Antwort:** ["x", "y", "z"]

**Erklärung:** `split` wirft das Trennzeichen weg und liefert die drei Stücke.

### Frage 22

**Antwort:** A, C, D

**Erklärung:** `*` auf der äußeren Liste wiederholt eine Referenz. Eine Zahlenliste `[0] * 2` hat keine veränderbare innere Liste.

### Frage 23

**Antwort:** B

**Erklärung:** `None` ist reserviert. Funktionen ohne `return` liefern es.

### Frage 24

**Antwort:** B

**Erklärung:** Parameter mit Default stehen hinter Parametern ohne Default. `global` ohne Namen ist zusätzlich ungültig, aber schon A und C scheitern an der Parameterreihenfolge.

### Frage 25

**Antwort:** A, B, D

**Erklärung:** `global` macht die Zuweisung außen sichtbar. Gelesen wird der alte Wert `1`, geschrieben wird `5`. Ohne `global` würde die Zuweisung lokal sein.

### Frage 26

**Antwort:** B, C, A

**Erklärung:** Wer nicht fängt, gibt die Ausnahme an den Aufrufer weiter. Der erste `except` behandelt sie.

### Frage 27

**Antwort:** ValueError

**Erklärung:** Ein String aus Leerzeichen ist keine Ganzzahl. Der Typ wäre zulässig, der Inhalt nicht.

### Frage 28

**Antwort:** B

**Erklärung:** Ein nacktes `except` fängt `BaseException`, also auch `KeyboardInterrupt`. Das verschluckt einen Abbruch.

### Frage 29

**Antwort:** `BaseException`

**Erklärung:** `SystemExit` erbt von `BaseException`, nicht von `Exception`.

### Frage 30

**Antwort:** A, C, D

**Erklärung:** Lokale Namen gehören zu einem Aufruf. Der äußere sieht sie nur, wenn der innere sie als Wert zurückgibt.
