# OptimiserApplyFailedRun Function

Notify optimiser that a simulation run failed. Currently this will abort the optimisation process.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | String | No | Nomessage | Error message |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Error message which will be recorded in final report

### Returns

Return type: Real array

2 element array with both values set to zero

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserapplyfailedrun) | | |
| [◄ OptimiserAnalysisLine](func_optimiseranalysisline.htm) |  | [OptimiserApplySpecification ▶](func_optimiserapplyspecification.htm) |
