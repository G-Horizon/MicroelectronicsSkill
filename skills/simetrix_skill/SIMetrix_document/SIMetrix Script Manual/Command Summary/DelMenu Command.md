# DelMenu Command

Deletes specified menu item, or submenu.

```
DelMenu [/bypos <pos>] [/force] [/keepid] <menuname>
```

### Parameters

|  |  |
| --- | --- |
| /bypos | The menu to be deleted is identified by its position. The first item in the menu is at position zero. |
| /force | If specified, will allow complete submenus to be deleted. Otherwise this command will only delete a single menu item. |
| menuname | Composed of strings separated by pipe symbol: '|'. First name must be one of the following:  |  |  | | --- | --- | | SHELL | Command shell menu | | SCHEM | Schematic popup menu | | GRAPH | Graph popup menu | | LEGEND | Popup menu in graph "legend panel" | | SCHEMMAIN | Schematic main menu | | SYMBOL | Symbol editor popup menu | | SYMBOLMAIN | Symbol editor fixed menu |  The remaining strings identify the menu and item names. See  [DefMenu](com_defmenu.htm)  for details on menu names. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_delmenu) | | |
| [◄ DelLegendProp](com_dellegendprop.htm) |  | [DelProp ▶](com_delprop.htm) |
