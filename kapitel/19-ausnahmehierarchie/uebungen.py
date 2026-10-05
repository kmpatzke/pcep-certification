"""Übungen zu Kapitel 19 (Syllabus 4.3)."""


# Aufgabe 1
# Name der direkten Syllabus-Oberklasse als String.
# Erwartetes Verhalten:
#   oberklasse("IndexError") == "LookupError"
#   oberklasse("KeyError") == "LookupError"
#   oberklasse("ZeroDivisionError") == "ArithmeticError"
#   oberklasse("KeyboardInterrupt") == "BaseException"
def oberklasse(name):
    # TODO
    pass


# Aufgabe 2
# True, wenn ein except Exception diesen Typ fängt.
# Erwartetes Verhalten:
#   faengt_exception("ValueError") ist True
#   faengt_exception("KeyboardInterrupt") ist False
#   faengt_exception("SystemExit") ist False
def faengt_exception(name):
    # TODO
    pass


# Aufgabe 3
# Welcher Fehlertyp entsteht? Gib den Klassennamen zurück.
# "division", "index", "schluessel", "plus", "inttext"
# Erwartetes Verhalten:
#   fehlerart("division") == "ZeroDivisionError"
#   fehlerart("index") == "IndexError"
#   fehlerart("schluessel") == "KeyError"
#   fehlerart("plus") == "TypeError"
#   fehlerart("inttext") == "ValueError"
def fehlerart(situation):
    # TODO
    pass


# Aufgabe 4
# True, wenn der Typ unter der abstrakten Ausnahme LookupError liegt.
# Erwartetes Verhalten:
#   ist_lookup("IndexError") ist True
#   ist_lookup("TypeError") ist False
def ist_lookup(name):
    # TODO
    pass


# Aufgabe 5
# IndexError und KeyError sind nicht voneinander abgeleitet.
# Erwartetes Verhalten: gleicher_zweig() ist False
def gleicher_zweig():
    # TODO
    # True nur, wenn IndexError eine Unterklasse von KeyError wäre
    # oder umgekehrt. Das ist sie nicht.
    pass
