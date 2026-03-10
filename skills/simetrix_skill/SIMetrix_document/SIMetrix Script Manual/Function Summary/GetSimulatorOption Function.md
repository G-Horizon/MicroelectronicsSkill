# GetSimulatorOption Function

Returns the value of a simulator option as used by the most recent analysis. The argument may be any one of the option names defined for the .OPTIONS control. E.g.

```
GetSimulatorOption('RELTOL')
```

will return the value of RELTOL for the most recent run. If the option value was not explicitly specified in a .OPTIONS control, its default value will be returned. If no simulation has been run, this function will return an empty string.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Option name |

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimulatoroption) | | |
| [◄ GetSimulatorMode](func_getsimulatormode.htm) |  | [GetSimulatorOptionInfo ▶](func_getsimulatoroptioninfo.htm) |
