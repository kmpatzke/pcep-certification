"""Lösungen zu Kapitel 20. Ausführen: python3 loesungen.py"""

gesehen = False


def sicher(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def art(text):
    try:
        int(text)
        return "ok"
    except ValueError:
        return "wert"
    except Exception:
        return "sonst"


def innen(b):
    return 1 / b


def aussen(b):
    try:
        return innen(b)
    except ZeroDivisionError:
        return None


def pruefe(n):
    if n < 0:
        raise ValueError("negativ")
    return n


def weiter(ausloesen):
    global gesehen
    try:
        if ausloesen:
            raise ValueError("absichtlich")
    except ValueError:
        gesehen = True
        raise


def pruefe_datei():
    assert sicher(6, 2) == 3.0
    assert sicher(1, 0) is None
    assert art("12") == "ok"
    assert art("x") == "wert"
    assert aussen(0) is None
    assert aussen(2) == 0.5
    assert pruefe(2) == 2
    try:
        pruefe(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("pruefe(-1) muss ValueError werfen")
    try:
        weiter(True)
    except ValueError:
        pass
    else:
        raise AssertionError("weiter muss weiterwerfen")
    assert gesehen is True
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe_datei()
