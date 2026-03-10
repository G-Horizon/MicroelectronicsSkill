# GetSymbols Function

Returns a string array containing information about installed symbols.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | 'name' | Options |
| 2 | string | No | 'all' | Catalog name |

#### Argument 1

Defines what the function returns as defined in the following table:

|  |  |
| --- | --- |
| **Options value** | **Description** |
| 'description' | Returns the user name of each symbol. |
| 'catalogs' | Returns the catalog names for each of the symbols. The catalog defines how the symbol user name is displayed in the symbol dialog display as opened by the function  [SelectSymbolDialog](func_selectsymboldialog.htm) . It consists of one or more strings separated by semi-colons. Each string defines a node in the tree list display. |
| 'tree' | 'catalogs' and 'description' merged together but separated by a semi-colon. |
| " | Internal symbol name. |

For example, the standard three terminal NPN symbol has an internal name of 'npn', a catalog of 'Semiconductors;BJTs' and a description of 'NPN 3 Terminal'. The value returned by the 'tree' option would be 'Semiconductors;BJTs;NPN 3 Terminal'.

#### Argument 2

Specifies a filter that selects symbols according to catalog. May be prefixed with '-' in which case all symbol not belonging to the specified catalog will be returned.

### Returns

Return type: string array

Returns string array providing the symbol info as defined by arg 1 and 2. If there are no symbol libraries installed or there are no symbols with the specified catalog, an empty vector will be returned.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsymbols) | | |
| [◄ GetSymbolPropertyNames](func_getsymbolpropertynames.htm) |  | [GetSystemInfo ▶](func_getsysteminfo.htm) |
