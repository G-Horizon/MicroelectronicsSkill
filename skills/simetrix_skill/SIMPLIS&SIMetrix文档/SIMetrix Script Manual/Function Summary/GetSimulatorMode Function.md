# GetSimulatorMode Function

Returns the simulator mode, that is SIMetrix or SIMPLIS, of the current schematic

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string

Return value may be 'SIMetrix' or 'SIMPLIS'.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatormode) | | |
| [◄ GetSimulatorEvents](func_getsimulatorevents.htm) |  | [GetSimulatorOption ▶](func_getsimulatoroption.htm) |
