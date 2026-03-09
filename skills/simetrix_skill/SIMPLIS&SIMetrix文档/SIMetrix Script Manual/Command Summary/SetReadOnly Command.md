# SetReadOnly Command

Sets a vector to be read-only. Once so assigned a vector can not be written to. Note that this is a one-way operation. It is not possible to remove the read-only status of a vector.

This command is intended for use when the program starts (possibly called from the startup script) to assign values as constants which can never be changed or deleted.

```
SetReadOnly <vecname>
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setreadonly) | | |
| [◄ SetPinSuffix](com_setpinsuffix.htm) |  | [SetRef ▶](com_setref.htm) |
