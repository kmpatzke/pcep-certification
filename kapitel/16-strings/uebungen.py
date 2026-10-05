"""Übungen zu Kapitel 16 (Syllabus 3.4)."""


# Aufgabe 1
# Erwartetes Verhalten:
#   anfang("Hallo") == "H"
#   ende("Hallo") == "o"
#   ausschnitt("Hallo") == "all"    # Index 1 bis vor 4
def anfang(text):
    # TODO
    pass


def ende(text):
    # TODO
    pass


def ausschnitt(text):
    # TODO
    pass


# Aufgabe 2
# Rückwärts, ohne die Quelle zu verändern. Die Quelle ist ohnehin unveränderbar.
# Erwartetes Verhalten: rueckwaerts("abc") == "cba"
def rueckwaerts(text):
    # TODO
    pass


# Aufgabe 3
# Erwartetes Verhalten:
#   normalisiert("  Ab ") == "ab"
#   position("ab", "b") == 1
#   position("ab", "z") == -1
def normalisiert(text):
    # TODO
    pass


def position(text, suche):
    # TODO
    # find, nicht index: fehlende Treffer werden -1
    pass


# Aufgabe 4
# Erwartetes Verhalten:
#   teilen("a,b") == ["a", "b"]
#   verbinden(["a", "b"]) == "a,b"
def teilen(text):
    # TODO
    pass


def verbinden(teile):
    # TODO
    pass


# Aufgabe 5
# Ein String mit einem Zeilenumbruch zwischen den beiden Wörtern.
# Erwartetes Verhalten: zwei_zeilen() == "oben\nunten"
def zwei_zeilen():
    # TODO
    pass
