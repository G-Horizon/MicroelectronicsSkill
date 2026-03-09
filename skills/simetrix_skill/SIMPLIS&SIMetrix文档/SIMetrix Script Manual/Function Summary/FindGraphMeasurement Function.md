# FindGraphMeasurement Function

Returns graph measurement objects that match a provided curve ID and, optionally, a Label value

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String Array | Yes |  | Curve ID |
| 2 | String | No | Matches any label | Measurement label |

#### Argument 1

ID of curve associated with measurement objects

#### Argument 2

Measurement label

### Returns

Return type: String array

IDs of measurement objects that are associated with the provided curve ID. If the Label value is provided, only those objects matching the label will be returned

### See Also

* [CreateGraphMeasurement](func_creategraphmeasurement.htm)
* [EditGraphMeasurement](func_editgraphmeasurement.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_findgraphmeasurement) | | |
| [◄ FinalDivision](func_finaldivision.htm) |  | [FindModel ▶](func_findmodel.htm) |
