# GetSimulatorOptionInfo Function

Returns type and default value of a simulator option setting

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | option name |

### Returns

Return type: string array

Array of strings providing the following information

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Option name |
| 1 | Type - can be 'REAL', 'INTEGER', 'BOOL', 'STRING' or 'UNKNOWN' |
| 2 | Default value |

### Notes

This function differs from  [GetSimulatorOption](func_getsimulatoroption.htm)  in that it returns information about an option setting independent of any simulation.  [GetSimulatorOption](func_getsimulatoroption.htm)  returns the value an option was set to in the most recent simulation.

### See Also

* [GetSimulatorOptions](func_getsimulatoroptions.htm)
* [GetSimulatorOption](func_getsimulatoroption.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatoroptioninfo) | | |
| [◄ GetSimulatorOption](func_getsimulatoroption.htm) |  | [GetSimulatorOptions ▶](func_getsimulatoroptions.htm) |
