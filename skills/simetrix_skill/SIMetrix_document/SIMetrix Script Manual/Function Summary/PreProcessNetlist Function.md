# PreProcessNetlist Function

Preprocesses netlist and returns filename where preprocessed result is placed.

Function performs the same task as the PreProcessNetlist command. See  [PreProcessNetlist](com_preprocessnetlist.htm)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Input file name |
| 2 | string array | Yes |  | Options |

#### Argument 1

Input file name to be preprocessed

#### Argument 2

Options

|  |  |
| --- | --- |
| inAppend | Add extra lines separated by semi-colons |
| simulator | SIMetrix or SIMPLIS. Default is SIMPLIS |
| mc | Performing a Monte Carlo run |
| importGlobals | Import global parameter values |
| params | Provide list of parameters in name=value pairs |
| mcseed | Monte Carlo seed value |
| rawdeck | Create raw deck |
| mclogfile | Create Monte Carlo log file |
| cpu | Index specifying cpu for multi-core runs |
|  | Used only for decorating the output file name |
| decoratedeckname | Decorate file name according to cpu, parameters and mc seed |
|  | If resulting name is too long, a unique hash value will be used |

### Returns

Return type: string

File name where preprocessed result is saved

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_preprocessnetlist) | | |
| [◄ PrepareSetComponentValue](func_preparesetcomponentvalue.htm) |  | [Probe ▶](func_probe.htm) |
