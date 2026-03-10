# GetGridCurves Function

Returns ids of all curves in the specified Grid. Grids are sections of a graph that contains one or more horizontally stacked Y-axes and one or more vertically stacked X-axes.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  |  |

#### Argument 1

Grid id

### Returns

Return type: string array

Curve ids

### Notes

The curves belonging to a specified grid may also be obtained by reading the Grid's Curves property using the function call: GetGraphObjPropValue(ID, 'curves', 'array'). See  [GetGraphObjPropValue](func_getgraphobjpropvalue.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgridcurves) | | |
| [◄ GetGridAxes](func_getgridaxes.htm) |  | [GetGroupAnalysisInfo ▶](func_getgroupanalysisinfo.htm) |
