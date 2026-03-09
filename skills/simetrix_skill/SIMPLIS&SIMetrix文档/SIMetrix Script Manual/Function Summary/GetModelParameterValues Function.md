# GetModelParameterValues Function

Returns the values of all parameters of the specified model. (Defined by 'model name' e.g. 'Q2N2222'). This function reads the values from the simulator and requires that a simulation has been run or checked. The returned array with arg2 omitted is of the same size as the array returned by  [GetModelParameterNames](func_getmodelparameternames.htm)  for the same device and the values and parameter names map directly.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Model name |
| 2 | string | No | All values returned if omitted | Parameter name |

#### Argument 1

Model name. (Model name is the user name for a model parameter set as defined in the.MODEL control e.g. 'Q2N2222').

#### Argument 2

Parameter name. If specified return value will be a single value for the specified parameter. If omitted, the values for all parameters will be returned.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmodelparametervalues) | | |
| [◄ GetModelParameters](func_getmodelparameters.htm) |  | [GetModelType ▶](func_getmodeltype.htm) |
