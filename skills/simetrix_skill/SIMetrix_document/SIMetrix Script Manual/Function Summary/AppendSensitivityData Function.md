# AppendSensitivityData Function

Appends new data to an existing sensitivity XML file.

Every sensitivity analysis generates an XML file that contains the results of evaluating the goal functions for each sensitivity case. If the data for the sensitivity analysis is still available, it is possible to add the results of further goal functions to the XML file after the sesensitivity analysis has completed. This makes it possible to perform worst-case analyses using goal functions that were not specified at the start of the sensitivity analysis.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Sensitivity XML file to process |
| 2 | String | Yes |  | Expression text and sensitivity id |
| 3 | Real array | Yes |  | Values to add to file |
| 4 | Real array | Yes |  | Case numbers |

#### Argument 1

Sensitivity XML file to process

#### Argument 2

Two element array. The first element provides the text for the expression evaluated. Note that this is used as a label and is not evaluated. The second element is the sensitivity id. If the resulting XML file is to be used as the input to a worst-case analysis, the sensid parameter on the worst-case analyiss line must match the sensitivity id provided here.

#### Argument 3

Array of values to add to XML file

#### Argument 4

Array of values providing case numbers. The number of items must match the number of values entered in argument 3

### Returns

Status: success: 1.0, fail: 0.0

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_appendsensitivitydata) | | |
| [◄ AddSymbolFiles](func_addsymbolfiles.htm) |  | [area ▶](func_area.htm) |
