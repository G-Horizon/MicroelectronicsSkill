# OptimiserUserMessage Function

Returns a string providing the current state of a running optimiser for display to the user. The message includes the current iteration number, parameter values and resulting measurements

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

String giving current iteration number, parameter values and resulting measurements. Empty if optimiser definition ID is invalid

### See Also

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserusermessage) | | |
| [◄ OptimiserSuccess](func_optimisersuccess.htm) |  | [OptimiserWidgetCreateOptDef ▶](func_optimiserwidgetcreateoptdef.htm) |
