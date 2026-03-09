# GetSimulatorOptions Function

Return list of simulator options

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Output option |

#### Argument 1

Can optionally be set to 'default' or 'type'. If set to 'default', function returns the default value instead of the name. If set to type, returns the type of the option - one of 'real', 'integer', 'boolean' or 'string'

### Returns

Array of strings holding names of all available options that can be set using the .OPTIONS statement. Optionally can return default value or type according to argument 2.

### See Also

* [GetSimulatorOptionInfo](func_getsimulatoroptioninfo.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatoroptions) | | |
| [◄ GetSimulatorOptionInfo](func_getsimulatoroptioninfo.htm) |  | [GetSimulatorStats ▶](func_getsimulatorstats.htm) |
