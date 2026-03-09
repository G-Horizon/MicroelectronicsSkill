# GetLine Function

Returns a single line from a file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | File handle |

#### Argument 1

Handle as returned by the function  [OpenFile](func_openfile.htm) .

### Returns

Return type: string

The first call to this function after opening the file, will return the first line in the file. Subsequent calls will return the remaining lines in sequence. The function will return an empty vector when there are no more lines in the file. The function will also return an empty vector if the file handle is not valid.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getline) | | |
| [◄ GetLicenseStats](func_getlicensestats.htm) |  | [GetListSelected ▶](func_getlistselected.htm) |
