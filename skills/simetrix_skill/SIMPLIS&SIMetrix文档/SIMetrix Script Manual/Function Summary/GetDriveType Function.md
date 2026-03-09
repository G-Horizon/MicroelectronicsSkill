# GetDriveType Function

Determines the type of drive or file system of the specified path.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

### Returns

Return type: string

Determines the type of drive or file system of the specified path. Returns one of the following values:

|  |  |
| --- | --- |
| **Return value** | **Description** |
| 'local' | Drive or file system present on the local machine |
| 'remote' | Network drive or file system |
| 'cdrom' | CD Rom or DVD drive |
| 'other' | Other file system or drive |
| 'notexist' | The path doesn't exist or media not present |
| 'unknown' | Drive type or file system could not be determined |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdrivetype) | | |
| [◄ GetDotParamValue](func_getdotparamvalue.htm) |  | [GetEnvVar ▶](func_getenvvar.htm) |
