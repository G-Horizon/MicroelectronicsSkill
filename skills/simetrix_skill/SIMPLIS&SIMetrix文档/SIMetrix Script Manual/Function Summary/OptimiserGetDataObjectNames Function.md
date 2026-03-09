# OptimiserGetDataObjectNames Function

Returns names of all data objects in an optimiser definition. Name can be used as an argument to  [OptimiserGetDataObject](func_optimisergetdataobject.htm)  to get actual data. Note that data objects are not stored in results files nor in the optimiser definition returned by the simulator (using  [OptimiserSimulatorWriteXMLString](func_optimisersimulatorwritexmlstring.htm)  )

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

List of names. Returns an empty vector if ID invalid

### See Also

* [OptimiserGetDataObject](func_optimisergetdataobject.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetdataobjectnames) | | |
| [◄ OptimiserGetDataObject](func_optimisergetdataobject.htm) |  | [OptimiserGetInfo ▶](func_optimisergetinfo.htm) |
