# GetGridAxes Function

Returns ids of all axes in the specified Grid. Grids are sections of a graph that contains one or more horizontally stacked Y-axes and one or more vertically stacked X-axes.

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

This function returns all axes both X and Y. These can also be obtained from the XAxes and YAxes properties of the Grid object. For example to get the y-axes use function call GetGraphObjPropValue(ID, 'yaxes', 'array'). See  [GetGraphObjPropValue](func_getgraphobjpropvalue.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgridaxes) | | |
| [◄ GetGraphTitle](func_getgraphtitle.htm) |  | [GetGridCurves ▶](func_getgridcurves.htm) |
