# DelLegendProp Command

Delete a graph measurement object defined by its curve and label property.

In version 8.1 and earlier, measurement values were displayed below the curve's legend and were referred to as "Legend Properties". From version 8.2, these have been replaced by Measurement objects. Measurement objects are more advanced and have greater functionality but may perform the same function as the older legend properties.

DelLegendProp can be used to delete a measurement object defined by its associated curve and label property.

Measurement objects may be deleted directly using DeleteGraphObject

```
DelLegendProp <curve-id> <legend-name>
```

### Parameters

|  |  |
| --- | --- |
| curve-id | Id of curve, histogram or scatter plot which possesses property. Curve id is returned by the functions  [GetSelectedCurves](func_getselectedcurves.htm)  ,  [GetAxisCurves](func_getaxiscurves.htm)  and  [GetAllCurves](func_getallcurves.htm) . |
| property-name | Name of property to be deleted. The function  [GetLegendProperties](func_getlegendproperties.htm)  returns legend properties owned by a specified curve. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_dellegendprop) | | |
| [◄ DelGroup](com_delgroup.htm) |  | [DelMenu ▶](com_delmenu.htm) |
