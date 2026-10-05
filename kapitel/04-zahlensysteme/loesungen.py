"""Lösungen zu Kapitel 04. Ausführen: python3 loesungen.py"""


def dezimal_von_literal(text):
    return int(text, 0)


def als_bin(zahl):
    return bin(zahl)


def als_oct(zahl):
    return oct(zahl)


def als_hex(zahl):
    return hex(zahl)


def aus_basis(text, basis):
    return int(text, basis)


def praefix_passt(literal, basis):
    zuordnung = {"0b": 2, "0B": 2, "0o": 8, "0O": 8, "0x": 16, "0X": 16}
    return zuordnung.get(literal[:2]) == basis


def hex_zehn():
    return 0x10


def pruefe():
    assert dezimal_von_literal("0b1010") == 10
    assert dezimal_von_literal("0o17") == 15
    assert dezimal_von_literal("0xFF") == 255
    assert als_bin(10) == "0b1010"
    assert als_oct(15) == "0o17"
    assert als_hex(255) == "0xff"
    assert aus_basis("1010", 2) == 10
    assert aus_basis("17", 8) == 15
    assert aus_basis("ff", 16) == 255
    assert praefix_passt("0b101", 2) is True
    assert praefix_passt("0x10", 16) is True
    assert praefix_passt("0o7", 2) is False
    assert hex_zehn() == 16
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
