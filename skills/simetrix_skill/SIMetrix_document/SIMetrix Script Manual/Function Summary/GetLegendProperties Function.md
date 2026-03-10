# GetLegendProperties Function

Returns measurement names or values. These were called 'Legend properties' in versions 8.1 and earlier, hence the name of the function. From version 8.2, measurements are displayed in the measurement window and are graph objects with an id and properties. Although the underlying implementation of measurements has radically changed, this function nevertheless remains compatible with older versions, and is fully supported.

If argument 2 = 'values' the function returns legend property values. Otherwise it returns legend property names.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Curve ID |
| 2 | string | No | 'names' | Options |

### Returns

Return type: string array

### Notes

If the measurement refers to a multi-division curve, that is one created from a multi-step analysis such as Monte Carlo, the value returned by this function will the result of the first division only. This is compatible with the behaviour of version 8.1 and earlier. However, values for all divisions are calculated and available. These can be obtained by interrogating the properties of the measurement object. Use FindGraphMeasurement to obtain the measurement ID then read the 'Value' property using GetGraphObjPropValue(ID, 'value', 'array').

### See Also

* [FindGraphMeasurement](func_findgraphmeasurement.htm)
* [GetGraphObjPropValue](func_getgraphobjpropvalue.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlegendproperties) | | |
| [◄ GetLastGraphObjectAdded](func_getlastgraphobjectadded.htm) |  | [GetLibraryModels ▶](func_getlibrarymodels.htm) |
