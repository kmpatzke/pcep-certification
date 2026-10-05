"""Übungen zu Kapitel 02 (Syllabus 1.2).

Lies lerntext.md. Ersetze pass durch deinen Code.
"""

import keyword


# Aufgabe 1
# True, wenn wort ein Python-Schlüsselwort ist, sonst False.
# Groß- und Kleinschreibung beachten.
# Erwartetes Verhalten:
#   ist_schluesselwort("for") ist True
#   ist_schluesselwort("For") ist False
#   ist_schluesselwort("summe") ist False
def ist_schluesselwort(wort):
    # TODO
    pass


# Aufgabe 2
# Gib die Einrückungstiefe als Anzahl Leerzeichen zurück.
# Der Block unter if soll 4 Leerzeichen haben, der innere Block 8.
# Baue das so, dass tiefe(0) == 0, tiefe(1) == 4, tiefe(2) == 8.
# Erwartetes Verhalten: tiefe(0) == 0, tiefe(1) == 4, tiefe(2) == 8
def tiefe(ebene):
    # TODO
    pass


# Aufgabe 3
# Wert von x nach diesem Ablauf: x startet bei 1.
# Die Zeile, die x auf 99 setzen würde, ist ein Kommentar und zählt nicht.
# Danach wird 4 addiert.
# Erwartetes Verhalten: wert_nach_kommentar() == 5
def wert_nach_kommentar():
    # TODO
    pass


# Aufgabe 4
# True, wenn der Name als Variable erlaubt ist.
# Verboten: Schlüsselwörter und der leere String.
# Erlaubt in dieser Aufgabe: "summe", "_x", "wert2"
# Verboten: "if", "None", ""
# Erwartetes Verhalten siehe die drei Gruppen oben.
def name_erlaubt(name):
    # TODO
    pass


# Aufgabe 5
# Welche print-Aufrufe gehören zum if-Block?
# Gegeben ist die gedachte Struktur:
#   zeile = "ausserhalb"
#   if True:
#       zeile = "innen"
#   # hier kein else
# Gib den Wert zurück, den zeile nach dem if hat, wenn die Bedingung True ist.
# Erwartetes Verhalten: nach_if(True) == "innen"
# Erwartetes Verhalten: nach_if(False) == "ausserhalb"
def nach_if(bedingung):
    # TODO
    pass
