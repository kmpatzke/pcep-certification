"""Übungen zu Kapitel 11 (Syllabus 2.2, Steuerung und else)."""


# Aufgabe 1
# Zeichen bis vor dem ersten "d" sammeln. Beim "d" die Schleife verlassen.
# Erwartetes Verhalten: bis_d("abcde") == "abc"
def bis_d(text):
    # TODO
    pass


# Aufgabe 2
# Jedes "a" überspringen, den Rest aneinanderhängen.
# Erwartetes Verhalten: ohne_a("abca") == "bc"
def ohne_a(text):
    # TODO
    pass


# Aufgabe 3
# Suche ziel in range(start, stopp).
# Bei Treffer True zurückgeben und die Schleife mit break verlassen.
# Läuft die Schleife ohne break zu Ende, soll der else-Zweig False liefern.
# Erwartetes Verhalten:
#   gefunden(4, 2, 5) ist True
#   gefunden(9, 2, 4) ist False
def gefunden(ziel, start, stopp):
    # TODO
    pass


# Aufgabe 4
# Äußere Schleife a in range(2), innere b in range(3).
# Wenn b == 1, nur die innere Schleife abbrechen.
# Hänge str(a) und str(b) an einen String, bevor das break kommt.
# Erwartetes Verhalten: paare() == "0010"
def paare():
    # TODO
    pass


# Aufgabe 5
# while: starte bei n und zähle herunter.
# Bei ungeradem n continue, nachdem n verkleinert wurde.
# Gerade Werte addieren. Bei n == 0 break.
# Erwartetes Verhalten: summe_gerade(5) == 6   # 4 + 2
def summe_gerade(n):
    # TODO
    pass
