# CanOpenFile Function

Returns TRUE (1) if file specified by argument 1 can be opened otherwise returns FALSE (0). Argument 2 may be set to 'copy' (the default), 'read' or 'write' specifying what operation is required to be performed on the file.

'copy' mode and 'read' mode differ only in the share access required for the file. 'copy' is less restricive and will allow copy operations using  [CopyFile](com_copyfile.htm)  but will not allow read operations using, for example,  [ReadFile](func_readfile.htm) .

This function takes account of lock files used to prevent other instances of SIMetrix from opening a file. For example, when a schematic is opened in non read only mode, a lock file is created which will prevent another instance of SIMetrix from opening that file but will not prevent another application from opening the file. CanOpenFile will return false for such files when 'write' mode is specified.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | file name |
| 2 | string | No | read | options |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_canopenfile) | | |
| [◄ BuildWorstCaseHTML](func_buildworstcasehtml.htm) |  | [ChangeDir ▶](func_changedir.htm) |
