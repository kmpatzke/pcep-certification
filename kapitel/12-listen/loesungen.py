"""Lösungen zu Kapitel 12. Ausführen: python3 loesungen.py"""


def erstes(werte):
    return werte[0]


def letztes(werte):
    return werte[-1]


def mitte(werte):
    return werte[1:3]


def umgedreht(werte):
    return werte[::-1]


def anzahl(werte):
    return len(werte)


def enthaelt(werte, ziel):
    return ziel in werte


def ersetzen(werte, neu):
    werte[1] = neu
    return werte


def verbinden(werte):
    text = ""
    for zahl in werte:
        text += str(zahl)
    return text


def pruefe():
    assert erstes([10, 20, 30]) == 10
    assert letztes([10, 20, 30]) == 30
    assert mitte([10, 20, 30, 40]) == [20, 30]
    assert umgedreht([1, 2, 3]) == [3, 2, 1]
    assert anzahl([1, 2, 2]) == 3
    assert enthaelt([1, 2], 2) is True
    assert enthaelt([1, 2], 9) is False
    assert ersetzen([10, 20, 30], 99) == [10, 99, 30]
    assert verbinden([1, 2]) == "12"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
