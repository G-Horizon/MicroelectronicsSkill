# SetReadOnlyStatus Function

Sets the read-only status of the specified schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Read-only status |
| 2 | real | No | -1 | Schematic ID |

#### Argument 1

Read only status. If 1.0, will set schematic to read-only; if 0.0 will set to writeable.

#### Argument 2

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string

Single string defining the success of the operation is defined below.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_setreadonlystatus) | | |
| [◄ SetPropertyStyles](func_setpropertystyles.htm) |  | [SetSymmetricDifference ▶](func_setsymmetricdifference.htm) |
