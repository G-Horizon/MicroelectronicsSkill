# OptimiserSuccess Function

Returns 1 if optimiser run has completed successfully

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

Return type: Real

Returns 1 if optimiser run has completed successfully, 0 if unsuccessful and -1 if ID not recognised

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisersuccess) | | |
| [◄ OptimiserStatus](func_optimiserstatus.htm) |  | [OptimiserUserMessage ▶](func_optimiserusermessage.htm) |
