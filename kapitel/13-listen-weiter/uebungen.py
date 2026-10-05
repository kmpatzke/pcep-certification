"""Übungen zu Kapitel 13 (Syllabus 3.1, Methoden und Kopien)."""


# Aufgabe 1
# Baue [9, 1, 2, 3] aus [1, 2]: erst 3 anhängen, dann 9 an Index 0.
# Erwartetes Verhalten: aufbauen() == [9, 1, 2, 3]
def aufbauen():
    # TODO
    pass


# Aufgabe 2
# Entferne den Wert 1 (nicht den Index 1) und danach den Index 0.
# Start: [9, 1, 2]
# Erwartetes Verhalten: entfernen() == [2]
def entfernen():
    # TODO
    pass


# Aufgabe 3
# Neue Liste, Quelle bleibt unverändert.
# Erwartetes Verhalten:
#   quadrate(4) == [0, 1, 4, 9]
#   sortiert([3, 1, 2]) == [1, 2, 3]
#   und die übergebene Liste von sortiert bleibt [3, 1, 2]
def quadrate(n):
    # TODO
    pass


def sortiert(werte):
    # TODO
    pass


# Aufgabe 4
# Echte zweite Liste, nicht nur ein zweiter Name.
# Erwartetes Verhalten:
#   kopiere([1, 2]) == [1, 2]
#   a is nicht das Ergebnis
def kopiere(werte):
    # TODO
    pass


# Aufgabe 5
# Drei getrennte Zeilen [0, 0]. Eine Änderung an [0][0] darf die anderen nicht treffen.
# Erwartetes Verhalten:
#   m = matrix()
#   m[0][0] = 1
#   m == [[1, 0], [0, 0], [0, 0]]
def matrix():
    # TODO
    pass
