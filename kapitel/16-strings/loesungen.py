"""Lösungen zu Kapitel 16. Ausführen: python3 loesungen.py"""


def anfang(text):
    return text[0]


def ende(text):
    return text[-1]


def ausschnitt(text):
    return text[1:4]


def rueckwaerts(text):
    return text[::-1]


def normalisiert(text):
    return text.strip().lower()


def position(text, suche):
    return text.find(suche)


def teilen(text):
    return text.split(",")


def verbinden(teile):
    return ",".join(teile)


def zwei_zeilen():
    return "oben\nunten"


def pruefe():
    assert anfang("Hallo") == "H"
    assert ende("Hallo") == "o"
    assert ausschnitt("Hallo") == "all"
    assert rueckwaerts("abc") == "cba"
    assert normalisiert("  Ab ") == "ab"
    assert position("ab", "b") == 1
    assert position("ab", "z") == -1
    assert teilen("a,b") == ["a", "b"]
    assert verbinden(["a", "b"]) == "a,b"
    assert zwei_zeilen() == "oben\nunten"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
