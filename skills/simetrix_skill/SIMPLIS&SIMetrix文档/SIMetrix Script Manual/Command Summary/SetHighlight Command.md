# SetHighlight Command

Highlights or unhighlights schematic objects.

At most one parameter switch at may be used.

```
SetHighlight /prop <propname> [<propvalue>] | /wire <wirehandle> [<colourindex>] | /net <netname> [<colour>] /all 1 | /all 0 | /clearallopen | 1 | 0
```

### Parameters

|  |  |
| --- | --- |
| /all | If '1' specified, highlights all objects on selected schematic. Otherwise, unhighlights all objects on selected schematic. |
| /clearAllOpen | Clears all highlighting on all open schematics. |
| /net |  |
| /prop | Property name. If specified without propvalue all instances possessing propname will be highlighted. Otherwise only instances possessing propname with propvalue will be highlighted. |
| /wire | Handle of wire to be highlighted. |
| 1|0 | When no switches are given, if set to '1', all selected objects highlighted, otherwise all selected objects unhighlighted. |

### Notes

Usage is one of the following:

1. SetHighlight /prop  *propname*  [  *propvalue*  ]
2. SetHighlight /wire  *wirehandle*
3. SetHighlight /all 1|0
4. SetHighlight /clearAllOpen
5. SetHighlight 1|0

;

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_sethighlight) | | |
| [◄ SetGroup](com_setgroup.htm) |  | [SetOrigin ▶](com_setorigin.htm) |
