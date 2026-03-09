# GetNamedSymbolPropNames Function

Returns names of all properties defined for a library symbol.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Internal symbol name |
| 2 | string | No | 'symbol' | Options |

#### Argument 1

Internal symbol name. This is the name used internally to reference the symbol and should not be confused with the 'user name' which is usually displayed by the user interface.

The symbol must be present in a currently installed library. If argument 2 is set to 'comp' then this argument instead specifies the file system path name of a component (.SXCMP) file.

### Returns

Return type: string array

Returns a string array holding the names of all the symbol's properties. If the symbol or component cannot be found the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getnamedsymbolpropnames) | | |
| [◄ GetNamedSymbolPins](func_getnamedsymbolpins.htm) |  | [GetNamedSymbolPropValue ▶](func_getnamedsymbolpropvalue.htm) |
