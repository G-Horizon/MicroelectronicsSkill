# GetGraphObjects Function

Returns a list of IDs for the graph objects defined by the optional arguments as follows:

If no arguments are specified, the IDs for all graph objects for all graph sheets are returned.

If the first argument is specified, all objects of the defined type for all graph sheets will be returned.

If both arguments are specified, all objects of the defined type and located on the specified graph will be returned.

If the type name is invalid, or if the graph id specified in arg 2 is invalid or if there are no graphs open, the function will return an empty vector.

See  [Graph Objects](applications_graphobjects.htm)  for information on graph objects.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Object type name |
| 2 | string | No | Current graph | Graph ID |
| 3 | string | No |  | Options |

#### Argument 3

Set to 'selected' to return selected objects only

### Returns

Return type: string array

### See Also

* [GetGraphObjPropValues](func_getgraphobjpropvalues.htm)
* [GetGraphObjPropValue](func_getgraphobjpropvalue.htm)
* [GetCurrentGraph](func_getcurrentgraph.htm)
* [GetGraphObjPropNames](func_getgraphobjpropnames.htm)
* [GetSelectedGraphAnno](func_getselectedgraphanno.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgraphobjects) | | |
| [◄ GetGraphFromWindow](func_getgraphfromwindow.htm) |  | [GetGraphObjectsWithProperty ▶](func_getgraphobjectswithproperty.htm) |
