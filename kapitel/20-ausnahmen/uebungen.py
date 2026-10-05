"""Übungen zu Kapitel 20 (Syllabus 4.4)."""


# Aufgabe 1
# a / b, bei ZeroDivisionError None.
# Erwartetes Verhalten:
#   sicher(6, 2) == 3.0
#   sicher(1, 0) is None
def sicher(a, b):
    # TODO
    pass


# Aufgabe 2
# int(text). ValueError -> "wert". Andere Exception -> "sonst".
# ArithmeticError fängt diesen Fall nicht.
# Erwartetes Verhalten:
#   art("12") == "ok"
#   art("x") == "wert"
def art(text):
    # TODO
    pass


# Aufgabe 3
# innen teilt durch null und fängt nichts.
# aussen fängt ZeroDivisionError und gibt None zurück.
# Erwartetes Verhalten: aussen(0) is None und aussen(2) == 0.5
def innen(b):
    # TODO
    pass


def aussen(b):
    # TODO
    pass


# Aufgabe 4
# Wirf ValueError, wenn n < 0. Sonst n zurückgeben.
# Erwartetes Verhalten: pruefe(2) == 2
# pruefe(-1) wirft ValueError
def pruefe(n):
    # TODO
    pass


# Aufgabe 5
# Fange ValueError, setze gesehen auf True und wirf dieselbe Ausnahme weiter.
# Erwartetes Verhalten: weiter(True) wirft ValueError, und gesehen ist danach True.
gesehen = False


def weiter(ausloesen):
    # TODO
    pass
