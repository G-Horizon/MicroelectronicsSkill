# OptimiserApplySpecification Function

Evaluates measurements for specified optimiser definition and passes results to the optimiser. Assumes that optimiser session was started with  [OptimiserStart](func_optimiserstart.htm)  and also assumes that all analysis IDs were specified on analysis lines. This is automatically handled for SIMPLIS simulations as long as the optimiser ID is passed to the PreProcessNetlist command using the /optid switch

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

Return type: Real array

Real array

|  |  |
| --- | --- |
| 0 | number of measurements (0 if measurements failed) |
| 1 | 1: measurements Ok, 0: measurements failed |
| next num\_measurements : 1:measurement OK, 0:measurement failed |  |
| next num\_measurements : Measurement values |  |

Returns empty if ID invalid or if optimiser is not running

### See Also

* [OptimiserFinish](func_optimiserfinish.htm)
* [OptimiserRunning](func_optimiserrunning.htm)
* [OptimiserApplyFailedRun](func_optimiserapplyfailedrun.htm)
* [OptimiserSuccess](func_optimisersuccess.htm)
* [OptimiserErrorMessage](func_optimisererrormessage.htm)
* [OptimiserStart](func_optimiserstart.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserapplyspecification) | | |
| [◄ OptimiserApplyFailedRun](func_optimiserapplyfailedrun.htm) |  | [OptimiserCloseDef ▶](func_optimiserclosedef.htm) |
