# 1.3 Zahlensysteme

Ganze Zahlen kann Python im Quelltext dezimal, binär, oktal oder hexadezimal schreiben. Der gespeicherte Wert ist immer ein `int`. Das Präfix ändert nur die Schreibweise.

| System | Basis | Präfix | Beispiel | Dezimalwert |
| --- | --- | --- | --- | --- |
| binär | 2 | `0b` oder `0B` | `0b1010` | 10 |
| oktal | 8 | `0o` oder `0O` | `0o17` | 15 |
| dezimal | 10 | keines | `255` | 255 |
| hexadezimal | 16 | `0x` oder `0X` | `0xFF` | 255 |

Hexadezimalziffern: `0`–`9` und `a`–`f` (auch groß). `0x10` ist 16, nicht 10.

```python
0b1010 == 10
0o17 == 15
0xFF == 255
```

Führende Nullen ohne Präfix sind in Python 3 **kein** Oktalcode. `0o17` ist oktal. Eine nackte `017` ist ein Syntaxfehler, weil die Ziffer 8 im Oktalsystem nicht existiert und weil eine führende Null so nicht mehr als Oktal gilt: `017` wird vom Parser abgelehnt.

## Umwandeln

```python
bin(10)   # '0b1010'
oct(15)   # '0o17'
hex(255)  # '0xff'
int("ff", 16)   # 255
int("1010", 2)  # 10
int("17", 8)    # 15
```

`bin`, `oct` und `hex` liefern einen **String** inklusive Präfix. `int(text, basis)` liest einen String ohne Präfix in der angegebenen Basis. Die Basis darf 2 bis 36 sein. `int("0xff", 16)` akzeptiert das Präfix ebenfalls.

`int("ff")` ohne Basis ist die Basis 10 und wirft `ValueError`, weil `f` keine Dezimalziffer ist.

## Prüfungsfallen

- `0x10` ist 16.
- `hex(255)` ist der String `'0xff'`, nicht die Zahl 255.
- `0b2` ist ein Syntaxfehler: die Ziffer 2 gibt es im Binärsystem nicht.
- Groß- und Kleinschreibung im Präfix und bei Hex-Ziffern ist egal: `0xFf == 0Xff`.
- Das Präfix gehört zum Literal. Es ist kein Operator.
