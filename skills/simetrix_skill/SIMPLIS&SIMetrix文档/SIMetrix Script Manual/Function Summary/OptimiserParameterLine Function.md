# OptimiserParameterLine Function

Gets parameter line for current optimiser iteration

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

Return type: String

Semicolon delimited string. Each element in form name=value giving the current value for each optimiser parameter.

Returns empty if the ID is invalid or if the optimiser is not running.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserparameterline) | | |
| [◄ OptimiserLoadWidgetFromXML](func_optimiserloadwidgetfromxml.htm) |  | [OptimiserResults ▶](func_optimiserresults.htm) |
