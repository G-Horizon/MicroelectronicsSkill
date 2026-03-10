# OptimiserWriteHTMLReport Function

Creates a human-readable HTML report file from an optimiser definition. Usually, the optimiser definition would have been created from the optimiser results file. The results file is an XML file that contains the definition information along with results including the data for each iteration and the final result.

The results file is automatically generated for each optimiser run. The path of the file can be obtained from  [OptimiserGetInfo](func_optimisergetinfo.htm)  or  [OptimiserSimulatorGetInfo](func_optimisersimulatorgetinfo.htm) . This file can then be loaded using  [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)  and the resulting ID used for argument 1.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Optimiser definition ID |
| 2 | String | Yes |  | Path of file to receive HTML content |
| 3 | String | No | An internal default style will be used | CSS file |

#### Argument 1

ID reference to optimiser definition as returned by functions:

* [OptimiserCreateFromXMLString](func_optimisercreatefromxmlstring.htm)
* [OptimiserCreateFromXML](func_optimisercreatefromxml.htm)
* [OptimiserWidgetCreateOptDef](func_optimiserwidgetcreateoptdef.htm)
* [OptimiserSimulatorGetDef](func_optimisersimulatorgetdef.htm)

#### Argument 2

Path of file to receive HTML content

#### Argument 3

CSS file containing style information for the HTML content.

CSS style names:

|  |  |
| --- | --- |
| datatable | General styles used for table containing iteration data |
| headertable | General styles used for table at top of report |
| opt\_expression | Style for table column holding the expression |
| opt\_none | Style for text showing values that are defined as report-only |
| opt\_constraint\_pass | Style for text showing constraint values that passed |
| opt\_constraint\_fail | Styke for text showing constraint values that failed |

The CSS file may also define h1, h2 and p tags used in the HTML document

### Returns

Return type: Real

Status. 1 for success, 0 failure, -1 definition not recognised

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimiserwritehtmlreport) | | |
| [◄ OptimiserWriteCommandFile](func_optimiserwritecommandfile.htm) |  | [OptimiserWriteXML ▶](func_optimiserwritexml.htm) |
