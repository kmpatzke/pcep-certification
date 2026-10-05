"""Lösungen zu Kapitel 19. Ausführen: python3 loesungen.py"""


def oberklasse(name):
    tabelle = {
        "IndexError": "LookupError",
        "KeyError": "LookupError",
        "ZeroDivisionError": "ArithmeticError",
        "KeyboardInterrupt": "BaseException",
    }
    return tabelle[name]


def faengt_exception(name):
    klassen = {
        "ValueError": ValueError,
        "KeyboardInterrupt": KeyboardInterrupt,
        "SystemExit": SystemExit,
    }
    return issubclass(klassen[name], Exception)


def fehlerart(situation):
    return {
        "division": "ZeroDivisionError",
        "index": "IndexError",
        "schluessel": "KeyError",
        "plus": "TypeError",
        "inttext": "ValueError",
    }[situation]


def ist_lookup(name):
    klassen = {"IndexError": IndexError, "TypeError": TypeError}
    return issubclass(klassen[name], LookupError)


def gleicher_zweig():
    return issubclass(IndexError, KeyError) or issubclass(KeyError, IndexError)


def pruefe():
    assert oberklasse("IndexError") == "LookupError"
    assert oberklasse("KeyError") == "LookupError"
    assert oberklasse("ZeroDivisionError") == "ArithmeticError"
    assert oberklasse("KeyboardInterrupt") == "BaseException"
    assert faengt_exception("ValueError") is True
    assert faengt_exception("KeyboardInterrupt") is False
    assert faengt_exception("SystemExit") is False
    assert fehlerart("division") == "ZeroDivisionError"
    assert fehlerart("index") == "IndexError"
    assert fehlerart("schluessel") == "KeyError"
    assert fehlerart("plus") == "TypeError"
    assert fehlerart("inttext") == "ValueError"
    assert ist_lookup("IndexError") is True
    assert ist_lookup("TypeError") is False
    assert gleicher_zweig() is False
    try:
        int("1.5")
    except ValueError:
        pass
    else:
        raise AssertionError("int('1.5') muss ValueError sein")
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
