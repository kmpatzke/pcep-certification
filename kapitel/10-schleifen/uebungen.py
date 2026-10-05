"""Übungen zu Kapitel 10 (Syllabus 2.2, ohne break/continue/else)."""


# Aufgabe 1
# Summe 1 + 2 + ... + n mit while. n >= 0.
# Erwartetes Verhalten: summe_while(4) == 10
def summe_while(n):
    # TODO
    pass


# Aufgabe 2
# Dieselbe Summe mit for und range. range-Stopp nicht mitzählen.
# Erwartetes Verhalten: summe_for(4) == 10
def summe_for(n):
    # TODO
    pass


# Aufgabe 3
# Liste der Zahlen, die range erzeugen würde.
# Erwartetes Verhalten:
#   zahlen(3) == [0, 1, 2]
#   zahlen_schritt() == [1, 3, 5]
#   zahlen_rueck() == [5, 4, 3, 2]
def zahlen(n):
    # TODO
    pass


def zahlen_schritt():
    # TODO
    # range(1, 6, 2)
    pass


def zahlen_rueck():
    # TODO
    # range(5, 1, -1)
    pass


# Aufgabe 4
# Baue einen String, in dem jedes Zeichen aus text doppelt vorkommt.
# Nur Schleife und +=, wie im Lerntext.
# Erwartetes Verhalten: verdoppelt("ab") == "aabb"
def verdoppelt(text):
    # TODO
    pass


# Aufgabe 5
# Der Zweig ist absichtlich leer. Gib den Startwert unverändert zurück,
# wenn die Bedingung wahr ist. Sonst gib start + 1 zurück.
# Erwartetes Verhalten:
#   mit_pass(True, 5) == 5
#   mit_pass(False, 5) == 6
def mit_pass(leer, start):
    # TODO
    pass
