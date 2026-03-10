# OptimiserWriteXML Function

Writes out an optimiser definition to a file in XML format. The optimiser definition including its parameters, analyses and measurements can be described using an XML based definition. This function writes out that definition to a file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | String | Yes |  | Filename |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Filename to receive XML definition

### Returns

Return type: Real

Status: 1.0 success, 0.0 save failed, -1.0 ID not recognised

### See Also

* [OptimiserWriteXMLString](func_optimiserwritexmlstring.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserwritexml) | | |
| [◄ OptimiserWriteHTMLReport](func_optimiserwritehtmlreport.htm) |  | [OptimiserWriteXMLString ▶](func_optimiserwritexmlstring.htm) |
