# OptimiserGetParameterValues Function

Gets parameter values for current optimiser iteration

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

Array of parameter values for current iteration in same order as  [OptimiserGetParameters](func_optimisergetparameters.htm) .

Returns empty if the ID is invalid or if the optimiser is not running.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetparametervalues) | | |
| [◄ OptimiserGetParameters](func_optimisergetparameters.htm) |  | [OptimiserGetSpecification ▶](func_optimisergetspecification.htm) |
