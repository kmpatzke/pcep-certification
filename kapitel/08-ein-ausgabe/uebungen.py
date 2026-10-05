"""Übungen zu Kapitel 08 (Syllabus 1.5).

input() blockiert hier nicht: der gelesene Text kommt als Argument.
"""


# Aufgabe 1
# Zeichenfolge, die print(a, b, sep="-", end="!") schreiben würde.
# Erwartetes Verhalten: formatierte_zeile(1, 2) == "1-2!"
def formatierte_zeile(a, b):
    # TODO
    pass


# Aufgabe 2
# print(a, b, c) mit den Standardwerten von sep und end,
# aber ohne den abschließenden Zeilenumbruch im Rückgabestring.
# Erwartetes Verhalten: standard_zeile(1, 2, 3) == "1 2 3"
def standard_zeile(a, b, c):
    # TODO
    pass


# Aufgabe 3
# Wie int(input()), wenn der Rohtext schon vorliegt.
# Erwartetes Verhalten:
#   lies_int("42") == 42
#   lies_int("  7") == 7
def lies_int(text):
    # TODO
    pass


# Aufgabe 4
# Wie float(input()).
# Erwartetes Verhalten: lies_float("1.5") == 1.5
def lies_float(text):
    # TODO
    pass


# Aufgabe 5
# print gibt None zurück. Die Funktion soll denselben Rückgabewert
# liefern, den ein Aufruf von print hätte, ohne wirklich zu drucken.
# Erwartetes Verhalten: rueckgabe_von_print() is None
def rueckgabe_von_print():
    # TODO
    pass
