# OptimiserResults Function

Returns information about the results of an optimiser run

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
| 0 | Order (i.e. number of parameters) |
| 1 | Number of measurements |
| 2 | Iteration number of best result |
| 3 | Value of objective function for best result |
| 4 | 1: complete, 0:not complete |
| 5 | number of iterations |
| next order | parameter values |
| next measurement count | measurement values |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserresults) | | |
| [◄ OptimiserParameterLine](func_optimiserparameterline.htm) |  | [OptimiserRunning ▶](func_optimiserrunning.htm) |
