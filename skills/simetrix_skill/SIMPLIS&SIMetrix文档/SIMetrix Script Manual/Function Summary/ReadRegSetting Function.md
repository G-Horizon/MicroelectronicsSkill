# ReadRegSetting Function

Reads a string setting from the windows registry. Currently this function can only read settings in the HKEY\_CURRENT\_USER and HKEY\_LOCAL\_MACHINE top level trees.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Key name |
| 2 | string | Yes |  | Value name |
| 3 | string | No | 'HKCU' | Top level tree |

#### Argument 1

Name of key. This must be a full path from the top level. E.g. 'Software\ SIMetrix\'

#### Argument 2

Name of value to be read.

#### Argument 3

Top level tree. This may be either 'HKEY\_CURRENT\_USER' or 'HKEY\_LOCAL\_MACHINE' or their respective abbreviations 'HKCU' and 'HKLM'.

### Returns

Return type: string

Returns value read from the registry. If the value doesn't exist, the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readregsetting) | | |
| [◄ ReadIniKey](func_readinikey.htm) |  | [ReadSchemProp ▶](func_readschemprop.htm) |
