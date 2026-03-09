# GetSimulationInfo Function

Returns information about the most recent simulation.

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array of length 11 providing the following information about the most recent simulation:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Netlist path |
| 1 | List file path |
| 2 | Always returns 'True' |
| 3 | Name of user specified data file |
| 4 | Not used - returns empty |
| 5 | .OPTIONS line specified at RUN command |
| 6 | Analysis line specified at RUN command |
| 7 | Returns analysis type |
| 8 | Netlist title. If run from the schematic editor, this will be the path of the schematic file. |
| 9 | Current simulation status. See  [GetSimulatorStatus](func_getsimulatorstatus.htm) |
| 10 | Reserved for future use |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulationinfo) | | |
| [◄ GetSimulationErrors](func_getsimulationerrors.htm) |  | [GetSimulationSeeds ▶](func_getsimulationseeds.htm) |
