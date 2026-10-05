"""Lösungen zu Kapitel 11. Ausführen: python3 loesungen.py"""


def bis_d(text):
    ergebnis = ""
    for zeichen in text:
        if zeichen == "d":
            break
        ergebnis += zeichen
    return ergebnis


def ohne_a(text):
    ergebnis = ""
    for zeichen in text:
        if zeichen == "a":
            continue
        ergebnis += zeichen
    return ergebnis


def gefunden(ziel, start, stopp):
    for n in range(start, stopp):
        if n == ziel:
            break
    else:
        return False
    return True


def paare():
    text = ""
    for a in range(2):
        for b in range(3):
            if b == 1:
                break
            text += str(a) + str(b)
    return text


def summe_gerade(n):
    summe = 0
    while True:
        n -= 1
        if n == 0:
            break
        if n % 2 != 0:
            continue
        summe += n
    return summe


def pruefe():
    assert bis_d("abcde") == "abc"
    assert ohne_a("abca") == "bc"
    assert gefunden(4, 2, 5) is True
    assert gefunden(9, 2, 4) is False
    assert paare() == "0010"
    assert summe_gerade(5) == 6
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
