# GetCursorCurve Function

Returns curve id and source group name of curve attached to measurement cursor

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array of length 3 providing information on the curve attached to the measurement cursor. Returns an empty vector if cursors not enabled.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Curve id |
| 1 | Source group name. This is the group that was current when the curve was created. |
| 2 | Division index if curve is grouped. (E.g. for Monte Carlo) |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcursorcurve) | | |
| [◄ GetCurrentStepValue](func_getcurrentstepvalue.htm) |  | [GetCurveAxes ▶](func_getcurveaxes.htm) |
