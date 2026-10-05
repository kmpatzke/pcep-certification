"""Lösungen zu Kapitel 07. Ausführen: python3 loesungen.py"""


def bits_und():
    return 5 & 3


def bits_oder():
    return 5 | 2


def bits_xor():
    return 5 ^ 1


def bits_not():
    return ~5


def schieben():
    return 5 << 1


def schieben_plus():
    return 1 << 2 + 1


def zu_int(wert):
    return int(wert)


def text_zu_float(text):
    return float(text)


def text_zu_int_ueber_float(text):
    return int(float(text))


def als_bool(wert):
    return bool(wert)


def pruefe():
    assert bits_und() == 1
    assert bits_oder() == 7
    assert bits_xor() == 4
    assert bits_not() == -6
    assert schieben() == 10
    assert schieben_plus() == 8
    assert zu_int(3.9) == 3
    assert zu_int(-3.9) == -3
    assert zu_int(True) == 1
    assert text_zu_float("1.5") == 1.5
    assert text_zu_int_ueber_float("1.5") == 1
    assert als_bool(0) is False
    assert als_bool("False") is True
    assert als_bool("") is False
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
