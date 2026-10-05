"""Lösungen zu Kapitel 09. Ausführen: python3 loesungen.py"""


def bewertung(note):
    if note == 1:
        return "sehr gut"
    elif note == 2:
        return "gut"
    elif note == 3:
        return "befriedigend"
    else:
        return "andere"


def zwei_ifs(x):
    spur = ""
    if x > 0:
        spur += "a"
    if x > 3:
        spur += "b"
    return spur


def mit_elif(x):
    spur = ""
    if x > 0:
        spur += "a"
    elif x > 3:
        spur += "b"
    return spur


def eintritt(alter, karte):
    if alter >= 18:
        if karte:
            return "ja"
        else:
            return "ausweis_fehlt"
    else:
        return "nein"


def gruss(name):
    if name:
        return name
    return "unbekannt"


def pruefe():
    assert bewertung(1) == "sehr gut"
    assert bewertung(2) == "gut"
    assert bewertung(4) == "andere"
    assert zwei_ifs(5) == "ab"
    assert zwei_ifs(1) == "a"
    assert zwei_ifs(-1) == ""
    assert mit_elif(5) == "a"
    assert mit_elif(-1) == ""
    assert eintritt(17, True) == "nein"
    assert eintritt(20, True) == "ja"
    assert eintritt(20, False) == "ausweis_fehlt"
    assert gruss("") == "unbekannt"
    assert gruss("Ada") == "Ada"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
