"""Lösungen zu Kapitel 05. Ausführen: python3 loesungen.py"""


def potenz_kette():
    # ** bindet nach rechts: 2 ** (3 ** 2) == 512
    return 2 ** 3 ** 2


def gemischt():
    return 2 + 3 * 4


def division():
    return 7 / 2


def ganzzahlig():
    return 7 // 2


def neg_div():
    # Richtung minus unendlich, nicht zur Null.
    return -7 // 2


def neg_rest():
    return -7 % 2


def verknuepfen():
    return "ab" + "c"


def wiederholen():
    return "ab" * 3


def kurzformen():
    x = 10
    x += 2
    x //= 3
    x **= 2
    return x


def fast_gleich(a, b):
    return abs(a - b) < 1e-9


def pruefe():
    assert potenz_kette() == 512
    assert gemischt() == 14
    assert division() == 3.5
    assert ganzzahlig() == 3
    assert neg_div() == -4
    assert neg_rest() == 1
    assert verknuepfen() == "abc"
    assert wiederholen() == "ababab"
    assert kurzformen() == 16
    assert fast_gleich(0.1 + 0.2, 0.3) is True
    assert fast_gleich(1.0, 2.0) is False
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
