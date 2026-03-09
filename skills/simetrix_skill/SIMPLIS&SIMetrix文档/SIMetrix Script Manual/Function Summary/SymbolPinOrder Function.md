# SymbolPinOrder Function

Returns pin order of symbol in currently open symbol editor sheet. Also sets new pin order if argument supplied.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | New pin order |

#### Argument 1

Array of strings with names of pins in the required order.

### Returns

Return type: string array

Array of strings containing pin names of current symbol in the current order. If no symbol editor sheets are open, the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_symbolpinorder) | | |
| [◄ SymbolNames](func_symbolnames.htm) |  | [SymbolPinPoints ▶](func_symbolpinpoints.htm) |
