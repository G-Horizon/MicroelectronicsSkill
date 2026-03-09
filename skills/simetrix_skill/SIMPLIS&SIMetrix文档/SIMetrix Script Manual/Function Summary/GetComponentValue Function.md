# GetComponentValue Function

Same as  [SetComponentValue](func_setcomponentvalue.htm)  except that it can only read values. Refer to  [SetComponentValue](func_setcomponentvalue.htm)  for full details.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Address |
| 2 | real | No | -1 | Schematic ID |
| 3 | string | No | none | Options |

#### Argument 2

Schematic ID as returned by the  [OpenSchematic](func_openschematic.htm)  function. This allows this function to be used with a schematic that is not open or not currently selected. If equal to -1, the currently selected schematic will be used.

#### Argument 3

If set to 'noopen' the schematic will not be opened to view by a call to this function

### Returns

Return type: string array

Refer to  [SetComponentValue](func_setcomponentvalue.htm)  for details

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcomponentvalue) | | |
| [◄ GetCompatiblePathName](func_getcompatiblepathname.htm) |  | [GetConfigLoc ▶](func_getconfigloc.htm) |
