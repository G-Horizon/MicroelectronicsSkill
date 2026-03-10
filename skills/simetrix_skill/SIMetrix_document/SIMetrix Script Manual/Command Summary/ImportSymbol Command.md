# ImportSymbol Command

Imports an existing symbol to the currently open symbol editor sheet.

```
ImportSymbol [/loc <x> <y>] [/local] [/path <pathname>] [/comp] <name>
```

### Parameters

|  |  |
| --- | --- |
| /comp | Opens the symbol for a component whose path is specified by  *name* . |
| /fromschematic | Will load the symbol from the last selected schematic. Used internally. |
| /loc | If /loc switch specified, the symbol is placed at the location specified by  *x*  and  *y* . In practice this location may only be used in a relative manner as the exact location on the symbol sheet of the origin will be adjusted to ensure that the symbol is in view. |
| /local | The symbol will be obtained from the local library of the current schematic. If not specified the symbol will be obtained from the global library. |
| /path | If specified, the symbol will be converted to a component to be saved in the file specified by  *pathname* . |
| name | Symbol name. |

### Notes

If the current symbol sheet is empty, the named symbol will become the current symbol in that sheet. This will be reflected in the caption bar text and the default symbol to be saved when **File** > **Save...** is selected.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_importsymbol) | | |
| [◄ HourGlass](com_hourglass.htm) |  | [Inst ▶](com_inst.htm) |
