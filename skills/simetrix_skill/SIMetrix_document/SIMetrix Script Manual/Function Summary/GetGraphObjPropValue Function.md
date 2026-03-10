# GetGraphObjPropValue Function

Returns property values for the specified object. If argument 2 is present the value of one particular property will be returned. Otherwise the function will return an array containing all property values. The order of the values corresponds to the return value of  [GetGraphObjPropNames](func_getgraphobjpropnames.htm) .

If argument 3 is set to 'array', any array properties will be output as a string array. Otherwise the array values will be composed into a single string in the form:

[ val1, val1, ...]

See  [Graph Objects](applications_graphobjects.htm)  for more information.

(Note the function GetGraphObjPropValues is the same but will only accept one argument)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Graph object ID |
| 2 | string | No | Return all values | Property name |
| 3 | string | No |  | Options |

### Returns

Return type: string array

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 |  |

### See Also

* [GetGraphObjPropValues](func_getgraphobjpropvalues.htm)
* [GetGraphObjects](func_getgraphobjects.htm)
* [GetCurrentGraph](func_getcurrentgraph.htm)
* [GetGraphObjPropNames](func_getgraphobjpropnames.htm)
* [GetSelectedGraphAnno](func_getselectedgraphanno.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgraphobjpropvalue) | | |
| [◄ GetGraphObjPropNames](func_getgraphobjpropnames.htm) |  | [GetGraphObjPropValues ▶](func_getgraphobjpropvalues.htm) |
