"""Übungen zu Kapitel 03 (Syllabus 1.3, ohne Zahlensysteme)."""


# Aufgabe 1
# Gib den Python-Typnamen zurück: "bool", "int", "float" oder "str".
# Erwartetes Verhalten:
#   typname(True) == "bool"
#   typname(4) == "int"
#   typname(2e3) == "float"
#   typname("4") == "str"
def typname(wert):
    # TODO
    pass


# Aufgabe 2
# Werte das Literal aus und gib die Zahl zurück.
# Erwartetes Verhalten:
#   wissenschaftlich("2e3") == 2000.0
#   wissenschaftlich("1.5e-1") == 0.15
#   wissenschaftlich("4E2") == 400.0
def wissenschaftlich(literal):
    # TODO
    pass


# Aufgabe 3
# True, wenn name nach den Syntaxregeln ein Bezeichner sein kann
# und kein Schlüsselwort ist.
# Erwartetes Verhalten:
#   name_gueltig("alter") ist True
#   name_gueltig("_privat") ist True
#   name_gueltig("2alter") ist False
#   name_gueltig("for") ist False
#   name_gueltig("") ist False
def name_gueltig(name):
    # TODO
    pass


# Aufgabe 4
# Wandle einen camelCase-Namen in snake_case um.
# Nur dieser einfache Fall: ein Großbuchstabe in der Mitte, keine Ziffern.
# Erwartetes Verhalten:
#   nach_pep8("flaecheKreis") == "flaeche_kreis"
#   nach_pep8("alter") == "alter"
def nach_pep8(name):
    # TODO
    pass


# Aufgabe 5
# Binde nacheinander neu und gib das Endergebnis zurück.
# Start: wert = 10. Dann wert = wert + 5. Dann wert = "ok", wenn wert > 12, sonst "klein".
# Erwartetes Verhalten: endwert() == "ok"
def endwert():
    # TODO
    pass
