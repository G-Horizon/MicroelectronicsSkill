# GetSimulatorStats Function

Returns statistical information about the most recent run

### Arguments

No arguments

### Returns

Return type: real array

Returns a 30 element real array providing statistical information about the most recent run. The meaning of each field is described below:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Number of event driven outputs |
| 1 | Number of event driven ports |
| 2 | Number of event driven instances |
| 3 | Number of event driven nodes |
| 4 | Number of equations (= matrix dimension = total number of nodes including internal nodes) |
| 5 | Total number of iterations |
| 6 | Number of transient iterations |
| 7 | Number of JI2 iterations. (First attempt at DC bias point) |
| 8 | Number of GMIN iterations |
| 9 | Number of source stepping iterations |
| 10 | Number of pseudo transient analysis iterations |
| 11 | Number of time points |
| 12 | Number of accepted time points |
| 13 | Total analysis time |
| 14 | Transient analysis time |
| 15 | Matrix load time (The time needed to calculate the device equations) |
| 16 | Matrix reorder time |
| 17 | Matrix decomposition time |
| 18 | Matrix solve time |
| 19 | Size of state vector |
| 20 | Parameter evaluation time |
| 21 | Matrix decomposition time (transient only) |
| 22 | Matrix solve time (transient only) |
| 23 | Circuit temperature |
| 24 | Circuit nominal temperature |
| 25 | Number of matrix fill-ins |
| 26 | Simulator initialisation time |
| 27 | Number of junction GMIN iterations |
| 28 | Time to process digital events |
| 29 | "Accept" time. This is the time used for processing transient time points after the simulator has accepted it. This includes the time taken to write out the data. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatorstats) | | |
| [◄ GetSimulatorOptions](func_getsimulatoroptions.htm) |  | [GetSimulatorStatus ▶](func_getsimulatorstatus.htm) |
