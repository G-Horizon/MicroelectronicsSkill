# OptimiserGetIteration Function

Returns data from a single optimiser iteration

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | Real | Yes |  | Iteration index |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Iteration index

### Returns

Real array with results in three groups:

First group: parameter values

Second group: measurement values

Third group: Constraint pass/fail for each measurement. 1.0 for pass 0.0 for fail. Includes objective which is always 1.0

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetiteration) | | |
| [◄ OptimiserGetInfo](func_optimisergetinfo.htm) |  | [OptimiserGetOptions ▶](func_optimisergetoptions.htm) |
