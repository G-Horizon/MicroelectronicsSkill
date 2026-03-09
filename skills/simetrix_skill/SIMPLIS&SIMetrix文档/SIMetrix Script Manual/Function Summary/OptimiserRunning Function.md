# OptimiserRunning Function

Returns 1 when optimiser run is currently running. Returns 0 if complete or not started

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

Returns 1 if optimiser is running, 0 if is complete or not started. Returns -1 if ID is invalid

### See Also

* [OptimiserFinish](func_optimiserfinish.htm)
* [OptimiserApplySpecification](func_optimiserapplyspecification.htm)
* [OptimiserApplyFailedRun](func_optimiserapplyfailedrun.htm)
* [OptimiserSuccess](func_optimisersuccess.htm)
* [OptimiserErrorMessage](func_optimisererrormessage.htm)
* [OptimiserStart](func_optimiserstart.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserrunning) | | |
| [◄ OptimiserResults](func_optimiserresults.htm) |  | [OptimiserSimulatorGetDef ▶](func_optimisersimulatorgetdef.htm) |
