# AddSymbolFiles Function

Adds file or files to list of installed symbol library files.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Files to add |

#### Argument 1

A string array containing the path names of the symbol libraries to be installed. The names may use symbolic constants.

### Returns

Return type: Real

Number of files actually added to the library. This may not be the same length as the argument as the function will not install files that are already installed.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addsymbolfiles) | | |
| [◄ AddRemoveDialogNew](func_addremovedialognew.htm) |  | [AppendSensitivityData ▶](func_appendsensitivitydata.htm) |
