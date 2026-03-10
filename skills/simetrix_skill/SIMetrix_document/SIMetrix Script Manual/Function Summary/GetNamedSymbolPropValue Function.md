# GetNamedSymbolPropValue Function

Returns the value of a property defined for a library symbol.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Internal symbol name |
| 2 | string | Yes |  | Property name |
| 3 | string | No | 'symbol' | Options |

#### Argument 1

Internal symbol name. This is the name used internally to reference the symbol and should not be confused with the 'user name' which is usually displayed by the user interface.

The symbol must be present in a currently installed library. If argument 3 is set to 'comp' then this argument instead specifies the file system path name of a component (.SXCMP) file

### Returns

Return type: string

Returns a string holding the value of the selected property. If the symbol/component or property do not exist the function will return an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getnamedsymbolpropvalue) | | |
| [◄ GetNamedSymbolPropNames](func_getnamedsymbolpropnames.htm) |  | [GetNearestNet ▶](func_getnearestnet.htm) |
