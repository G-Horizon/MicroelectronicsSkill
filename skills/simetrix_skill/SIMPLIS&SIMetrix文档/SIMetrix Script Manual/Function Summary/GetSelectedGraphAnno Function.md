# GetSelectedGraphAnno Function

Obsolete - for new code use  [GetSelectedGraphAnnotations](func_getselectedgraphannotations.htm) . Returns the ID for a single selected graph annotation object. If no objects are selected, the function returns '-1'. If no graphs are open, the function returns an empty vector.

If multiple objects are selected, the function will return the id of just one of them. To get all selected annotation objects, use the function  [GetSelectedGraphAnnotations](func_getselectedgraphannotations.htm) .

See  [Graph Objects](applications_graphobjects.htm)  for information on graph annotation objects.

### Arguments

No arguments

### Returns

Return type: string

### Notes

Compatibility: Version 8.1 and earlier only allowed a single object to be selected so this function always returned a scalar value

### See Also

* [GetSelectedGraphAnnotations](func_getselectedgraphannotations.htm)
* [GetGraphObjPropValues](func_getgraphobjpropvalues.htm)
* [GetGraphObjPropValue](func_getgraphobjpropvalue.htm)
* [GetGraphObjects](func_getgraphobjects.htm)
* [GetCurrentGraph](func_getcurrentgraph.htm)
* [GetGraphObjPropNames](func_getgraphobjpropnames.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getselectedgraphanno) | | |
| [◄ GetSelectedCurves](func_getselectedcurves.htm) |  | [GetSelectedGraphAnnotations ▶](func_getselectedgraphannotations.htm) |
