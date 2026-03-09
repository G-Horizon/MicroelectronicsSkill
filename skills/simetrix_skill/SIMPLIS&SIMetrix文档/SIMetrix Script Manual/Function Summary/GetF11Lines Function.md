# GetF11Lines Function

Returns the contents of the schematic's text window also known as the F11 window. Each element of the returned array contains a single line of the F11 text.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Options |
| 2 | real | No | -1 | Schematic ID |

#### Argument 1

If set to 'spice' the lines will be filtered to remove inline comments and join lines connected using the '+' continuation character. Note that with arg1='spice' normal '\*' comments pass through unmodified as long as they are not embedded between '+' continuation lines. Also, leading spaces will also be stripped in this mode.

#### Argument 2

Schematic ID as returned by  [OpenSchematic](func_openschematic.htm) . This makes it possible to apply this function to any schematic and not just the one that is currently displayed. See  [OpenSchematic](func_openschematic.htm)  for more details.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getf11lines) | | |
| [◄ GetEthernetAddresses](func_getethernetaddresses.htm) |  | [GetFailedNodesFromIterNum ▶](func_getfailednodesfromiternum.htm) |
