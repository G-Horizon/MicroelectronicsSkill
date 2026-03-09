# GetAllSimulatorDevices Function

Returns a list of semi-colon delimited strings containing information on all built-in simulator devices.

### Arguments

No arguments

### Returns

Return type: string array

Array of semi-colon delimited strings. The strings in the field are defined in the following table:

|  |  |
| --- | --- |
| **Field** | **Description** |
| 0 | Device name |
| 1 | Model name - as used in the .MODEL statement. E.g npn, nmos etc. |
| 2 | Level parameter value |
| 3 | Minimum number of terminals |
| 4 | Maximum number of terminals |
| 5 | Device letter. E.g. 'Q' for BJTs, 'D' for diodes |

### Example

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getallsimulatordevices) | | |
| [◄ GetAllCurves](func_getallcurves.htm) |  | [GetAllSymbolPropertyNames ▶](func_getallsymbolpropertynames.htm) |
