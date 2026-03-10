# AddLegendProp Command

Creates a measurement object that is compatible with legend properties used in older versions of SIMetrix.

In version 8.1 and earlier, measurement values were displayed below the curve's legend and were referred to as "Legend Properties". From version 8.2, these have been replaced by Measurement objects. Measurement objects are more advanced and have greater functionality but may perform the same function as the older legend properties.

The AddLegendProp command creates a measurement object that displays the same information as a legend property and is in all respects compatible with version 8.1 and earlier.

AddLegendProp creates a Measurement object with a Label property equal to the Name and a Template property equal to the Value. The Expression property will be empty.

This command is intended to keep old code working. New scripts should use the function  [CreateGraphMeasurement](func_creategraphmeasurement.htm) .

```
AddLegendProp <curveId> <property-name> <property-value>
```

### Parameters

|  |  |
| --- | --- |
| curveId | The curve ID. Curve id is returned by the functions  [GetSelectedCurves](func_getselectedcurves.htm)  ,  [GetAxisCurves](func_getaxiscurves.htm)  and  [GetAllCurves](func_getallcurves.htm) . |
| property-name | Name of property. May be any string and may contain spaces. |
| property-value | Value of property. May be any string and may contain spaces. |

### See Also

* [CreateGraphMeasurement](func_creategraphmeasurement.htm)
* [EditGraphMeasurement](func_editgraphmeasurement.htm)
* [FindGraphMeasurement](func_findgraphmeasurement.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addlegendprop) | | |
| [◄ AddLegend](com_addlegend.htm) |  | [AddPin ▶](com_addpin.htm) |
