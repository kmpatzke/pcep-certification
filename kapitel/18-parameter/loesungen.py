"""Lösungen zu Kapitel 18. Ausführen: python3 loesungen.py"""

stand = 0


def addiere(a, b):
    return a + b


def gruss(name, zeichen="!"):
    return "Hallo " + name + zeichen


def sammeln(wert, folge=None):
    if folge is None:
        folge = []
    folge.append(wert)
    return folge


def lokal():
    x = 1
    x = 2
    return x


def setzen(wert):
    global stand
    stand = wert


def pruefe():
    assert addiere(1, 2) == 3
    assert addiere(a=2, b=5) == 7
    assert gruss("Ada") == "Hallo Ada!"
    assert gruss("Ada", "?") == "Hallo Ada?"
    erster = sammeln(1)
    zweiter = sammeln(2)
    assert erster == [1]
    assert zweiter == [2]
    assert lokal() == 2
    setzen(5)
    assert stand == 5
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
