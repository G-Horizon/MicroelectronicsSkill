# DrawPin Command

Initiates "pin draw" mode in the currently open symbol editor. In this mode a pin symbol is presented for the user to place at the desired location on the symbol sheet.

```
DrawPin [/forcerepeat] [/loc <x> <y> ] [<base-name>]
```

### Parameters

|  |  |
| --- | --- |
| /forceRepeat | If specified, the operation will be repeated until the user cancels with the right mouse button. Each new pin be named according to the base name appended with an integer to make it unique. |
| /loc |  |
| base-name | Name of pin. If a pin of that name is already present on the schematic, the name will be appended with a number to make it unique. If the base name is already appended with a number, that number will be incremented until an unused name is found. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_drawpin) | | |
| [◄ DrawArrow](com_drawarrow.htm) |  | [Echo ▶](com_echo.htm) |
