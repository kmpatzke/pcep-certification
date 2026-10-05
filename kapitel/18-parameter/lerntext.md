# 4.2 Parameter, Argumente, Gültigkeit, `global`

## Parameter und Argumente

Parameter stehen in der Definition. Argumente stehen im Aufruf.

```python
def addiere(a, b):    # a und b sind Parameter
    return a + b

addiere(1, 2)         # 1 und 2 sind Argumente
```

Drei Arten, die der Syllabus nennt:

- positional: `addiere(1, 2)` — die Reihenfolge zählt
- Schlüsselwort: `addiere(b=2, a=1)` — die Namen zählen, die Reihenfolge nicht
- gemischt: `addiere(1, b=2)` — positionale Argumente zuerst, danach Schlüsselwörter

`addiere(a=1, 2)` ist ein Syntaxfehler. Ein positionales Argument darf nicht hinter einem Schlüsselwortargument stehen.

## Standardwerte

```python
def gruss(name, zeichen="!"):
    return "Hallo " + name + zeichen

gruss("Ada")         # "Hallo Ada!"
gruss("Ada", "?")    # "Hallo Ada?"
```

Parameter mit Standardwert stehen hinter Parametern ohne Standardwert. `def f(a=1, b)` ist ein Syntaxfehler.

Der Standardwert wird **einmal** erzeugt, beim Definieren der Funktion, nicht bei jedem Aufruf.

```python
def haenge_an(wert, folge=[]):
    folge.append(wert)
    return folge

haenge_an(1)    # [1]
haenge_an(2)    # [1, 2], dieselbe Liste
```

Für eine frische Liste je Aufruf nimm `None` als Standard und erzeuge die Liste im Körper:

```python
def haenge_an(wert, folge=None):
    if folge is None:
        folge = []
    folge.append(wert)
    return folge
```

## Gültigkeitsbereiche

Namen, die eine Funktion zuweist, sind lokal. Sie verdecken einen gleichnamigen Namen außen. Das heißt Verschattung (shadowing).

```python
x = 1

def aussen_unberuehrt():
    x = 2
    return x

aussen_unberuehrt()    # 2
# x außen ist weiter 1
```

Liest du einen Namen nur, sucht Python außen:

```python
x = 1

def lesen():
    return x
```

Weist du dem Namen irgendwo in der Funktion zu, ist er in der **ganzen** Funktion lokal. Dann ist ein Lesen davor ein `UnboundLocalError`:

```python
x = 1

def falle():
    print(x)    # UnboundLocalError
    x = 2
```

## `global`

`global x` meint den Namen auf Modul-Ebene, nicht einen lokalen.

```python
x = 1

def setzen():
    global x
    x = 2

setzen()
# x ist 2
```

`global` steht im Funktionskörper, bevor du den Namen benutzt. Es macht aus einer Zuweisung keine neue lokale Variable.

Parameter verdecken ebenfalls äußere Namen. Ein Parameter `x` ist lokal, auch wenn außen ein `x` liegt.

## Prüfungsfallen

- Schlüsselwortargumente stehen nach den positionalen.
- Der Default einer Liste wird wiederverwendet.
- Eine Zuweisung irgendwo in der Funktion macht den Namen lokal, auch in Zeilen davor.
- Ohne `global` ändert eine Zuweisung die äußere Variable nicht.
- `global` ist kein Typ und kein Wert. Es ist eine Anweisung über einen Namen.
