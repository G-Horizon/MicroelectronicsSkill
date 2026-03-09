# GetAxisLimits Function

Returns min and max limits and axis type (log or lin) of specified axis

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Axis ID |

### Returns

Return type: real array

Returns array of length 3 providing limits info for specified axis.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Minimum limit |
| 1 | Maximum limit |
| 2 | Axis scale type - 0 = linear, 1 = logarithmic |
| 3 | Fixed or auto. 0 = fixed, 1 = auto |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getaxislimits) | | |
| [◄ GetAxisCurves](func_getaxiscurves.htm) |  | [GetAxisType ▶](func_getaxistype.htm) |
