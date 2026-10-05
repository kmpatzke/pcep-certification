"""Lösungen zu Kapitel 03. Ausführen: python3 loesungen.py"""

import keyword


def typname(wert):
    return type(wert).__name__


def wissenschaftlich(literal):
    # float() liest auch die wissenschaftliche Schreibweise.
    return float(literal)


def name_gueltig(name):
    return name.isidentifier() and not keyword.iskeyword(name)


def nach_pep8(name):
    teile = []
    puffer = ""
    for zeichen in name:
        if zeichen.isupper() and puffer:
            teile.append(puffer)
            puffer = zeichen.lower()
        else:
            puffer += zeichen.lower()
    teile.append(puffer)
    return "_".join(teile)


def endwert():
    wert = 10
    wert = wert + 5
    if wert > 12:
        wert = "ok"
    else:
        wert = "klein"
    return wert


def pruefe():
    assert typname(True) == "bool"
    assert typname(4) == "int"
    assert typname(2e3) == "float"
    assert typname("4") == "str"
    assert wissenschaftlich("2e3") == 2000.0
    assert wissenschaftlich("1.5e-1") == 0.15
    assert wissenschaftlich("4E2") == 400.0
    assert name_gueltig("alter") is True
    assert name_gueltig("_privat") is True
    assert name_gueltig("2alter") is False
    assert name_gueltig("for") is False
    assert name_gueltig("") is False
    assert nach_pep8("flaecheKreis") == "flaeche_kreis"
    assert nach_pep8("alter") == "alter"
    assert endwert() == "ok"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
