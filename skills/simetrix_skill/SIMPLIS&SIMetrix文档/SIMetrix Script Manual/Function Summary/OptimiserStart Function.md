# OptimiserStart Function

Start optimiser run. This function is used for running optimisation for the SIMPLIS simulator. This function creates the runtime environment needed to run an optimisation session.

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

Status. Rteurn 1 if successful, 0 on failure

### See Also

* [OptimiserRunning](func_optimiserrunning.htm)
* [OptimiserApplySpecification](func_optimiserapplyspecification.htm)
* [OptimiserApplyFailedRun](func_optimiserapplyfailedrun.htm)
* [OptimiserSuccess](func_optimisersuccess.htm)
* [OptimiserErrorMessage](func_optimisererrormessage.htm)
* [OptimiserFinish](func_optimiserfinish.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserstart) | | |
| [◄ OptimiserSimulatorWriteXMLString](func_optimisersimulatorwritexmlstring.htm) |  | [OptimiserStatus ▶](func_optimiserstatus.htm) |
