# ShellExecute Function

Performs an operation on a windows registered file. The operation to be performed is determined by how the file is associated by the system. For example, if the file has the extension PDF, the Adobe Acrobat or Adobe Acrobat Reader would be started to open the file. (Assuming Acrobat is installed and correctly associated)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File |
| 2 | string | No | none | Parameters |
| 3 | string | No | current directory | Default directory |
| 4 | string | No | 'open' | Verb |

#### Argument 1

Name of file to process. This can also be the path to a directory, in which case an 'explorer' window will be opened.

#### Argument 2

Parameters to be passed if the file is an executable process. This should be empty if arg 1 is a document file.

#### Argument 3

Default directory for application that processes the file.

#### Argument 4

'Verb' that defines the operation to be performed. This would usually be 'open' but could be 'print' or any other operation that is defined for that type of file.

### Returns

Return type: string

Returns one of the following:

|  |  |
| --- | --- |
| **Value** | **Description** |
| 'OK' | Function completed successfully |
| 'NotFound' | File not found |
| 'BadFormat' | File format was incorrect |
| 'AccessDenied' | File could not be accessed due to insufficient privilege |
| 'NoAssoc' | File has no association for specified verb |
| 'Share' | File could not be accessed because of a sharing violation |
| 'Other' | Function failed for other reason |
| 'NotImplemented' | Function not implemented on this platform. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_shellexecute) | | |
| [◄ Shell](func_shell.htm) |  | [ShiftRef ▶](func_shiftref.htm) |
