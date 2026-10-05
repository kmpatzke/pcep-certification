# PCEP-Lernpfad (Deutsch)

Eigenständiger Lernpfad für die Prüfung **PCEP-30-02** des Python Institute / OpenEDG: *PCEP – Certified Entry-Level Python Programmer*.

Geprüft am **2026-10-05** auf den offiziellen Seiten. An diesem Tag ist PCEP-30-02 die aktive Fassung. PCEP-30-03 steht dort noch auf „in development“. Zahlen, Bedingungen und Quellen stehen in [`einleitung/aufbau-und-bedingungen.md`](einleitung/aufbau-und-bedingungen.md).

Die Aufgaben und Testprüfungen in diesem Repo sind **neu geschrieben**. Sie sind keine offiziellen Items, keine Dumps und keine bezahlten Fragenbanken.

## So lernst du

1. Lies die Einleitung: Aufbau, Bedingungen, Kapitelplan.
2. Gehe die Ordner in `kapitel/` der Reihe nach durch.
3. Lies `lerntext.md`.
4. Löse `uebungen.py`. Dort stehen nur Aufgaben als Kommentare und leere Stubs (`pass` / `TODO`).
5. Vergleiche mit `loesungen.py` und starte die Referenz:

   ```bash
   python3 loesungen.py
   ```

   Am Ende muss `Alle Checks bestanden.` erscheinen.
6. Wenn die Kapitel sitzen, schreibe die zehn Prüfungen in `testpruefungen/`. Jede hat 30 Aufgaben, 40 Minuten und die Bestehensgrenze 70 von 100 Punkten. Die Lösungen stehen unter dem Trenner. Vorher nicht nach unten scrollen.

Die offizielle Prüfung nennt keine Python-Nebenversion, nur die Mittel von **Python 3**. Die Lösungen laufen mit Python 3 (hier geprüft mit 3.12) und nutzen keine Syntax, die erst nach Python 3.8 kam.

## Ordner

| Ordner | Syllabus |
| --- | --- |
| `kapitel/01-begriffe` | 1.1 |
| `kapitel/02-struktur` | 1.2 |
| `kapitel/03-literale` | 1.3 (Literale, Namen, PEP 8) |
| `kapitel/04-zahlensysteme` | 1.3 (binär, oktal, hexadezimal) |
| `kapitel/05-operatoren` | 1.4 (Zahlen, Strings, Priorität, Gleitkomma) |
| `kapitel/06-vergleiche` | 1.4 (Vergleiche, `not` / `and` / `or`) |
| `kapitel/07-bit-und-typen` | 1.4 (Bitoperatoren, Typumwandlung) |
| `kapitel/08-ein-ausgabe` | 1.5 |
| `kapitel/09-bedingungen` | 2.1 |
| `kapitel/10-schleifen` | 2.2 (`while`, `for`, `range`, `pass`) |
| `kapitel/11-schleifensteuerung` | 2.2 (`break`, `continue`, `else`, Verschachtelung) |
| `kapitel/12-listen` | 3.1 (Aufbau, Index, Slice) |
| `kapitel/13-listen-weiter` | 3.1 (Methoden, Comprehensions, Kopien) |
| `kapitel/14-tupel` | 3.2 |
| `kapitel/15-dictionaries` | 3.3 |
| `kapitel/16-strings` | 3.4 |
| `kapitel/17-funktionen` | 4.1 |
| `kapitel/18-parameter` | 4.2 |
| `kapitel/19-ausnahmehierarchie` | 4.3 |
| `kapitel/20-ausnahmen` | 4.4 |
| `testpruefungen/pruefung-01.md` … `pruefung-10.md` | ganze Prüfung, zehn verschiedene Sätze |

## Prüfung in Kürze

- Code: **PCEP-30-02** (aktiv am 2026-10-05)
- Umfang: **30** Aufgaben, **40** Minuten plus 5 Minuten NDA/Tutorial
- Bestehen: **70 %**
- Blöcke: 7 Aufgaben / 18 %, 8 / 29 %, 7 / 25 %, 8 / 28 %
- Sprachen der echten Prüfung: Englisch, Spanisch, Portugiesisch, Polnisch, Japanisch. Deutsch ist keine Prüfungssprache.
