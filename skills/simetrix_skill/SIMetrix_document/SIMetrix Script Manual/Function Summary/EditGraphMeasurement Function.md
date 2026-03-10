# EditGraphMeasurement Function

Edits the Label, Expression and Template properties of a measurement object.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Measurement object ID |
| 2 | String array | Yes |  | New values for Label, Expression and Template properties |

#### Argument 1

Measurement object ID

#### Argument 2

String array with up to three values providing new values for Label, Expression and Template properties respectively

### Returns

Return type: Real

1 if successful. 0 if provided ID is invalid

### See Also

* [CreateGraphMeasurement](func_creategraphmeasurement.htm)
* [FindGraphMeasurement](func_findgraphmeasurement.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editgraphmeasurement) | | |
| [◄ EditFreeTextDialog](func_editfreetextdialog.htm) |  | [EditGraphTextBoxDialog ▶](func_editgraphtextboxdialog.htm) |
