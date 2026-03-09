# GetSymbolInfo Function

Returns information on symbol in the symbol editor.

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array of length 3 providing information on the symbol in the currently selected symbol editor sheet. If no symbol editor sheet is open the function returns an empty vector.

Format of the return value is:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Symbol name |
| 1 | Symbol description |
| 2 | Symbol catalog |
| 3 | Path to symbol library or component file where the symbol definition is located. If the symbol is not found in any symbol library, this element will be empty. |
| 4 | Type of symbol. One of two values: 'Symbol': Regular symbol stored in a library 'Component': Hierarchical component |
| 5 | Flags. Currently values can only be 0 or 1. Future versions may use additional bits. For forward compatibility, test this value using the function  [Field](func_field.htm)  to test bit 0. The value reports the state of the 'All references to symbol automatically updated' check box when the symbol was saved. If checked, this value will be 1 otherwise 0. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsymbolinfo) | | |
| [◄ GetSymbolFiles](func_getsymbolfiles.htm) |  | [GetSymbolOrigin ▶](func_getsymbolorigin.htm) |
