# 3.4 Strings

Ein String ist eine unveränderbare Folge von Zeichen.

```python
s = "Hallo"
t = 'Hallo'
mehrzeilig = """Zeile 1
Zeile 2"""
```

Einfache und doppelte Anführungszeichen sind gleichwertig. Steht ein Apostroph im Text, nimm doppelte Anführungszeichen, oder umgekehrt:

```python
"Ada's Buch"
'Er sagte "ja"'
```

## Escape

Ein Backslash leitet ein Sonderzeichen ein.

```python
"a\nb"      # a, Zeilenumbruch, b
"a\tb"      # Tab
"a\\b"      # a, ein Backslash, b
"\""        # ein doppeltes Anführungszeichen
```

Häufige Folgen: `\n` Zeilenumbruch, `\t` Tab, `\\` Backslash, `\'` und `\"` das jeweilige Anführungszeichen.

## Index, Slice, Unveränderbarkeit

```python
"Hallo"[0]      # "H"
"Hallo"[-1]     # "o"
"Hallo"[1:4]    # "all"
len("ab")       # 2
"a" in "ab"     # True
```

`s[0] = "h"` wirft `TypeError`. Methoden und `+` bauen einen **neuen** String.

```python
s = "ab"
s = s + "c"     # s zeigt auf den neuen String "abc"
```

## Grundlegende Methoden

Der Syllabus sagt „basic string functions and methods“ und zählt sie nicht einzeln auf. Diese hier reichen für den Einstieg und für die Aufgaben:

```python
"Ab".lower()           # "ab"
"ab".upper()           # "AB"
"  ab ".strip()        # "ab"
"ab".find("b")         # 1
"ab".find("z")         # -1
"ab".index("b")        # 1
"ab".index("z")        # ValueError
"aba".count("a")       # 2
"ab".replace("a", "x") # "xb"
"a,b".split(",")       # ["a", "b"]
",".join(["a", "b"])   # "a,b"
"ab".startswith("a")   # True
"ab".endswith("b")     # True
"12".isdigit()         # True
"ab".isalpha()         # True
```

`len` ist eine Funktion, keine Methode: `len(s)`, nicht `s.len()`.

`find` liefert `-1`, wenn nichts da ist. `index` wirft `ValueError`. Dieselbe Unterscheidung gibt es bei Listen.

## Prüfungsfallen

- Strings sind unveränderbar. Jede „Änderung“ ist ein neuer String.
- `s[1:4]` enthält Index 4 nicht.
- `"abc"[::-1]` ist `"cba"`.
- `+` zwischen String und Zahl ist `TypeError` (Kapitel 05).
- Ein Slice außerhalb der Länge wirft nicht. Ein Index außerhalb wirft `IndexError`.
- `"""` beginnt einen mehrzeiligen String, keinen Kommentar.
