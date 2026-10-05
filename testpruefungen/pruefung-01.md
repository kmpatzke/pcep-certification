# Testprüfung 01

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

Eine Aufgabe zählt nur, wenn sie vollständig stimmt. Die offiziellen Seiten sagen nichts über Teilpunkte. Mehrfachauswahl, Zuordnung und Sortierung geben hier deshalb keinen Teilpunkt.

Bearbeite nur den Frageteil. Der Lösungsteil steht unter dem Trenner.

## Frageteil

### Frage 1 · Einzelauswahl · Block 1 · Ziel 1.1 · 2 Punkte

Wofür steht der Interpreter in der Gegenüberstellung des Syllabus?

- A) Er übersetzt das gesamte Programm, bevor irgendeine Anweisung läuft.
- B) Er führt den Python-Quelltext aus.
- C) Er entfernt Kommentare und ändert sonst nichts.
- D) Er ist nur ein anderer Name für PEP 8.

### Frage 2 · Einzelauswahl · Block 1 · Ziel 1.2 · 2 Punkte

Welches Wort ist ein Schlüsselwort und darf deshalb kein Variablenname sein?

- A) `print`
- B) `length`
- C) `elif`
- D) `main`

### Frage 3 · Mehrfachauswahl · Block 1 · Ziel 1.3 · 3 Punkte

Welche Literale haben den Typ `float`? Wähle alle zutreffenden Antworten.

- A) `2e2`
- B) `4`
- C) `1.0`
- D) `"3.0"`

### Frage 4 · Lückentext · Block 1 · Ziel 1.3 · 3 Punkte

Das Literal `0x10` hat den Dezimalwert ___.

### Frage 5 · Einzelauswahl · Block 1 · Ziel 1.4 · 2 Punkte

Welchen Wert hat `2 ** 3 ** 2`?

- A) `64`
- B) `512`
- C) `12`
- D) `256`

### Frage 6 · Code ergänzen · Block 1 · Ziel 1.4 · 3 Punkte

Ergänze den Operator, damit `ergebnis` den Integer `3` enthält.

```python
ergebnis = 7 ___ 2
```

### Frage 7 · Einzelauswahl · Block 1 · Ziel 1.5 · 3 Punkte

Was gibt ein Aufruf von `print(1)` an den Aufrufer zurück?

- A) den String `"1"`
- B) `None`
- C) `True`
- D) `0`

### Frage 8 · Einzelauswahl · Block 2 · Ziel 2.1 · 4 Punkte

Was steht nach diesem Programm in `spur`?

```python
x = 5
spur = ""
if x > 0:
    spur += "a"
if x > 3:
    spur += "b"
```

- A) `"a"`
- B) `"b"`
- C) `"ab"`
- D) `""`

### Frage 9 · Mehrfachauswahl · Block 2 · Ziel 2.1 · 3 Punkte

Welche Formen sind gültige Verzweigungen? Wähle alle zutreffenden Antworten.

- A) `if` mit `else`
- B) `elif` als erste Anweisung, ohne vorheriges `if`
- C) `if` mit `elif` und `else`
- D) `else` vor dem zugehörigen `if`

### Frage 10 · Szenario · Block 2 · Ziel 2.1 · 4 Punkte

Ein Programm setzt Noten so um: ab 90 Punkte `"A"`, sonst ab 80 `"B"`, sonst `"C"`. Es benutzt `if` / `elif` / `else` in dieser Reihenfolge. Die Punktzahl ist 80. Welcher Buchstabe entsteht?

- A) `"A"`
- B) `"B"`
- C) `"C"`
- D) kein Zweig läuft

### Frage 11 · Sortieren · Block 2 · Ziel 2.1 · 4 Punkte

Ordne die Operatoren von der höchsten Priorität zur niedrigsten. Gib die Buchstaben in dieser Reihenfolge an.

- A) `or`
- B) `+`
- C) `and`
- D) `not`

### Frage 12 · Einzelauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Wie viele Zahlen liefert `range(1, 6, 2)`?

- A) 2
- B) 3
- C) 5
- D) 6

### Frage 13 · Code einsetzen · Block 2 · Ziel 2.2 · 4 Punkte

Welche Zeile muss an der Markierung stehen, damit die Schleife endet und `s` die Summe `6` ist?

```python
n = 3
s = 0
while n > 0:
    s += n
    ___
```

- A) `n = n + 1`
- B) `n = n - 1`
- C) `pass`
- D) `s = 0`

### Frage 14 · Mehrfachauswahl · Block 2 · Ziel 2.2 · 3 Punkte

Welche Aussagen über `else` an einer `for`-Schleife stimmen? Wähle alle zutreffenden Antworten.

- A) `else` läuft, wenn die Schleife nicht mit `break` verlassen wurde.
- B) `else` läuft nur, wenn der Schleifenkörper nie betreten wurde.
- C) `else` wird übersprungen, wenn `break` ausgeführt wurde.
- D) `else` ersetzt die Schleifenbedingung.

### Frage 15 · Lückentext · Block 2 · Ziel 2.2 · 4 Punkte

`range(4)` erzeugt ___ ganze Zahlen. Schreibe die Anzahl.

### Frage 16 · Einzelauswahl · Block 3 · Ziel 3.1 · 4 Punkte

Welchen Wert hat `[10, 20, 30][-1]`?

- A) `10`
- B) `20`
- C) `30`
- D) `IndexError`

### Frage 17 · Mehrfachauswahl · Block 3 · Ziel 3.2 · 3 Punkte

Welche Aussagen über Tupel stimmen? Wähle alle zutreffenden Antworten.

- A) `(1)` ist ein Tupel.
- B) `(1,)` ist ein Tupel mit einem Element.
- C) Elemente liest man per Index.
- D) Nach `t = (1, 2)` ist `t[0] = 9` erlaubt.

### Frage 18 · Zuordnen · Block 3 · Ziel 3.4 · 4 Punkte

Ordne jedem Ausdruck das Ergebnis zu.

Ausdrücke:

1. `"ab".find("z")`
2. `"ab".index("b")`
3. `len("ab")`
4. `"a,b".split(",")`

Ergebnisse:

- A) `1`
- B) `-1`
- C) `["a", "b"]`
- D) `2`

### Frage 19 · Code ergänzen · Block 3 · Ziel 3.1 · 4 Punkte

Ergänze den Namen, der eine neue sortierte Liste liefert und `werte` bei `[3, 1, 2]` lässt.

```python
werte = [3, 1, 2]
neu = ___(werte)
```

### Frage 20 · Einzelauswahl · Block 3 · Ziel 3.3 · 3 Punkte

`buch = {"a": 1}`. Welchen Wert hat der Ausdruck `1 in buch`?

- A) `True`
- B) `False`
- C) `1`
- D) `KeyError`

### Frage 21 · Lückentext · Block 3 · Ziel 3.4 · 4 Punkte

`"Hallo"[1:4]` ergibt den String ___. Schreibe nur die drei Zeichen.

### Frage 22 · Mehrfachauswahl · Block 3 · Ziel 3.1 · 3 Punkte

`a = [1, 2]` und danach eine der Zuweisungen. Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) Nach `b = a` sind `a` und `b` zwei Namen desselben Listenobjekts.
- B) Nach `b = a[:]` ist `b` eine neue Liste.
- C) `b = a[:]` kopiert verschachtelte Listen immer vollständig getrennt.
- D) Wenn `b = a` gilt, sieht man `a.append(3)` auch über `b`.

### Frage 23 · Einzelauswahl · Block 4 · Ziel 4.1 · 4 Punkte

Eine Funktion enthält keine `return`-Anweisung. Was liefert der Aufruf?

- A) `0`
- B) `False`
- C) `None`
- D) einen leeren String

### Frage 24 · Code einsetzen · Block 4 · Ziel 4.1 · 3 Punkte

Welche Zeile schließt die Rekursion korrekt ab, sodass `summe_bis(3)` den Wert `6` hat?

```python
def summe_bis(n):
    if n <= 0:
        ___
    return n + summe_bis(n - 1)
```

- A) `return 0`
- B) `return n`
- C) `pass`
- D) `yield n`

### Frage 25 · Mehrfachauswahl · Block 4 · Ziel 4.2 · 4 Punkte

```python
x = 1

def f():
    x = 2
    return x
```

Welche Aussagen stimmen? Wähle alle zutreffenden Antworten.

- A) `f()` gibt `2` zurück.
- B) Das äußere `x` wird `2`.
- C) Das äußere `x` bleibt `1`.
- D) Der Aufruf wirft `UnboundLocalError`.

### Frage 26 · Sortieren · Block 4 · Ziel 4.3 · 3 Punkte

Ordne von der Wurzel hinunter zu `IndexError`. Gib die Buchstaben in dieser Reihenfolge an.

- A) `LookupError`
- B) `BaseException`
- C) `IndexError`
- D) `Exception`

### Frage 27 · Lückentext · Block 4 · Ziel 4.3 · 4 Punkte

`int("1.5")` wirft ___. Schreibe den Ausnahmenamen.

### Frage 28 · Einzelauswahl · Block 4 · Ziel 4.3 · 3 Punkte

Fängt `except Exception` ein `KeyboardInterrupt`?

- A) Ja, weil jede Ausnahme unter `Exception` hängt.
- B) Nein, `KeyboardInterrupt` hängt direkt unter `BaseException`.
- C) Nur wenn zusätzlich `finally` steht.
- D) Nur innerhalb von `input()`.

### Frage 29 · Code ergänzen · Block 4 · Ziel 4.4 · 4 Punkte

Ergänze den Ausnahmenamen, sodass `sicher(1, 0)` den Wert `None` liefert.

```python
def sicher(a, b):
    try:
        return a / b
    except ___:
        return None
```

### Frage 30 · Mehrfachauswahl · Block 4 · Ziel 4.1 · 3 Punkte

Welche Aussagen über Generatoren stimmen? Wähle alle zutreffenden Antworten.

- A) Eine Funktion mit `yield` liefert beim Aufruf ein Generator-Objekt.
- B) Der Funktionskörper läuft beim Aufruf vollständig, noch vor dem ersten `yield`.
- C) `list(...)` über den Generator sammelt die mit `yield` gelieferten Werte.
- D) `yield` ist ein Schlüsselwort.

## Abgabe

Punkte: ____ / 100. Bestanden ab 70.

-----

# Lösungsteil

Erst nach der Abgabe lesen.

### Frage 1

**Antwort:** B

**Erklärung:** Im Syllabus führt der Interpreter aus, der Compiler übersetzt vor dem Lauf.

### Frage 2

**Antwort:** C

**Erklärung:** `elif` ist reserviert. `print` und `main` sind gewöhnliche Namen.

### Frage 3

**Antwort:** A, C

**Erklärung:** Wissenschaftliche Schreibweise und `1.0` sind `float`. `4` ist `int`, `"3.0"` ist `str`.

### Frage 4

**Antwort:** 16

**Erklärung:** `0x10` ist eine Sechzehn, nicht die Dezimalzahl 10.

### Frage 5

**Antwort:** B

**Erklärung:** `**` bindet nach rechts: `2 ** (3 ** 2)` ist `512`.

### Frage 6

**Antwort:** `//`

**Erklärung:** `7 // 2` ist `3`. `7 / 2` wäre `3.5`.

### Frage 7

**Antwort:** B

**Erklärung:** `print` schreibt auf die Konsole und gibt `None` zurück.

### Frage 8

**Antwort:** C

**Erklärung:** Zwei getrennte `if` können beide laufen. `5` erfüllt beide Bedingungen.

### Frage 9

**Antwort:** A, C

**Erklärung:** `elif` und `else` brauchen ein vorheriges `if` und stehen danach.

### Frage 10

**Antwort:** B

**Erklärung:** 80 scheitert an `>= 90` und erfüllt das folgende `elif`.

### Frage 11

**Antwort:** B, D, C, A

**Erklärung:** `+` bindet enger als `not`, das enger als `and`, das enger als `or`.

### Frage 12

**Antwort:** B

**Erklärung:** Die Folge ist `1, 3, 5`. Die 6 gehört nicht dazu.

### Frage 13

**Antwort:** B

**Erklärung:** `n` muss sinken, sonst bleibt die Bedingung wahr. `3+2+1` ist `6`.

### Frage 14

**Antwort:** A, C

**Erklärung:** Schleifen-`else` bedeutet „kein `break`“, nicht „Körper war leer“.

### Frage 15

**Antwort:** 4

**Erklärung:** `0, 1, 2, 3`.

### Frage 16

**Antwort:** C

**Erklärung:** `-1` ist das letzte Element.

### Frage 17

**Antwort:** B, C

**Erklärung:** `(1)` ist nur die Zahl 1. Ein Tupel-Index lässt sich nicht neu zuweisen.

### Frage 18

**Antwort:** 1–B, 2–A, 3–D, 4–C

**Erklärung:** `find` liefert `-1`, `index` die Position `1`, `len` die `2`, `split` die Liste.

### Frage 19

**Antwort:** `sorted`

**Erklärung:** `sorted` gibt eine neue Liste zurück. `list.sort` würde `None` liefern und die Quelle ändern.

### Frage 20

**Antwort:** B

**Erklärung:** `in` prüft bei einem Dictionary die Schlüssel, nicht die Werte.

### Frage 21

**Antwort:** all

**Erklärung:** Indizes 1, 2 und 3. Index 4 bleibt außen vor.

### Frage 22

**Antwort:** A, B, D

**Erklärung:** `[:]` ist eine flache Kopie. Innere Listen werden dabei nicht tief kopiert.

### Frage 23

**Antwort:** C

**Erklärung:** Ohne `return` ist das Funktionsergebnis `None`.

### Frage 24

**Antwort:** A

**Erklärung:** Der Abbruch muss `0` liefern, sonst fehlt die Basis oder die Rekursion geht weiter.

### Frage 25

**Antwort:** A, C

**Erklärung:** Die Zuweisung `x = 2` erzeugt ein lokales `x` und lässt das äußere unberührt.

### Frage 26

**Antwort:** B, D, A, C

**Erklärung:** `BaseException`, dann `Exception`, dann `LookupError`, dann `IndexError`.

### Frage 27

**Antwort:** ValueError

**Erklärung:** `int` akzeptiert den Typ String, aber nicht den Inhalt `"1.5"`.

### Frage 28

**Antwort:** B

**Erklärung:** `KeyboardInterrupt` erbt nicht von `Exception`.

### Frage 29

**Antwort:** `ZeroDivisionError`

**Erklärung:** Genau diese Ausnahme entsteht bei der Division durch null.

### Frage 30

**Antwort:** A, C, D

**Erklärung:** Der Körper läuft erst bei der Iteration bis zum nächsten `yield`, nicht vollständig beim bloßen Aufruf.
