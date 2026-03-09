# GetFileDir Function

Get the directory where the specified file is located.

The function first converts the supplied path to a full path then strips off the final component of the path. If the path actually points to a directory, the value returned will be the parent directory. The function does not check that the path supplied actually exists.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | yes |  | Path to file. May be a relative path |

### Returns

Full directory path where file is located

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfiledir) | | |
| [◄ GetFileCD](func_getfilecd.htm) |  | [GetFileExtensions ▶](func_getfileextensions.htm) |
