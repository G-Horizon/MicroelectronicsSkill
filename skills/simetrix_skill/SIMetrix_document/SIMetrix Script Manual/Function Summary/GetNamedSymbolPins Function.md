# GetNamedSymbolPins Function

Returns the names for all pins of the specified symbol or hierarchical component.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Symbol name or component path |
| 2 | string | No | 'symbol' | Options |

#### Argument 1

Internal symbol name. This is the name used internally to reference the symbol and should not be confused with the 'user name' which is usually displayed by the user interface.

The symbol must be present in a currently installed library. If argument 2 is set to 'comp' then this argument instead specifies the file system path name of a component (.SXCMP) file.

#### Argument 2

May be set to 'comp' or 'local'. If set to 'comp' argument 1 specifies the file system path name of a component. If set to 'local' the currently displayed schematic will be searched for the specified symbol.

### Returns

Return type: string array

Returns a string array of length equal to the number of pins on the specified symbol. If the symbol or component cannot be found the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getnamedsymbolpins) | | |
| [◄ GetModifiedStatus](func_getmodifiedstatus.htm) |  | [GetNamedSymbolPropNames ▶](func_getnamedsymbolpropnames.htm) |
