# GetUncPath Function

Returns the given path in UNC form. This function's main purpose is to convert windows drive letters to a consistent format.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

#### Argument 1

Path of file in any form. Typically this would include a drive letter on windows.

### Returns

Return type: string

Path in UNC form. Note that if a drive letter on a local machine is used in the path, this function will return the original path unmodified even if a netwrok share is defined for that drive.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getuncpath) | | |
| [◄ GetTouchstoneErrors](func_gettouchstoneerrors.htm) |  | [GetURLFromLocalPath ▶](func_geturlfromlocalpath.htm) |
