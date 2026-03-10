# OptimiserFinish Function

Instruct optimiser runtime session to terminate. This function can oly be used to stop a session started with OptimiserStart typically used for SIMPLIS simulations

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

Status. Returns 1 if optimiser was previously running otherwise returns 0. Returns -1 if definition invalid

### See Also

* [OptimiserRunning](func_optimiserrunning.htm)
* [OptimiserApplySpecification](func_optimiserapplyspecification.htm)
* [OptimiserApplyFailedRun](func_optimiserapplyfailedrun.htm)
* [OptimiserSuccess](func_optimisersuccess.htm)
* [OptimiserErrorMessage](func_optimisererrormessage.htm)
* [OptimiserStart](func_optimiserstart.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserfinish) | | |
| [◄ OptimiserErrorMessage](func_optimisererrormessage.htm) |  | [OptimiserGetDataObject ▶](func_optimisergetdataobject.htm) |
