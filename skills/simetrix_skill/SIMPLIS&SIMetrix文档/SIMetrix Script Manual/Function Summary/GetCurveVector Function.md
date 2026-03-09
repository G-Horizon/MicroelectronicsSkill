# GetCurveVector Function

Returns the data for a curve.

For a single curve (i.e. not a group of curves as created from a Monte Carlo plot) only the first argument is required and this specifies the curve's id.

If the curve id refers to a group of curves created by a multi-step run, then the second argument may be used to identify a single curve within the group. The data for the complete curve set is arranged as a  [Multi Division Vector](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__multidivisionvectors) . The second argument specifies the division index. If absent the entire vector is returned

Note that the arguments to this function for version 4 and later have changed from earlier versions.

The function  [cv](func_cv.htm)  is identical to this function and is convenient in situations where a short expression is desirable.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | curve id |
| 2 | real | No | Return all divisions | Division index |
| 3 | string | No |  | Obsolete - no longer used |

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcurvevector) | | |
| [◄ GetCurves](func_getcurves.htm) |  | [GetDatumCurve ▶](func_getdatumcurve.htm) |
