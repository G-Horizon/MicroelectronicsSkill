# GetModelType Function

Returns internal device name given user model name. The internal device name is a name used internally by the simulator and is required by some functions. See  [GetInternalDeviceName](func_getinternaldevicename.htm)  for full details. The user model name is the name of a model parameter set defined using .MODEL. E.g. 'Q2N2222'.

Important: this function only works for models used by the current simulation. That is, you must run or check a simulation on a netlist that uses the specified model before calling this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Model name |

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmodeltype) | | |
| [◄ GetModelParameterValues](func_getmodelparametervalues.htm) |  | [GetModifiedStatus ▶](func_getmodifiedstatus.htm) |
