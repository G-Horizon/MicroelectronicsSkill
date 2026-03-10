# OpenEchoFile Function

Redirects the output of the command  [Echo](com_echo.htm)  to a file. Redirection is disabled when the function  [CloseEchoFile](func_closeechofile.htm)  is called or when control returns to the command line.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File name |
| 2 | string | Yes |  | Access mode |

#### Argument 1

File name.

#### Argument 2

A single letter to determine how the file is opened. Can be either 'w' or 'a'. If 'w', a new file will be created. If a file of that name already exists, it will be overwritten. If 'a' and the file already exists, it will be appended.

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_openechofile) | | |
| [◄ NumElems](func_numelems.htm) |  | [OpenFile ▶](func_openfile.htm) |
