"""Lösungen zu Kapitel 17. Ausführen: python3 loesungen.py"""


def flaeche(a, b):
    return a * b


def ohne_return():
    x = 1
    # absichtlich kein return: das Ergebnis ist None
    return


def vorzeichen(n):
    if n > 0:
        return "plus"
    if n < 0:
        return "minus"
    return "null"


def summe_bis(n):
    if n <= 0:
        return 0
    return n + summe_bis(n - 1)


def zaehle(n):
    i = 0
    while i < n:
        yield i
        i += 1


def pruefe():
    assert flaeche(2, 3) == 6
    assert ohne_return() is None
    assert vorzeichen(2) == "plus"
    assert vorzeichen(-2) == "minus"
    assert vorzeichen(0) == "null"
    assert summe_bis(3) == 6
    assert summe_bis(0) == 0
    assert list(zaehle(3)) == [0, 1, 2]
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
