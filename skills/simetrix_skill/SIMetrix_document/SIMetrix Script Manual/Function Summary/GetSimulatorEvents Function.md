# GetSimulatorEvents Function

\*\*\* UNSUPPORTED \*\*\* See [Unsupported Functions and Commands](scriptlanguage_unsupportedfunctionscommands.htm) for more information.

Returns list of events for most recent simulation.

This function was developed to aid simulator development and also to assist identifying causes of convergence failure. It has also been used to detect the success or otherwise of a simulation run called by a script by examining the last event in the return value.

The following is accurate for version 4.0b. Later versions may be different but any changes are likely to be made by adding additional events or/and adding additional fields to the event line.

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array, each element of which describes an event that occurred during the most recent simulation. Each element is a string consisting of a number of values separated by semi-colons. The first value is the name of the event. This can be one of the following:

|  |  |
| --- | --- |
| Singular matrix | Singular matrix - may lead to abort but not necessarily. |
| Floating point error | Floating point error occurred such as divide by zero or log of a negative number. May lead to abort but depends on where it occurred. |
| Operating point complete |  |
| Operating point failed |  |
| GMIN step started |  |
| Source step started |  |
| Pseudo transient started |  |
| Job started | Always the first event |
| Job complete | Final event |
| Job failed | Final event |
| Job paused | Final event |
| Job resumed |  |
| Job aborted | Final event |
| Node limit exceeded | Means that a node voltage exceeded the value of the NODELIMIT option. (Default 1e50). The iteration is rejected when this happens but does not directly lead to an abort. |
| Iteration succeeded (full) |  |
| Iteration failed (full) |  |
| Load failed | Iteration failed because device equations could not be evaluated. Usually caused by excessive junction voltage. |
| LTE reject (full) | Time step rejected because local truncation error too high. |
| LTE accept (full) | Local truncation error below tolerance. Time step accepted. |

The items marked "(full)" will only be listed if the .OPTIONS setting FULLEVENTREPORT is specified when the simulator is run.

The remaining values are listed below:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | See above table |
| 1 | Top level analysis mode. One of: 'none', 'Op', 'Tran', 'AC', 'Sweep', 'Noise', 'TF', 'Sensitivity', 'Pole-zero' |
| 2 | Operating point mode. One of: 'none', 'JI2', 'GMIN', 'Source', 'PTA' |
| 3 | Transient analysis time |
| 4 | Time step |
| 5 | Real time measured from start of run (not output for all events) |
| 6 | Iteration number |
| 7 | Event specific message |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatorevents) | | |
| [◄ GetSimulationSeeds](func_getsimulationseeds.htm) |  | [GetSimulatorMode ▶](func_getsimulatormode.htm) |
