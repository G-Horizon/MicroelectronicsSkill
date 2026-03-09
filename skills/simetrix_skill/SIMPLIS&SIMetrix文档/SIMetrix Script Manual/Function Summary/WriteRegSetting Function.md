# WriteRegSetting Function

Writes a string value to the windows registry.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Key path |
| 2 | string | Yes |  | Value name |
| 3 | string | Yes |  | Value to be written |
| 4 | string | No | 'HKCU' | Top level tree |

#### Argument 1

Name of key. This must be a full path from the top level. E.g. 'Software\ SIMetrix\ Version42\ Options'

#### Argument 2

Name of value to be read

#### Argument 3

Value to be written to key

#### Argument 4

Top level tree. This may be either 'HKEY\_CURRENT\_USER' or 'HKEY\_LOCAL\_MACHINE' or their respective abbreviations HKCU and HKLM. Note that you must have administrator rights to write to the HKEY\_LOCAL\_MACHINE tree.

### Returns

Return type: string

Returns one of three string values as defined below:

|  |  |
| --- | --- |
| 'Ok' | Function executed successfully |
| 'WriteFailed' | Could not write that value |
| 'InvalidTreeName' | Arg 4 invalid. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writeregsetting) | | |
| [◄ WriteRawData](func_writerawdata.htm) |  | [WriteSchemProp ▶](func_writeschemprop.htm) |
