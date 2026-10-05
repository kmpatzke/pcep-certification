"""Lösungen zu Kapitel 01. Ausführen: python3 loesungen.py"""


def modell_von_python():
    # Python führt den Quelltext mit einem Interpreter aus.
    return "Interpreter"


def werkzeug_vor_dem_lauf():
    return "Compiler"


def ebene(kennzeichen):
    zuordnung = {
        "name": "Lexik",
        "klammer": "Syntax",
        "division": "Semantik",
    }
    return zuordnung[kennzeichen]


def ist_syntaxfehler(situation):
    # Einrückung und Form gehören zur Syntax, 1/0 zur Laufzeit.
    return situation in ("klammer", "einrueckung")


def definition(begriff):
    return {
        "syntax": "Form",
        "semantik": "Bedeutung",
        "lexik": "Bausteine",
    }[begriff]


def pruefe():
    assert modell_von_python() == "Interpreter"
    assert werkzeug_vor_dem_lauf() == "Compiler"
    assert ebene("name") == "Lexik"
    assert ebene("klammer") == "Syntax"
    assert ebene("division") == "Semantik"
    assert ist_syntaxfehler("klammer") is True
    assert ist_syntaxfehler("einrueckung") is True
    assert ist_syntaxfehler("division") is False
    assert definition("syntax") == "Form"
    assert definition("semantik") == "Bedeutung"
    assert definition("lexik") == "Bausteine"
    print("Alle Checks bestanden.")


if __name__ == "__main__":
    pruefe()
