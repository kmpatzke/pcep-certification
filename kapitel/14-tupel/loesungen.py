"""Lösungen zu Kapitel 14. Ausführen: python3 loesungen.py"""


def erster(werte):
    return werte[0]


def rest(werte):
    return werte[1:]


def laenge(werte):
    return len(werte)


def einzel(wert):
    return (wert,)


def innere_liste(huelle):
    huelle[0].append(2)
    return huelle


def anhaengen(links, rechts):
    return links + rechts


def ist_tupel(wert):
    return isinstance(wert, tuple)


def pruefe():
    assert erster((10, 20, 30)) == 10
    assert rest((10, 20, 30)) == (20, 30)
    assert laenge((10, 20)) == 2
    assert einzel(5) == (5,)
    assert type(einzel(5)).__name__ == "tuple"
    assert innere_liste(([1],)) == ([1, 2],)
    assert anhaengen((1,), (2,)) == (1, 2)
    assert ist_tupel((1, 2)) is True
    assert ist_tupel([1, 2]) is False
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
