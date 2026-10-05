"""Übungen zu Kapitel 04 (Syllabus 1.3, Zahlensysteme)."""


# Aufgabe 1
# Dezimalwert der drei Literale.
# Erwartetes Verhalten:
#   dezimal_von_literal("0b1010") == 10
#   dezimal_von_literal("0o17") == 15
#   dezimal_von_literal("0xFF") == 255
def dezimal_von_literal(text):
    # TODO
    pass


# Aufgabe 2
# String mit Präfix, wie bin/oct/hex ihn liefern.
# Erwartetes Verhalten:
#   als_bin(10) == "0b1010"
#   als_oct(15) == "0o17"
#   als_hex(255) == "0xff"
def als_bin(zahl):
    # TODO
    pass


def als_oct(zahl):
    # TODO
    pass


def als_hex(zahl):
    # TODO
    pass


# Aufgabe 3
# Lies einen String ohne Präfix in der gegebenen Basis.
# Erwartetes Verhalten:
#   aus_basis("1010", 2) == 10
#   aus_basis("17", 8) == 15
#   aus_basis("ff", 16) == 255
def aus_basis(text, basis):
    # TODO
    pass


# Aufgabe 4
# True, wenn das Literal-Präfix zur Basis passt.
# Erwartetes Verhalten:
#   praefix_passt("0b101", 2) ist True
#   praefix_passt("0x10", 16) ist True
#   praefix_passt("0o7", 2) ist False
def praefix_passt(literal, basis):
    # TODO
    pass


# Aufgabe 5
# 0x10 ist nicht die Dezimalzahl 10. Gib den echten int-Wert zurück.
# Erwartetes Verhalten: hex_zehn() == 16
def hex_zehn():
    # TODO
    pass
