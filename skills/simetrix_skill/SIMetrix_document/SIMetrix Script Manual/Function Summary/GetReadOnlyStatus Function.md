# GetReadOnlyStatus Function

Returns the read only status of the specified schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: real

Returns 1.0 if the schematic is read-only. Otherwise returns 0.0

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getreadonlystatus) | | |
| [◄ GetPrintValues](func_getprintvalues.htm) |  | [GetRegistryClassesRootKeys ▶](func_getregistryclassesrootkeys.htm) |
