# GetActualPath Function

Returns actual file or directory path as a full path even if the path passed is a symbolic or hard link. If the path is a network share it will return a \\server style UNC path. It will also convert "8.3" short paths to "long" paths. Path returned will always use native path separators (i.e. backslashes) but will accept forward slashes on input. This will return an empty string if the object pointed to does not exist or cannot be opened

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

### Returns

Return type: string

Resolved path

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getactualpath) | | |
| [◄ GenPrintDialog](func_genprintdialog.htm) |  | [GetAllAxes ▶](func_getallaxes.htm) |
