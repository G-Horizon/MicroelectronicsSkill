# GetModelParameters Function

Returns the names and types of all parameters for a device model.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Internal device name |
| 2 | string | No | Use internal device name | options |

#### Argument 1

Internal device name. This is returned by the functions  [GetInternalDeviceName](func_getinternaldevicename.htm)  and  [GetModelType](func_getmodeltype.htm) . If argument 2 is set to 'modelname' argument must be the model name of a model used in the most recent simulation

#### Argument 2

If set to 'modelname' argument 1 must be the name of a model used in the most recent simulation.

### Returns

Return type: string array

String array of semi-colon delimited strings. Each token in the string is defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | parameter name |
| 1 | Parameter type |
| 2 | Parameter description - this is blank for most devices |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmodelparameters) | | |
| [◄ GetModelParameterNames](func_getmodelparameternames.htm) |  | [GetModelParameterValues ▶](func_getmodelparametervalues.htm) |
