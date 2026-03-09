# GetTempFile Function

Creates a temporary file name

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Default temporary directory | Directory for file |

### Returns

Return type: string

Returns the full path to a unique file to be used for temporary storage

### Notes

The filename generated is guaranteed to be unique at the time the function executes but this function does not open the file. It is theoretically possible (but unlikely) for the filename to be used by another process between the time the function is called and at a later time when it is opened for writing.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gettempfile) | | |
| [◄ GetSystemInfo](func_getsysteminfo.htm) |  | [GetTextEditorText ▶](func_gettexteditortext.htm) |
