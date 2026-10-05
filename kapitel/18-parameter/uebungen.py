"""Übungen zu Kapitel 18 (Syllabus 4.2)."""


# Aufgabe 1
# Positionale Reihenfolge a, dann b.
# Erwartetes Verhalten: addiere(1, 2) == 3
def addiere(a, b):
    # TODO
    pass


# Aufgabe 2
# Standardwert "!" für zeichen.
# Erwartetes Verhalten:
#   gruss("Ada") == "Hallo Ada!"
#   gruss("Ada", "?") == "Hallo Ada?"
def gruss(name, zeichen="!"):
    # TODO
    pass


# Aufgabe 3
# Frische Liste bei jedem Aufruf ohne zweites Argument.
# Erwartetes Verhalten:
#   erster = sammeln(1)
#   zweiter = sammeln(2)
#   erster == [1]
#   zweiter == [2]
def sammeln(wert, folge=None):
    # TODO
    pass


# Aufgabe 4
# Die Zuweisung bleibt lokal. Der übergebene Startwert der Außenwelt
# wird nicht verändert. Gib nur den lokalen Wert zurück.
# Erwartetes Verhalten: lokal() == 2
def lokal():
    # TODO
    x = 1
    # setze ein lokales x auf 2 und gib es zurück
    pass


# Aufgabe 5
# Ändere die Modulvariable stand über global.
# Erwartetes Verhalten:
#   setzen(5)
#   stand == 5
stand = 0


def setzen(wert):
    # TODO
    pass
