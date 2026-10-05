"""Lösungen zu Kapitel 13. Ausführen: python3 loesungen.py"""


def aufbauen():
    werte = [1, 2]
    werte.append(3)
    werte.insert(0, 9)
    return werte


def entfernen():
    werte = [9, 1, 2]
    werte.remove(1)
    del werte[0]
    return werte


def quadrate(n):
    return [i * i for i in range(n)]


def sortiert(werte):
    return sorted(werte)


def kopiere(werte):
    return werte[:]


def matrix():
    return [[0, 0] for _ in range(3)]


def pruefe():
    assert aufbauen() == [9, 1, 2, 3]
    assert entfernen() == [2]
    assert quadrate(4) == [0, 1, 4, 9]
    quelle = [3, 1, 2]
    assert sortiert(quelle) == [1, 2, 3]
    assert quelle == [3, 1, 2]
    original = [1, 2]
    kopie = kopiere(original)
    assert kopie == [1, 2]
    assert kopie is not original
    m = matrix()
    m[0][0] = 1
    assert m == [[1, 0], [0, 0], [0, 0]]
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
