# NetNames Function

Returns array of all net names in selected schematic

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

Returns an array of strings holding all the net names in the currently selected schematic. Returns an empty value if the schematic is empty or can't be found.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_netnames) | | |
| [◄ NetName](func_netname.htm) |  | [NetToCirc ▶](func_nettocirc.htm) |
