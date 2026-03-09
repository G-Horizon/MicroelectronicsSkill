# OptimiserGetOptions Function

Returns options for an optimiser definition

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

Return type: String array

6 element string array:

|  |  |
| --- | --- |
| 0 | Iteration limit. 0 if not defined |
| 1 | relative tolerance |
| 2 | absolute tolerance |
| 3 | show progress (1 enabled, 0 not enabled) |
| 4 | optimiser algorithm |
| 5 | auto create HTML report (1 enabled, 0 not enabled) |

Returns empty if ID invalid

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetoptions) | | |
| [◄ OptimiserGetIteration](func_optimisergetiteration.htm) |  | [OptimiserGetParameters ▶](func_optimisergetparameters.htm) |
