# GetModelName Function

Returns the model name used by an instance. The model name is the name for the parameter set (e.g. 'QN2222') as opposed to 'model type name' (e.g. 'npn') and 'internal device name' (e.g. 'BJT').

Note that all simulator devices use a model even if it is not possible for the device to use a .MODEL statement. Inductors, for example. are not permitted a .MODEL control but they nevertheless all refer to an internal model which is always called '$Inductor'.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Instance name |

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmodelname) | | |
| [◄ GetModelLibraryErrors](func_getmodellibraryerrors.htm) |  | [GetModelParameterNames ▶](func_getmodelparameternames.htm) |
