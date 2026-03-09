# NewSchem Command

Creates a new schematic sheet within the currently selected schematic window. If no schematic window is open, one will be created.

```
NewSchem [/newWindow] [/simulator simulator] <window-title>
```

### Parameters

|  |  |
| --- | --- |
| /newWindow | If specified, a new schematic window will be created. |
| /simulator | Specifies initial simulaor mode. Set to 'SIMPLIS' to open an empty schematic switched to SIMPLIS mode or 'SIMetrix' to open in SIMetrix mode. If not specified, the schematic will open in a mode determined by the 'InitSchematicSimulator' option setting. (Defined using command  [Set](com_set.htm)  ). |
| window-title | The name of the schematic, which will appear in the schematics title bar and will be the default filename that will be used if **File** > **Save** is used. Note that no file is created by the NewSchem command. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_newschem) | | |
| [◄ NewPrinterPage](com_newprinterpage.htm) |  | [NewScript ▶](com_newscript.htm) |
