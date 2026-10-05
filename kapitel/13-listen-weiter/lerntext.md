# 3.1 Listen verändern, Comprehensions, Kopien

## Methoden und `del`

```python
werte = [1, 2]
werte.append(3)        # [1, 2, 3], hängt ans Ende
werte.insert(0, 9)     # [9, 1, 2, 3], Index und Wert
werte.index(1)         # 1, erster Treffer, sonst ValueError
werte.remove(1)        # entfernt den ersten Wert 1, nicht den Index
del werte[0]           # entfernt nach Index
```

Weitere Methoden, die zur Gruppe „usw.“ gehören und in Aufgaben vorkommen:

```python
werte.pop()            # letztes Element entfernen und zurückgeben
werte.pop(0)           # Index entfernen und zurückgeben
werte.count(2)         # wie oft der Wert vorkommt
werte.extend([7, 8])   # jedes Element anhängen, nicht die Liste als ein Element
werte.reverse()        # dreht an Ort und Stelle, Ergebnis None
werte.sort()           # sortiert an Ort und Stelle, Ergebnis None
werte.clear()
```

`sorted(werte)` ist eine **Funktion**. Sie liefert eine neue Liste und lässt die alte in Ruhe. `werte.sort()` sortiert die vorhandene Liste und gibt `None` zurück.

`del werte[1:3]` löscht einen Slice. `del` ist eine Anweisung, keine Methode.

## Comprehensions

```python
quadrate = [n * n for n in range(4)]
# [0, 1, 4, 9]
gerade = [n for n in range(6) if n % 2 == 0]
# [0, 2, 4]
```

Links steht der neue Wert, dann `for`, optional `if`. Die Schleifenvariable bleibt in Python 3 nicht nach der Comprehension als normale Schleifenvariable liegen.

## Kopieren

```python
a = [1, 2, 3]
b = a
b.append(4)
# a ist auch [1, 2, 3, 4], weil a und b dasselbe Objekt sind

c = a[:]
d = a.copy()
d.append(5)
# a ändert sich dadurch nicht
```

`[:]` und `list.copy()` sind flache Kopien. Die neue Liste ist ein anderes Objekt. Die Elemente darin sind dieselben Objekte.

```python
matrix = [[0, 0], [0, 0]]
andere = matrix.copy()
andere[0].append(1)
# matrix[0] ist ebenfalls [0, 0, 1]
```

Eine tiefe Kopie brauchst du, wenn die Elemente selbst Listen sind: `[zeile[:] for zeile in matrix]`.

Die Falle beim Aufbau:

```python
falsch = [[0] * 2] * 3
# drei Namen für dieselbe innere Liste
falsch[0][0] = 1
# [[1, 0], [1, 0], [1, 0]]

richtig = [[0, 0] for _ in range(3)]
```

`[0] * 2` ist ungefährlich, weil Zahlen nicht an Ort und Stelle verändert werden. `[[0] * 2] * 3` vervielfacht die **Referenz** auf die innere Liste.

## Prüfungsfallen

- `append` gibt `None` zurück, nicht die Liste. `werte = werte.append(1)` macht `werte` zu `None`.
- `sort` und `reverse` geben `None` zurück. `sorted` gibt die neue Liste zurück.
- `index` sucht den Wert und wirft `ValueError`, wenn er fehlt. Ein Indexzugriff wirft `IndexError`.
- `remove` sucht den Wert. `del` und `pop` arbeiten mit dem Index.
- `* ` auf Listen von Listen teilt die innere Liste.
