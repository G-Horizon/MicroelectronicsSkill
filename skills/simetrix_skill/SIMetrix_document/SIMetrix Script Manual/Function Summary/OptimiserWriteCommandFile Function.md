# OptimiserWriteCommandFile Function

Create SIMetrix simulator command file from optimiser definition. The optimiser definition describes the parameters, analyses and measurements to run an optimisation analysis. The SIMetrix simulator uses a number of netlist commands to describe the analysis. This function generates those commands from an optimiser definition.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | String | Yes |  | Filename to receive simulator commands |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Filename to receive simulator commands

### Returns

Return type: Real

Error code:

|  |  |
| --- | --- |
| -1 | ID invalid |
| 0 | Funcion completed successfully |
| 1 | Cannot open file |
| 2 | Optimiser definition ID invalid |
| 3 | Cannot open file and Optimiser definition ID invalid |
| 4 | No analyses defined in definition |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserwritecommandfile) | | |
| [◄ OptimiserWidgetWriteXMLString](func_optimiserwidgetwritexmlstring.htm) |  | [OptimiserWriteHTMLReport ▶](func_optimiserwritehtmlreport.htm) |
