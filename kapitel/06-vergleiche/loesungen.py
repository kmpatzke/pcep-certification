"""Lösungen zu Kapitel 06. Ausführen: python3 loesungen.py"""


def gleich(a, b):
    return a == b


def ungleich(a, b):
    return a != b


def kette():
    return 1 < 2 < 3


def kette_falsch():
    return 3 < 2 < 1


def geklammert():
    # False < 1, und False entspricht 0.
    return (3 < 2) < 1


def und_oder():
    return (1 and 2, 0 and 2, 0 or 5, 3 or 5)


def negation(wert):
    return not wert


def prioritaet():
    return True or False and False


def pruefe():
    assert gleich(3, 3) is True
    assert gleich(3, 3.0) is True
    assert ungleich("a", "b") is True
    assert kette() is True
    assert kette_falsch() is False
    assert geklammert() is True
    assert und_oder() == (2, 0, 5, 3)
    assert negation(0) is True
    assert negation("0") is False
    assert negation([]) is True
    assert negation([0]) is False
    assert prioritaet() is True
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
