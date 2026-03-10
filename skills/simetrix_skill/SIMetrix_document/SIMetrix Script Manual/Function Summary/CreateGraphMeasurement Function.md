# CreateGraphMeasurement Function

Creates a graph measurement object. Measurement objects are visible in the measurement window. Typically they display scalar measurements on whole curves.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | Yes |  | Curve ID and, optionally, graph ID |
| 2 | String array | No | All values empty | Values for Label, Expression and Template |

#### Argument 1

First element is the ID of the associated curve. Optional second element specifies a graph ID. If omitted, the measurement object is placed in the currently selected graph.

#### Argument 2

String array with up to three elements providing values for the Label, Expression and Template properties

### Returns

Return type: String

ID of measurement created. Result will be empty if the specified curve does not exist or if the specified graph, if any, does not exist.

### See Also

* [EditGraphMeasurement](func_editgraphmeasurement.htm)
* [FindGraphMeasurement](func_findgraphmeasurement.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_creategraphmeasurement) | | |
| [◄ CreateDiodeDialog](func_creatediodedialog.htm) |  | [CreateLockFile ▶](func_createlockfile.htm) |
