"""Übungen zu Kapitel 01 (Syllabus 1.1).

Lies lerntext.md. Ersetze pass durch deinen Code.
In dieser Datei steht keine Lösung. Erwartetes Verhalten steht im Kommentar.
"""


# Aufgabe 1
# Ordne Python dem Syllabus-Begriff zu.
# Erwartetes Verhalten: modell_von_python() == "Interpreter"
def modell_von_python():
    # TODO
    pass


# Aufgabe 2
# "Compiler" oder "Interpreter": Was übersetzt das Programm,
# bevor es ausgeführt wird?
# Erwartetes Verhalten: werkzeug_vor_dem_lauf() == "Compiler"
def werkzeug_vor_dem_lauf():
    # TODO
    pass


# Aufgabe 3
# Ebene eines Beispiels: "Lexik", "Syntax" oder "Semantik".
# "print" als erlaubter Name -> "Lexik"
# eine fehlende Klammer in print("hi" -> "Syntax"
# die Division 1/0, die erst beim Lauf scheitert -> "Semantik"
# Erwartetes Verhalten:
#   ebene("name") == "Lexik"
#   ebene("klammer") == "Syntax"
#   ebene("division") == "Semantik"
def ebene(kennzeichen):
    # TODO
    pass


# Aufgabe 4
# True, wenn die Situation ein Syntaxfehler ist, sonst False.
# "klammer" und "einrueckung" sind Syntaxfehler.
# "division" (1/0) ist keiner.
# Erwartetes Verhalten:
#   ist_syntaxfehler("klammer") ist True
#   ist_syntaxfehler("einrueckung") ist True
#   ist_syntaxfehler("division") ist False
def ist_syntaxfehler(situation):
    # TODO
    pass


# Aufgabe 5
# Kurze Definition als exakter String, wie unten gefordert.
# Erwartetes Verhalten:
#   definition("syntax") == "Form"
#   definition("semantik") == "Bedeutung"
#   definition("lexik") == "Bausteine"
def definition(begriff):
    # TODO
    pass
