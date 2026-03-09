# OptimiserGetParameters Function

Returns parameter definition from an optimiser definition

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

String array with one element for each parameter. Each element is a semi-colon delimited string with four fields:

|  |  |
| --- | --- |
| 0 | Parameter name |
| 1 | Initialvalue |
| 2 | Minimum value or empty if no minimum defined |
| 3 | Maximum value or empty if no maximum defined |

Returns an empty vector if ID invalid

### See Also

* [OptimiserGetSpecification](func_optimisergetspecification.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_optimisergetparameters) | | |
| [◄ OptimiserGetOptions](func_optimisergetoptions.htm) |  | [OptimiserGetParameterValues ▶](func_optimisergetparametervalues.htm) |
