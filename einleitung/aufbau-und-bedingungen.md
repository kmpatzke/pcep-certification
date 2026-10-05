# Aufbau und Bedingungen der PCEP-Prüfung

Stand der Live-Prüfung: **2026-10-05**. An diesem Tag wurden die unten verlinkten Seiten erneut gelesen. Wenn eine Zahl dort nicht steht, steht das hier ausdrücklich so.

## Welche Fassung

Vertraut wurde der Statustabelle auf der Prüfungsseite des Python Institute, nicht Blogposts und nicht Anbieter von Übungsfragen.

| Fassung | Status auf der offiziellen Seite am 2026-10-05 |
| --- | --- |
| **PCEP-30-02** | Active, current exam version |
| PCEP-30-03 | In development. Die Seite nennt eine geplante Veröffentlichung im dritten Quartal 2026. Am 5. Oktober 2026 ist 30-03 dort trotzdem nicht die aktive Prüfung. |

Dieser Lernpfad bereitet auf **PCEP-30-02** vor. Eine eigene Syllabus-Seite für 30-03 lag am Prüftag nicht vor.

Die offizielle Gültigkeit eines bestandenen Zertifikats ist **5 Jahre**. Unabhängige Webseiten behaupten teilweise eine lebenslange Gültigkeit oder ein Ruhestandsdatum 31. August 2026. Beides steht nicht auf den drei offiziellen Seiten, die hier zitiert werden. Es wird die Tabelle auf [pythoninstitute.org/pcep](https://pythoninstitute.org/pcep) verwendet.

## Eckdaten

Quelle der Tabelle: [PCEP – Exam Information](https://pythoninstitute.org/pcep), gelesen am 2026-10-05.

| Angabe | Wert |
| --- | --- |
| Name | PCEP – Certified Entry-Level Python Programmer |
| Code | PCEP-30-02 |
| Voraussetzungen | keine |
| Dauer | 40 Minuten Prüfung, zusätzlich 5 Minuten NDA/Tutorial |
| Anzahl der Aufgaben | 30 |
| Bestehensgrenze | 70 % |
| Gültigkeit | 5 Jahre |
| Sprachen | Englisch, Spanisch, Portugiesisch, Polnisch, Japanisch |
| Durchführung | OpenEDG Testing Service, TestNow |
| Python-Version | nicht als Nebenversion genannt; die Seite spricht von den wesentlichen Mitteln von **Python 3** |

Eine Nebenversion wie 3.10 oder 3.12 steht auf der Prüfungsseite, der Syllabus-Seite und im Syllabus-PDF nicht. Die FAQ des Instituts empfiehlt für den Kurs eine normale Installation von Python 3 von python.org. Das ist eine Lernempfehlung, keine Laufzeitangabe der Prüfung.

Deutsch ist **keine** Prüfungssprache. Dieser Lernpfad erklärt auf Deutsch. Bezeichner und Code bleiben so, wie sie in Python und in der Prüfung vorkommen.

## Aufgabentypen

Die Prüfungsseite nennt das Format so:

> Single- and multiple-select questions, drag & drop, gap fill, sort, code fill, code insertion, interactive & scenario-based items

Die Syllabus-Seite formuliert kürzer: single-select, multiple-select, coding, scenario-based und interactive items. Die ausführlichere Liste der Prüfungsseite ist die, nach der die Testprüfungen gebaut sind.

**Nicht veröffentlicht** ist, wie viele Aufgaben welchen Typs in einer echten Sitzung vorkommen. Die zehn Testprüfungen nutzen deshalb in jeder Prüfung dieselbe selbst gewählte Mischung aller genannten Typen, nicht eine offizielle Quote. Interaktive Widgets gibt es auf Papier nicht. Sie sind als Nachvollziehen von Ablauf und Ausgabe umgesetzt.

## Blöcke, Gewichte, Ziel-IDs

Quelle: [PCEP-30-0x Exam Syllabus](https://pythoninstitute.org/pcep-exam-syllabus), Syllabus zuletzt 23. Februar 2022, ausgerichtet auf PCEP-30-02. Dieselben Anzahlen und Gewichte stehen im [Syllabus-PDF](https://pythoninstitute.org/assets/627e61bc29de3989767095.pdf).

| Block | Name | Aufgaben | Gewicht | Max. Rohpunkte im PDF |
| --- | --- | --- | --- | --- |
| 1 | Computer Programming and Python Fundamentals | 7 | 18 % | 180 |
| 2 | Control Flow – Conditional Blocks and Loops | 8 | 29 % | 290 |
| 3 | Data Collections – Tuples, Dictionaries, Lists, and Strings | 7 | 25 % | 250 |
| 4 | Functions and Exceptions | 8 | 28 % | 280 |
| | Summe | 30 | 100 % | 1000 |

Bestehen laut Syllabus-Seite: ein kumulativer Durchschnitt von mindestens **70 %** über alle Blöcke.

### Bewertung, und wo die Quellen sich ergänzen

- Die **Live-Syllabus-Seite** sagt: jede Aufgabe ist höchstens 40 Punkte wert. Danach wird der Rohwert normalisiert und als Prozent angezeigt.
- Das **PDF** nennt die Block-Maxima 180, 290, 250 und 280. Deren Summe ist 1000, und 180/1000 ist genau 18 %, analog für die anderen Blöcke.
- 7 mal 40 ist 280 und wäre etwa 23 % des Examens, nicht 18 %. Die Gewichte passen also nicht zu „jede Aufgabe zählt genau 40“. Sie passen zu den PDF-Rohpunkten. „Maximum of 40 points“ wird hier als Obergrenze je Aufgabe gelesen, nicht als Einheitswert. Für die Obergrenze wird die Live-Seite zitiert, für die Blocksummen das PDF, weil nur das PDF diese vier Zahlen nennt und sie die veröffentlichten Prozente erklären.
- **Teilpunkte** und **Punktabzug für falsche Antworten** stehen auf den geprüften Seiten nicht. Beides wird hier nicht behauptet. In den Testprüfungen gibt es eine Aufgabe nur dann voll, wenn sie vollständig stimmt.

Der am Ende einer Sitzung angezeigte Score ist laut Testing Policies vorläufig und kann nach der Aufsicht noch geändert werden.

### Ziel-IDs

**Block 1**

- 1.1 Understand fundamental terms and definitions: Interpreter und Compiler, Lexik, Syntax, Semantik
- 1.2 Understand Python’s logic and structure: Schlüsselwörter, Anweisungen, Einrückung, Kommentare
- 1.3 Literale und Variablen, Zahlensysteme, Namen, PEP 8
- 1.4 Operatoren und Datentypen: Zahlen, Strings, Zuweisung, unär/binär, Priorität und Bindung, Bitoperatoren, Boolesche Operatoren, Vergleiche, Gleitkomma-Genauigkeit, Typumwandlung
- 1.5 Konsole: `print()`, `input()`, `sep`, `end`, `int()`, `float()`

**Block 2**

- 2.1 `if`, `if-else`, `if-elif`, `if-elif-else`, mehrere Bedingungen, Verschachtelung
- 2.2 `pass`, `while`, `for`, `range()`, `in`, Schleifen über Sequenzen, `while-else`, `for-else`, Verschachtelung, `break`, `continue`

**Block 3**

- 3.1 Listen: Aufbau, Index, Slice, `len()`, Methoden (`append`, `insert`, `index` und weitere), `sorted()`, `del`, `for`, `in` / `not in`, Comprehensions, Kopieren, verschachtelte Listen
- 3.2 Tupel: Index, Slice, Aufbau, Unveränderbarkeit, Unterschied zu Listen, Verschachtelung
- 3.3 Dictionaries: Aufbau, Index, Schlüssel hinzufügen und entfernen, Iteration, Existenzprüfung, `keys()`, `items()`, `values()`
- 3.4 Strings: Aufbau, Index, Slice, Unveränderbarkeit, Escape mit `\`, Anführungszeichen, mehrzeilige Strings, grundlegende Funktionen und Methoden

Die Syllabus-Seite zählt bei 3.3 und 3.4 keinen Gedankenstrich vor dem Titel (`3.3 Collect…`). Die PDF-Fassung und die übrigen IDs nutzen denselben Nummernkreis. Es sind die Ziele 3.3 und 3.4.

**Block 4**

- 4.1 Funktionen und Generatoren definieren und aufrufen, `return`, `None`, Rekursion
- 4.2 Parameter und Argumente, positional, Schlüsselwort, gemischt, Standardwerte, Gültigkeitsbereiche, Verschattung, `global`
- 4.3 Hierarchie: `BaseException`, `Exception`, `SystemExit`, `KeyboardInterrupt`, abstrakte Ausnahmen, `ArithmeticError`, `LookupError`, `IndexError`, `KeyError`, `TypeError`, `ValueError`
- 4.4 `try-except`, Reihenfolge der `except`-Zweige, Weiterreichen über Funktionsgrenzen, Verantwortung abgeben

Die Live-Seite schreibt über Block 4 zusätzlich „7 objectives & 19 sub-objectives“, listet aber nur die vier IDs 4.1 bis 4.4. Dieselben vier IDs stehen im PDF. Gezählt werden hier die nummerierten IDs.

Der Abschnitt „MQC Profile“ auf der Syllabus-Seite gruppiert die Themen anders als die vier Prüfungsblöcke und nennt dort beispielhaft die Module `math` und `random`. Diese Module haben keine eigene Ziel-ID. Sie sind kein eigenes Kapitel. Wo ein Beispiel sie braucht, wird das im Kapitel gesagt.

## Bedingungen

Quelle: [PCEP Testing Policies](https://pythoninstitute.org/pcep-testing-policies), zuletzt überarbeitet 18. November 2025, gelesen am 2026-10-05. Ergänzend die FAQ auf der Prüfungsseite.

### Durchführung

Standard weltweit ist die **Online-Aufsicht** über den OpenEDG Online Proctoring Service in **TestNow**, einer Browser-Anwendung. Zusätzliche Software ist dafür nicht vorgesehen.

Der andere Weg sind **OpenEDG Testing Service Partners** (Schulen, Hochschulen, Einrichtungen im Partnerprogramm). Das ist ausdrücklich nicht der Standardweg. Die Prüfung findet dort in einer gesicherten Umgebung statt, mit Aufsicht vor Ort. Die Policies sprechen von physical test center, ruhigem Testraum und Prüfstation. Wer diesen Weg nutzt, soll 15 Minuten vor dem Termin da sein.

Online-Prüfungen über den Proctoring Service müssen nicht umgebucht werden, solange der Voucher nicht eingelöst ist und nicht abgelaufen ist. Einen Termin bei einem Partner verschiebt man mindestens 24 Stunden vorher beim Anbieter.

### Identität

- Partner / Testzentrum: mindestens ein gültiger Lichtbildausweis. Abgelaufene Ausweise gelten nicht. Genannt werden State/Country ID card, Führerschein, Reisepass, Military ID, Employee/school ID, Social Security card, Kredit- oder Debitkarte, Bank/ATM card, Library card. Ohne Ausweis kein Einlass. Die Aufsicht prüft die Identität und startet die Sitzung.
- Online: Während des Check-ins kann ein Foto des Gesichts und/oder des Ausweisdokuments verlangt werden. Webcam und Mikrofon bleiben erforderlich. Gesicht und Schultern müssen sichtbar bleiben. Die Policies sagen „may be asked“, nicht dass jeder Schritt bei jeder Sitzung gleich aussieht.

Kinder unter 13 Jahren dürfen nicht prüfen. Mit 13 bis 17 Jahren nur mit Zustimmung der Erziehungsberechtigten. Ab 18 ohne diese Altersauflage.

### Materialien

Die Policies verwenden nicht das Wort „closed book“. Der Sache nach ist die Sitzung geschlossen:

- Verboten sind Notizen, Hefte, Lehrbücher, externe Monitore, Aufnahmegeräte, Telefone, Smartwatches, Headsets, Smart Glasses und andere elektronische oder Kommunikationsgeräte.
- Verboten ist der Zugriff auf Notizen, Lernmaterial, didaktische Hilfen und andere Prüfungshilfen.
- Verboten sind Braindumps und nicht autorisierte Veröffentlichungen von Aufgaben.
- Die Prüfung wird allein abgelegt. Keine zweite Person, keine Pausen sind vorgesehen. Den Raum verlassen oder aus dem Kamerabild gehen kann die Sitzung beenden.
- NDA: Aufgaben und Antworten dürfen nicht kopiert, notiert oder weitergegeben werden. Wer die NDA ablehnt, verliert die Sitzung und die Gebühr.
- Vollbild nicht verlassen, keine neuen Tabs, nicht mehr als ein Bildschirm.

### Sprache

PCEP-30-02: Englisch, Spanisch, Portugiesisch, Polnisch, Japanisch.

Es gibt keine automatische Zeitverlängerung, nur weil die Erstsprache nicht Englisch ist. Zeitzuschlag gibt es nur nach genehmigter Accommodation (25 %, 50 % oder 100 %), vorher beantragt.

### Wiederholung

- Prüfungsseite, FAQ „Can I retake the exam?“: eine nicht bestandene Prüfung erst nach **7 Tagen**. Mit Retake-Voucher erscheint danach „Get Free Retake“. Mit Single-Shot-Voucher braucht es einen neuen Voucher, ebenfalls nach 7 Tagen.
- Testing Policies, Retake Policy: nach einem Fehlversuch 7 Tage warten. Ein neuer Voucher kann nötig sein. Die Zahl der Wiederholungen einer nicht bestandenen Prüfung ist nicht begrenzt.
- Dieselbe Seite, Additional Information: nach Bestehen oder Nichtbestehen muss man „usually“ 7 Tage warten, bevor man dieselbe Prüfung erneut sitzt.

Die 7-Tage-Frist für einen Fehlversuch steht an beiden Stellen. Die Policies ergänzen, dass auch ein erneutes Antreten nach einem Bestehen üblicherweise 7 Tage wartet. Eine abweichende PCEP-Sonderfrist ist dort nicht beziffert.

### Zertifikat und Score

- Bestehensgrenze 70 %.
- Nach der Prüfung liegt ein Bericht (bestanden/nicht, Aufschlüsselung) in der Exam History.
- Wer besteht, erhält innerhalb von 24 Stunden eine E-Mail mit digitalem Zertifikat, Prüfcode und Credly-Badge. Das steht auf der Prüfungsseite, nicht in den Policies.
- Der sofort angezeigte Punktwert ist vorläufig, bis die Aufsicht die Sitzung freigibt.

Kosten standen am 2026-10-05 auf der Prüfungsseite (Exam ab 69 USD, mit Retake ab 86 USD, mit Retake und Practice Test ab 95 USD, Practice Test 29 USD). Sie sind keine Prüfungsbedingung und können sich ändern. Die offiziellen Practice Tests sind ein kostenpflichtiges Produkt des Instituts und nicht Teil dieses Repos.

## Kapitelplan

Jedes Kapitel hat `lerntext.md`, `uebungen.py` und `loesungen.py`.

| Ordner | IDs | Inhalt |
| --- | --- | --- |
| `kapitel/01-begriffe` | 1.1 | Interpreter, Compiler, Lexik, Syntax, Semantik |
| `kapitel/02-struktur` | 1.2 | Schlüsselwörter, Anweisungen, Einrückung, Kommentare |
| `kapitel/03-literale` | 1.3 | Bool, int, float, wissenschaftliche Schreibweise, Strings, Variablen, PEP 8 |
| `kapitel/04-zahlensysteme` | 1.3 | binär, oktal, dezimal, hexadezimal |
| `kapitel/05-operatoren` | 1.4 | `** * / % // + -`, String-`+` und `*`, Zuweisung, Priorität, Bindung, Gleitkomma |
| `kapitel/06-vergleiche` | 1.4 | `== != > >= < <=`, `not`, `and`, `or` |
| `kapitel/07-bit-und-typen` | 1.4 | `~ & ^ &#124; << >>`, Typumwandlung |
| `kapitel/08-ein-ausgabe` | 1.5 | `print`, `input`, `sep`, `end`, `int`, `float` |
| `kapitel/09-bedingungen` | 2.1 | `if`, `elif`, `else`, Verschachtelung |
| `kapitel/10-schleifen` | 2.2 | `pass`, `while`, `for`, `range`, `in` |
| `kapitel/11-schleifensteuerung` | 2.2 | `break`, `continue`, `else`, verschachtelte Schleifen |
| `kapitel/12-listen` | 3.1 | Aufbau, Index, Slice, `len`, `in`, `for` |
| `kapitel/13-listen-weiter` | 3.1 | Methoden, `del`, `sorted`, Comprehensions, Kopien, Matrizen |
| `kapitel/14-tupel` | 3.2 | Tupel, Unveränderbarkeit, Mischung mit Listen |
| `kapitel/15-dictionaries` | 3.3 | Aufbau, Schlüssel, Iteration, `keys`, `items`, `values` |
| `kapitel/16-strings` | 3.4 | Index, Slice, Escape, Methoden |
| `kapitel/17-funktionen` | 4.1 | `def`, `return`, `None`, Rekursion, Generatoren |
| `kapitel/18-parameter` | 4.2 | Argumente, Standards, Scope, `global` |
| `kapitel/19-ausnahmehierarchie` | 4.3 | eingebaute Hierarchie |
| `kapitel/20-ausnahmen` | 4.4 | `try`, `except`, Reihenfolge, Weiterreichen |

String-Operatoren `+` und `*` gehören im Syllabus zu 1.4 und liegen in Kapitel 05. Kapitel 16 wiederholt nur, dass Strings unveränderbar sind, und behandelt Aufbau und Methoden (3.4). `int()` und `float()` als Umwandlung liegen in Kapitel 07 (1.4) und als Teil der Eingabe noch einmal in Kapitel 08 (1.5), weil der Syllabus sie an beiden Stellen nennt.
