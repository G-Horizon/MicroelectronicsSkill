# OptimiserCloseDef Function

Deletes an optimiser object defined by its ID. Note that this deletes the ID and does not necessarily delete the object that created it. For example,  [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)  returns an ID providing details of the current state of the simulator's optimiser. Calling OptimiserCloseDef on that ID will not destroy the simulator's optimiser it only destroys the data that was generated from that optimiser.

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

Returns 1 if object existed and was successfully deleted otherwise returns 0. A return value of 0 usually means that the ID was not valid.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserclosedef) | | |
| [◄ OptimiserApplySpecification](func_optimiserapplyspecification.htm) |  | [OptimiserCreateFromXML ▶](func_optimisercreatefromxml.htm) |
