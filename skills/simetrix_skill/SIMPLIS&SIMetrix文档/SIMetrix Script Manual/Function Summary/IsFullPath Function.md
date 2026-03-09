# IsFullPath Function

Returns TRUE if the supplied path name is a full absolute path. Note that a path that starts with a directory separator but which does not include a drive letter is classed as a full path.

The path does not need to exist to be identified as a full path

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

#### Argument 1

File system path name

### Returns

Return type: real

TRUE if arg is a full absolute path. FALSE if it is a relative path.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_isfullpath) | | |
| [◄ IsFileOfType](func_isfileoftype.htm) |  | [IsImageFile ▶](func_isimagefile.htm) |
