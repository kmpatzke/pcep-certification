"""Übungen zu Kapitel 14 (Syllabus 3.2)."""


# Aufgabe 1
# Erwartetes Verhalten:
#   erster((10, 20, 30)) == 10
#   rest((10, 20, 30)) == (20, 30)
#   laenge((10, 20)) == 2
def erster(werte):
    # TODO
    pass


def rest(werte):
    # TODO
    pass


def laenge(werte):
    # TODO
    pass


# Aufgabe 2
# Ein einelementiges Tupel. Die Klammern allein reichen nicht.
# Erwartetes Verhalten:
#   einzel(5) == (5,)
#   type(einzel(5)).__name__ == "tuple"
def einzel(wert):
    # TODO
    pass


# Aufgabe 3
# Hänge an die Liste im Tupel an, ohne das Tupel neu zu bauen.
# Erwartetes Verhalten: innere_liste(([1],)) == ([1, 2],)
def innere_liste(huelle):
    # TODO
    pass


# Aufgabe 4
# Neues Tupel, Quelle bleibt.
# Erwartetes Verhalten: anhaengen((1,), (2,)) == (1, 2)
def anhaengen(links, rechts):
    # TODO
    pass


# Aufgabe 5
# True, wenn der Wert ein Tupel ist, False bei einer Liste.
# Erwartetes Verhalten:
#   ist_tupel((1, 2)) ist True
#   ist_tupel([1, 2]) ist False
def ist_tupel(wert):
    # TODO
    pass
