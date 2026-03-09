# CopyURL Function

Copies a file specified by a URL from one location to another. The URL may specify HTTP addresses (prefix 'http://'), HTTPS addresses (prefix 'https://'), FTP addresses (prefix 'ftp: and local file system addresses (prefix 'file:/').

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | From URL file |
| 2 | string | Yes |  | To URL file |
| 3 | string | No | progress | options |

#### Argument 1

URL of source file.

#### Argument 2

URL of destination file

#### Argument 3

Options: can be 'progress' or 'noprogress'. If set to 'progress' (the default) a box will display with a bar showing the progress of the file transfer. Otherwise no such box will display.

### Returns

Return type: string array

String array of length 2. First element will be one of the values shown in the following table:

|  |  |
| --- | --- |
| **Id** | **Description** |
| IncorrectLogin | A username and password are required for this URL |
| HostNotFound | The specified host in the URL could not be found. This error can also occur if there is no Internet connection. |
| Unexpected2 | This is an internal error that should not occur |
| MkdirError | Could not create target directory |
| RemoveError | This is an internal error that should not occur |
| RenameError | This is an internal error that should not occur |
| GetError | An error occurred while fetching a file |
| PutError | An error occurred while storing a file |
| FileNotExist | File doesn't exist |
| PermissionDenied | You do not have sufficient privilege to perform the operation |
| Unknown Error | This is an internal error that should not occur |

The second element of the returned string gives a descriptive message providing more information about the cause of failure.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_copyurl) | | |
| [◄ CopyTree](func_copytree.htm) |  | [cos ▶](func_cos.htm) |
