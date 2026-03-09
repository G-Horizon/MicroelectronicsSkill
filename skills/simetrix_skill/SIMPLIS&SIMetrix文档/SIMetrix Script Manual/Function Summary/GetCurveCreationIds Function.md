# GetCurveCreationIds Function

The commands  [Plot](com_plot.htm)  ,  [Curve](com_curve.htm)  and  [NewPlot](com_newplot.htm)  usually create new graph objects. This function returns the IDs of those objects.

### Arguments

No arguments

### Returns

Return type: Real array

Five element real array containing the IDs of the following objects

* 0: Graph ID
* 1: Grid ID
* 2: X-Axis ID
* 3: Y-Axis ID
* 4: Curve ID

If no Plot, Curve or NewPlot command has been called, or the most recent call failed, the return values from this function will all be zero.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcurvecreationids) | | |
| [◄ GetCurveAxis](func_getcurveaxis.htm) |  | [GetCurveName ▶](func_getcurvename.htm) |
