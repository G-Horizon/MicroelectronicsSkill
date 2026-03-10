# ReadSpiceFile Function

Returns an array of strings holding lines of text from the file specified by argument 1. Continuation lines marked with a '+' are merged to a single line and inline comments are removed. Comment lines starting with a '\*' are included in the output.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File name |
| 2 | string | Yes |  | Options |

#### Argument 2

Set to 'skipcomment' to remove comment lines from output

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readspicefile) | | |
| [◄ ReadSIMPLISF11Data](func_readsimplisf11data.htm) |  | [ReadTextEditorProp ▶](func_readtexteditorprop.htm) |
