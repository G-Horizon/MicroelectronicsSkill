# GetFileInfo Function

Returns information about a specified file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File path |

### Returns

Return type: string array

Returns an array of length 5.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Drive type, one of: 'local', 'cdrom', 'remote', 'other', 'notexist', 'unknown'. See notes for function  [GetDriveType](func_getdrivetype.htm) . |
| 1 | File size in bytes |
| 2 | Full path name |
| 3 | Last modified time. Value is the number of seconds elapsed since January 1, 1970. |
| 4 | 'True' if path is a directory, otherwise 'false' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfileinfo) | | |
| [◄ GetFileExtensions](func_getfileextensions.htm) |  | [GetFileProductName ▶](func_getfileproductname.htm) |
