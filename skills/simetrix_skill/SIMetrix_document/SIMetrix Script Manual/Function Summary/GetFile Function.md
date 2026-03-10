# GetFile Function

Opens the Open File dialog box. Return value is full pathname of file selected by user. If user cancels operation, function returns an empty string. Argument to function supplies description of files and default extension. These two items are separated by '\ '. E.g. `GetFile('Schematic Files\\sch')`.

This function has now been superseded by the functions  [GetSimetrixFile](func_getsimetrixfile.htm)  and  [GetUserFile](func_getuserfile.htm)  which are more flexible.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File specification |
| 2 | real | No |  | 0: file must exist, 1:need not exist |

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfile) | | |
| [◄ GetFailedNodesFromIterNum](func_getfailednodesfromiternum.htm) |  | [GetFileCD ▶](func_getfilecd.htm) |
