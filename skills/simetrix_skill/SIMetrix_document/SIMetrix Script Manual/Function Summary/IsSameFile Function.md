# IsSameFile Function

Compares two paths and returns true (1) if they point to the same file. The function takes account of the fact that the two arguments might try to access the same file by different methods. For example, on Windows, one file might use a drive letter while the other might use a server path. The function will always return true if the path names are identical even if the target does not exist.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path of file 1 |
| 2 | string | Yes |  | Path of file 2 |

### Returns

Return type: real

Returns 1 if the paths are the same, 0 otherwise.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_issamefile) | | |
| [◄ IsOptionMigrateable](func_isoptionmigrateable.htm) |  | [IsScript ▶](func_isscript.htm) |
