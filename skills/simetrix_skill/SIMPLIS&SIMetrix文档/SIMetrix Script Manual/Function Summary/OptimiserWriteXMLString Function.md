# OptimiserWriteXMLString Function

Returns an optimiser XML definition as a string. The optimiser definition including its parameters, analyses and measurements can be described using an XML based definition.

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

Return type: String

Complete optimiser XML definition. Returns empty if ID invalid

### See Also

* [OptimiserWriteXML](func_optimiserwritexml.htm)
* [OptimiserSimulatorWriteXMLString](func_optimisersimulatorwritexmlstring.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserwritexmlstring) | | |
| [◄ OptimiserWriteXML](func_optimiserwritexml.htm) |  | [Parse ▶](func_parse.htm) |
