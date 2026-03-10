# GetSimulatorStatus Function

Returns the current status of the simulator.

### Arguments

No arguments

### Returns

Return type: string

May be one of the following values:

|  |  |
| --- | --- |
| **Value** | **Definition** |
| Paused | Simulator paused |
| InProgress | Simulation in progress. (The only situation where this value can be returned is when calling this function remotely using the SxCommand utility with the - immediate switch. It isn't otherwise possible to call a function while a simulation is running.) |
| ConvergenceFail | Last simulation failed because of no convergence |
| SimErrors | Last simulation failed because of a run time error |
| NetlistErrors | Last simulation failed because of a netlist error |
| Warnings | Last simulation completed with warnings |
| Complete | Last simulation successful |
| None | No simulation has been run |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatorstatus) | | |
| [◄ GetSimulatorStats](func_getsimulatorstats.htm) |  | [GetSoaDefinitions ▶](func_getsoadefinitions.htm) |
