# OptimiserGetInfo Function

Get optimiser file information

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

### Returns

Return type: String array

|  |  |
| --- | --- |
| 0 | Path to attached schenmatic |
| 1 | Path to results file |
| 2 | Path to definition file |

Returns an empty vector if ID invalid

### See Also

* [OptimiserSimulatorGetInfo](func_optimisersimulatorgetinfo.htm)
* [OptimiserWidgetGetInfo](func_optimiserwidgetgetinfo.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetinfo) | | |
| [◄ OptimiserGetDataObjectNames](func_optimisergetdataobjectnames.htm) |  | [OptimiserGetIteration ▶](func_optimisergetiteration.htm) |
