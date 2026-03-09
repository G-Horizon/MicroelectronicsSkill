# ListDirectory Function

Lists all files that comply with the spec provided in argument 1.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path specification |
| 2 | string | No | 'none' | Option |

#### Argument 1

Specification for output. This would usually contain a DOS style wild card value. E.g. 'C:\ Program Files\ SIMetrix 42\ \*.\*'. No output will result if just a directory name is given.

#### Argument 2

If omitted, the result will be file names only. If set to 'fullpath', the full path of the files will be returned.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_listdirectory) | | |
| [◄ length](func_length.htm) |  | [ListSchemProps ▶](func_listschemprops.htm) |
