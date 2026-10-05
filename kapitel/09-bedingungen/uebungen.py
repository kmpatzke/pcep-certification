"""Übungen zu Kapitel 09 (Syllabus 2.1)."""


# Aufgabe 1
# 1 -> "sehr gut", 2 -> "gut", 3 -> "befriedigend", sonst "andere".
# Erwartetes Verhalten:
#   bewertung(1) == "sehr gut"
#   bewertung(2) == "gut"
#   bewertung(4) == "andere"
def bewertung(note):
    # TODO
    pass


# Aufgabe 2
# Zwei unabhängige ifs, nicht elif.
# x > 0 hängt "a" an, x > 3 hängt "b" an. Start ist "".
# Erwartetes Verhalten:
#   zwei_ifs(5) == "ab"
#   zwei_ifs(1) == "a"
#   zwei_ifs(-1) == ""
def zwei_ifs(x):
    # TODO
    pass


# Aufgabe 3
# Dieselbe Logik mit elif. Der zweite Zweig läuft nur, wenn der erste falsch ist.
# Erwartetes Verhalten:
#   mit_elif(5) == "a"
#   mit_elif(-1) == ""
def mit_elif(x):
    # TODO
    pass


# Aufgabe 4
# Verschachtelt: unter 18 -> "nein".
# Ab 18 mit karte True -> "ja", sonst "ausweis_fehlt".
# Erwartetes Verhalten:
#   eintritt(17, True) == "nein"
#   eintritt(20, True) == "ja"
#   eintritt(20, False) == "ausweis_fehlt"
def eintritt(alter, karte):
    # TODO
    pass


# Aufgabe 5
# Leerer String ist falsch. None ebenfalls.
# Erwartetes Verhalten:
#   gruss("") == "unbekannt"
#   gruss("Ada") == "Ada"
def gruss(name):
    # TODO
    pass
