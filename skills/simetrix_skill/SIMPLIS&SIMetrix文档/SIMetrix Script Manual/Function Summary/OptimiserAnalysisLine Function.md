# OptimiserAnalysisLine Function

Returns optimiser analysis lines

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

Returns an array with each element containing one optimiser analysis line. The final element holds any options line present in the definition. If there are no options lines, the final element will be an empty string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiseranalysisline) | | |
| [◄ OpenSchematic](func_openschematic.htm) |  | [OptimiserApplyFailedRun ▶](func_optimiserapplyfailedrun.htm) |
