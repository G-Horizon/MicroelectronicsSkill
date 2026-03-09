# GetSoaDefinitions Function

Returns all Safe Operating Area definitions specified in the most recent analysis.

### Arguments

No arguments

### Returns

Return type: string array

Returns an array of strings with each string in the form:

```
label;minvalue;maxvalue;xwindow;derating;type
```

Where:

|  |  |
| --- | --- |
| `label` | The label specification on the .SETSOA line |
| `minvalue` | Minimum value |
| `maxvalue` | Maximum value |
| `xwindow` | Window width - the time the limits must be exceeded for the violation to be recorded |
| `derating` | Derating factor |
| `type` | 'Peak' or 'Mean' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsoadefinitions) | | |
| [◄ GetSimulatorStatus](func_getsimulatorstatus.htm) |  | [GetSoaMaxMinResults ▶](func_getsoamaxminresults.htm) |
