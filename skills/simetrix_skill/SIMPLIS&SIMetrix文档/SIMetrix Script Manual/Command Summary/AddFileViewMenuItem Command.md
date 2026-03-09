# AddFileViewMenuItem Command

Adds a menu item to a for a FileView context menu.

The functiond  [GetFileViewerSelectedDirectories](func_getfileviewerselecteddirectories.htm)  and  [GetFileViewerSelectedFiles](func_getfileviewerselectedfiles.htm)  may be used to retrieve the items currently selected in the file viewer

```
AddFileViewMenuItem <file-type> <text> <command>
```

### Parameters

|  |  |
| --- | --- |
| /directory | Flag to say associate this with directories. |
| file-type | The file format to associate this with, for example 'Schematic'. This corresponds to the File Extensions list in the General Options dialog. This is not required if the directory flag is set. The following values can be used:   * Component * Schematic * Script * VerilogA * VerilogHDL * Netlist * Model |
| text | The name of the menu that will be shown. |
| command | The script command to call if the menu item is executed. |

### See Also

* [GetFileViewerSelectedDirectories](func_getfileviewerselecteddirectories.htm)
* [GetFileViewerSelectedFiles](func_getfileviewerselectedfiles.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addfileviewmenuitem) | | |
| [◄ AddDoubleClickAction](com_adddoubleclickaction.htm) |  | [AddFloodFill ▶](com_addfloodfill.htm) |
