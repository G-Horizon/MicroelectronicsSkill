# GraphLimits Function

Returns x and y limits of selected graph and axis type (log/linear). Function will fail if there are no selected graphs.

### Arguments

No arguments

### Returns

Return type: real array

The x and y axis limits of the currently selected graph and axis type. Meaning of each index of the 6 element array are as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | x-axis lower limit |
| 1 | x-axis upper limit |
| 2 | y-axis lower limit |
| 3 | y-axis upper limit |
| 4 | 1 if x-axis is logarithmic, 0 if linear |
| 5 | 1 if y-axis is logarithmic, 0 if linear |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_graphlimits) | | |
| [◄ GraphImageParameter](func_graphimageparameter.htm) |  | [GroupDelay ▶](func_groupdelay.htm) |
