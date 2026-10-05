"""Lösungen zu Kapitel 15. Ausführen: python3 loesungen.py"""


def ada():
    person = {"name": "Ada"}
    person["jahr"] = 1815
    return (person["name"], person["jahr"])


def ohne_a():
    buch = {"a": 1, "b": 2}
    del buch["a"]
    return len(buch)


def hat_schluessel(buch, schluessel):
    return schluessel in buch


def schluessel_sortiert(buch):
    return sorted(buch.keys())


def werte_in_reihenfolge(buch):
    return list(buch.values())


def paare(buch):
    return list(buch.items())


def pruefe():
    assert ada() == ("Ada", 1815)
    assert ohne_a() == 1
    assert hat_schluessel({"a": 1}, "a") is True
    assert hat_schluessel({"a": 1}, 1) is False
    assert schluessel_sortiert({"b": 2, "a": 1}) == ["a", "b"]
    assert werte_in_reihenfolge({"b": 2, "a": 1}) == [2, 1]
    assert paare({"a": 1, "b": 2}) == [("a", 1), ("b", 2)]
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
