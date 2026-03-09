# OptimiserGetSpecification Function

Returns details of all analyses and specifications for an optimiser definition

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

Array of strings providing analysis definitions along with all measurements. Definition as follows:

|  |  |
| --- | --- |
| 0 | Number of analyses |
| 1 | Number of specifications |
| Next num\_analyses elements | semi-colon delimited string in form analysis\_id;analysis\_line |
| Next num\_measurements elements | semi-colon delimited string in form analysis\_id ; label ; expression ; value ; tolerance |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetspecification) | | |
| [◄ OptimiserGetParameterValues](func_optimisergetparametervalues.htm) |  | [OptimiserLoadWidgetFromXML ▶](func_optimiserloadwidgetfromxml.htm) |
