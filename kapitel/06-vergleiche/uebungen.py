"""Übungen zu Kapitel 06 (Syllabus 1.4, Vergleiche und Bool)."""


# Aufgabe 1
# Erwartetes Verhalten:
#   gleich(3, 3) ist True
#   gleich(3, 3.0) ist True
#   ungleich("a", "b") ist True
def gleich(a, b):
    # TODO
    pass


def ungleich(a, b):
    # TODO
    pass


# Aufgabe 2
# Kettenvergleich, nicht die geklammerte Form.
# Erwartetes Verhalten:
#   kette() ist True          # 1 < 2 < 3
#   kette_falsch() ist False  # 3 < 2 < 1
#   geklammert() ist True     # (3 < 2) < 1
def kette():
    # TODO
    pass


def kette_falsch():
    # TODO
    pass


def geklammert():
    # TODO
    pass


# Aufgabe 3
# and/or geben den entscheidenden Operanden zurück, nicht zwingend bool.
# Erwartetes Verhalten:
#   und_oder() == (2, 0, 5, 3)
#   als Tupel: 1 and 2, 0 and 2, 0 or 5, 3 or 5
def und_oder():
    # TODO
    pass


# Aufgabe 4
# Erwartetes Verhalten:
#   negation(0) ist True
#   negation("0") ist False
#   negation([]) ist True
#   negation([0]) ist False
def negation(wert):
    # TODO
    pass


# Aufgabe 5
# Priorität: not vor and vor or.
# Erwartetes Verhalten: prioritaet() ist True
# Ausdruck: True or False and False
def prioritaet():
    # TODO
    pass
