# GetAxisType Function

This function is obsolete and should not be used for new code. To obtain the type of an axis (either X or Y) read the 'AxisType' property using  [GetGraphObjPropValue](func_getgraphobjpropvalue.htm) .

The concept of a 'Main' axis is not obsolete. In versions 8.1 and earlier the grid at the bottom of the graph was described as the 'Main axis' or 'Main grid'. Other grids were described as just 'Grids'. The main axis or grid could have multiple y-axes whereas the other grids supported just a single y-axis. This limitation no longer applies and all grids have equal functionality. So there is no longer a concept of a main axis. However, for compatibility with old code, this function will return 'Main' for the grid at the bottom of the graph.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Axis ID |

### Returns

Return type: string

Returns the type of axis. Possible values are:

|  |  |
| --- | --- |
| 'X' | X-axis |
| 'Digital' | A Digital Y-axis. (Created with `Curve /dig` or menu **Probe** > **Voltage - Digital...** ) |
| 'Main' | Main Y-axis (axes at bottom of graph) |
| 'Grid' | Grid Y-axis (axes stacked on top of main) |
| 'NotExist' | Axis does not exist |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getaxistype) | | |
| [◄ GetAxisLimits](func_getaxislimits.htm) |  | [GetAxisUnits ▶](func_getaxisunits.htm) |
