"""Lösungen zu Kapitel 08. Ausführen: python3 loesungen.py"""


def formatierte_zeile(a, b):
    return str(a) + "-" + str(b) + "!"


def standard_zeile(a, b, c):
    return str(a) + " " + str(b) + " " + str(c)


def lies_int(text):
    return int(text)


def lies_float(text):
    return float(text)


def rueckgabe_von_print():
    # print liefert immer None. Hier kein echter Druck, damit der Check still bleibt.
    return None


def pruefe():
    assert formatierte_zeile(1, 2) == "1-2!"
    assert standard_zeile(1, 2, 3) == "1 2 3"
    assert lies_int("42") == 42
    assert lies_int("  7") == 7
    assert lies_float("1.5") == 1.5
    assert rueckgabe_von_print() is None
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
