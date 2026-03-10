# SelectSymbolDialog Function

Opens the following dialog box allowing the user to select a schematic symbol from the symbol library. ![](../../assets/SelectSymbol.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No | Use all installed symbols | Internal symbol names |
| 2 | string array | No | As defined by symbol | Display name and tree paths |
| 3 | string | No |  | Option |

#### Argument 1

An array of internal symbol names. For the left hand graphic display to function correctly, each symbol specified must be currently installed.

#### Argument 2

An array of strings that describes how the symbol will be identified in the right hand pane. Expected to be a semi-colon delimited string with each token representing the node name in the tree list structure.

In practice, however, it is more usual to leave this argument empty, so that the path information can be obtained from the symbol definition itself.

#### Argument 3

Set to 'outIndex' to change return value to an index into argument 1 instead of the actual symbol name.

### Returns

Return type: string

The function returns the internal name of the selected symbol. If the user cancels, the function returns an empty value.

### Notes

This function is used for the **Place** > **From Symbol Library...** menu. In that application, no arguments are supplied and the whole symbol library is displayed.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectsymboldialog) | | |
| [◄ SelectSIMPLISAnalysis](func_selectsimplisanalysis.htm) |  | [SelGraph ▶](func_selgraph.htm) |
