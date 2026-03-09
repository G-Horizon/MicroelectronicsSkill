# OpenFile Function

Opens a file and returns its handle. This may be used by the command  [Echo](com_echo.htm) . Use the function  [CloseFile](func_closefile.htm)  to close the file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File path |
| 2 | string | Yes |  | File open mode |

#### Argument 1

Path of file to open.

#### Argument 2

Open mode. May be 'w' or 'wa'. 'w' opens file for writing and clears the file if it already exists. 'wa' opens the file for append, that is it will append any output to the file if that file already exists.

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_openfile) | | |
| [◄ OpenEchoFile](func_openechofile.htm) |  | [OpenPDFPrinter ▶](func_openpdfprinter.htm) |
