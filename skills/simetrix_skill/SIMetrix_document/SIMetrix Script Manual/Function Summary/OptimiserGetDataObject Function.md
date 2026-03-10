# OptimiserGetDataObject Function

Get data for optimiser data object given optimiser definition ID nad data object name

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | String | Yes |  | Name of data object |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Name of data object

### Returns

Return type: Real vector

XY Vector containing both x-values and y-values for data object

### See Also

* [OptimiserGetDataObjectNames](func_optimisergetdataobjectnames.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetdataobject) | | |
| [◄ OptimiserFinish](func_optimiserfinish.htm) |  | [OptimiserGetDataObjectNames ▶](func_optimisergetdataobjectnames.htm) |
