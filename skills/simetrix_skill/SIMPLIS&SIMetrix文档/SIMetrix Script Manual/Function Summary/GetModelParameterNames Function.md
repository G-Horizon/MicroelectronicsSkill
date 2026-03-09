# GetModelParameterNames Function

Returns the names or default values of all real valued parameters for a device model.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Internal device name |
| 2 | string | No |  | default flag (unsupported) |

#### Argument 1

Internal device name. This is returned by the functions  [GetInternalDeviceName](func_getinternaldevicename.htm)  and  [GetModelType](func_getmodeltype.htm) .

#### Argument 2

If a second argument is supplied set to 'default', the function will instead return the default values used for the device's parameter names. This doesn't work correctly for all simulator devices and so is currently unsupported.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmodelparameternames) | | |
| [◄ GetModelName](func_getmodelname.htm) |  | [GetModelParameters ▶](func_getmodelparameters.htm) |
