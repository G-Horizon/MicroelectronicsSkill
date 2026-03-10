# GetGroupStepVals Function

Returns the 'stepped values' in a multi-step run. These values are stored within the group created for the simulation run's output data. The stepped values are the values assigned to the 'stepped parameters' (see the function  [GetGroupStepParameter](func_getgroupstepparameter.htm)  ) during a multi-step run.

If there is more than one stepped parameter, the second argument may be used to identify for which parameter the values are returned.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Current group | Group name |
| 2 | real | No | 0 | index |

#### Argument 2

Identifies parameter when there is more than one

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgroupstepvals) | | |
| [◄ GetGroupStepParameter](func_getgroupstepparameter.htm) |  | [GetGUID ▶](func_getguid.htm) |
