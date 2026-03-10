# OptimiserErrorMessage Function

Returns string showing error message returned by a filed optimiser run

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

Optimiser error message. Empty if optimiser definition ID is invalid.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisererrormessage) | | |
| [◄ OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm) |  | [OptimiserFinish ▶](func_optimiserfinish.htm) |
