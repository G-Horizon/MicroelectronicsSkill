# GetFileVersionStamp Function

Returns file version stamp

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File path |
| 2 | string | No |  | Options |

#### Argument 1

File path

#### Argument 2

If set to 'usestringinfo' the FileVersion string will be read instead of the integer values. Set this if you need the behaviour of this function to be the same as SIMetrix version 7.2 or earlier.

### Returns

Return type: string

Version stamp typically in form major.minor.service.build

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfileversionstamp) | | |
| [◄ GetFileSave](func_getfilesave.htm) |  | [GetFileViewerSelectedDirectories ▶](func_getfileviewerselecteddirectories.htm) |
