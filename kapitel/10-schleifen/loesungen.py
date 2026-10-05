"""Lösungen zu Kapitel 10. Ausführen: python3 loesungen.py"""


def summe_while(n):
    summe = 0
    while n > 0:
        summe += n
        n -= 1
    return summe


def summe_for(n):
    summe = 0
    for i in range(1, n + 1):
        summe += i
    return summe


def zahlen(n):
    return list(range(n))


def zahlen_schritt():
    return list(range(1, 6, 2))


def zahlen_rueck():
    return list(range(5, 1, -1))


def verdoppelt(text):
    ergebnis = ""
    for zeichen in text:
        ergebnis += zeichen + zeichen
    return ergebnis


def mit_pass(leer, start):
    if leer:
        pass
    else:
        start = start + 1
    return start


def pruefe():
    assert summe_while(4) == 10
    assert summe_while(0) == 0
    assert summe_for(4) == 10
    assert zahlen(3) == [0, 1, 2]
    assert zahlen_schritt() == [1, 3, 5]
    assert zahlen_rueck() == [5, 4, 3, 2]
    assert verdoppelt("ab") == "aabb"
    assert mit_pass(True, 5) == 5
    assert mit_pass(False, 5) == 6
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
