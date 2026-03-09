# GetConvergenceInfo Function

Return convergence data for most recent simulation

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array providing convergence information about the most recent run. Each element of the array is a list of values separated by semi-colons. The output may be pasted into a spreadsheet program that has been set up to interpret a semicolon as a column separator. The first element of the array lists the names for each column and therefore provides a heading. The following headings are currently in use:

|  |  |
| --- | --- |
| type | Node or Device |
| name | Name of node or device that failed to converge count Number of times node/device failed to converge during run |
| time (first step) | Time of most recent occurrence of a 'first step' failure. |
| required tol | Required tolerance for most recent 'first step' failure |
| actual tol | Tolerance actually achieved for most recent 'first step' failure |
| absolute val | Absolute value for most recent 'first step' failure |
| time (cut back step) | Time of most recent occurrence of a 'cut back step' failure. |
| required tol | Required tolerance for most recent 'cut back step' failure |
| actual tol | Tolerance actually achieved for most recent 'cut back step' failure |
| absolute val | Absolute value for most recent 'cut back step' failure |
| final? | Node or device failed on the final step that caused the simulation to abort |
| top analysis | Main analysis mode (Tran, DC etc.) |
| current analysis | Current analysis. Either the same as 'top analysis' or Op |
| op mode | Method being used for operating point. (PTA, JI2, GMIN or SOURCE) |

A  *first step*  failure is a failure that occurred at the first attempt at a time step after a previously successful step. If a time point fails, the time step is cut back and further iterations are made. Failures on steps that have been cut back are referred to in the above table as  *cut back steps* . Quite often the nodes or devices that fail on a  *cut back step*  are quite different from the nodes or devices that fail on a first step. The root cause of a convergence failure will usually be at the nodes or devices that fail on a  *first step* .

It is quite difficult to interpret the information provided by this function. The 'where' script performs a simple analysis and sometimes displays the nodes or devices most likely to be the cause.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getconvergenceinfo) | | |
| [◄ GetConvergenceDevNames](func_getconvergencedevnames.htm) |  | [GetConvergenceNodeNames ▶](func_getconvergencenodenames.htm) |
