"""Lösungen zu Kapitel 02. Ausführen: python3 loesungen.py"""

import keyword


def ist_schluesselwort(wort):
    return keyword.iskeyword(wort)


def tiefe(ebene):
    # PEP 8: vier Leerzeichen je Ebene.
    return ebene * 4


def wert_nach_kommentar():
    x = 1
    # x = 99
    x = x + 4
    return x


def name_erlaubt(name):
    if name == "":
        return False
    return not keyword.iskeyword(name)


def nach_if(bedingung):
    zeile = "ausserhalb"
    if bedingung:
        zeile = "innen"
    return zeile


def pruefe():
    assert ist_schluesselwort("for") is True
    assert ist_schluesselwort("For") is False
    assert ist_schluesselwort("summe") is False
    assert tiefe(0) == 0 and tiefe(1) == 4 and tiefe(2) == 8
    assert wert_nach_kommentar() == 5
    assert name_erlaubt("summe") is True
    assert name_erlaubt("_x") is True
    assert name_erlaubt("wert2") is True
    assert name_erlaubt("if") is False
    assert name_erlaubt("None") is False
    assert name_erlaubt("") is False
    assert nach_if(True) == "innen"
    assert nach_if(False) == "ausserhalb"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
