# 1.5 Eingabe und Ausgabe

`print` schreibt auf die Konsole. `input` liest eine Zeile und liefert immer einen String.

## `print`

```python
print("Hallo")
print(1, 2, 3)            # 1 2 3 und danach Zeilenumbruch
print(1, 2, sep="-")      # 1-2
print(1, 2, end="!")      # 1 2!
print(1, 2, sep="", end="")
```

- `sep` steht zwischen den Argumenten. Standard ist ein Leerzeichen.
- `end` steht nach dem letzten Argument. Standard ist ein Zeilenumbruch `"\n"`.
- `print()` ohne Argumente schreibt nur den Zeilenumbruch.
- `print` gibt `None` zurück. Wer `x = print(1)` schreibt, hat danach `x is None`.

`sep` und `end` sind Schlüsselwortargumente. `print(1, 2, "-")` setzt kein Trennzeichen. Das dritte Argument wird mit ausgegeben: `1 2 -`.

## `input`

```python
name = input()
name = input("Name: ")
```

Der optionale Text ist die Eingabeaufforderung. Der Rückgabewert enthält **nicht** das Zeilenende und ist immer `str`. Tippt jemand `42`, ist das Ergebnis `"42"`, nicht die Zahl `42`.

```python
alter = int(input())
preis = float(input())
```

`int` und `float` stehen im Syllabus bei der Ein- und Ausgabe genau dafür. Was sie sonst tun, steht in Kapitel 07. Ein leeres Enter oder der Text `abc` führt bei `int(input())` zu `ValueError`.

## Eine Zeile nachbauen

In den Übungen gibt es kein echtes Terminal. Die Funktion soll denselben String liefern, den `print` schreiben würde, **ohne** den abschließenden Standard-Zeilenumbruch, wenn `end` den Umbruch ersetzt. Beispiel: `print(1, 2, sep="-", end="!")` schreibt die Zeichen `1-2!`.

```python
def zeile(a, b):
    return str(a) + "-" + str(b) + "!"
```

`print` wandelt die Argumente mit `str` um.

## Prüfungsfallen

- `input` liefert nie von allein einen `int`.
- `sep` und `end` müssen benannt werden.
- Das Komma in `print(1, 2)` ist kein Plus. Es fügt das Trennzeichen ein.
- `print(1 + 2)` gibt `3` aus. `print(1, 2)` gibt `1 2` aus.
- Der Rückgabewert von `print` ist `None`, nicht der gedruckte Text.
