# SymbolInfoDialog Function

Opens a dialog box allowing the specification of symbol details.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Initial settings |
| 2 | string | No |  | Available catalogs |

#### Argument 1

String array length 5 specifying initial settings:

|  |  |
| --- | --- |
| 0 | Symbol name |
| 1 | Display name |
| 2 | Catalog |
| 3 | Path |
| 4 | If 'component', save as component initially selected |
| 5 | If '1' "All references to symbol automatically updated" box will be checked. |

#### Argument 2

List of available catalogs entered into catalog list box.

### Returns

Return type: string array

String array of length 6 as follows

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Symbol name entry |
| 1 | Display name entry |
| 2 | Catalog selected |
| 3 | 'Save to' radio button: 1 Global library, 2 Current schematic only, 3 Both |
| 4 | File path |
| 5 | '1' if 'All references to symbol automatically updated' box is checked, otherwise '0' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_symbolinfodialog) | | |
| [◄ SxUUID](func_sxuuid.htm) |  | [SymbolLibraryManagerDialog ▶](func_symbollibrarymanagerdialog.htm) |
