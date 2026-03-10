# GetAxisCurves Function

Returns an array listing all curve id's for specified x or y-axis. All curves are referred to by a unique value that is the 'id'. Some functions and command require a curve id as an argument.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Y axis id |

### Returns

Return type: string array

Curve ids for curves attached to specified axis

### Notes

Compatibility: In version 8.1 and earlier, GetAxisCurves returns an empty vector if the specified axis is an x-axis.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getaxiscurves) | | |
| [◄ GetAnnotationText](func_getannotationtext.htm) |  | [GetAxisLimits ▶](func_getaxislimits.htm) |
