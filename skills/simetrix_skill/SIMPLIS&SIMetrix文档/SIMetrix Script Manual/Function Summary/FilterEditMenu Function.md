# FilterEditMenu Function

Filters a menu list to return only menu definitions that are actually displayed.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Menu definition list |

#### Argument 1

The menu definition list, as given by global:menusnapshot.

### Returns

Return type: string array

Same as the input, but with entries removed for menus that are not displayed but rather form menus that are built up.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_filtereditmenu) | | |
| [◄ FileToString](func_filetostring.htm) |  | [FilterFile ▶](func_filterfile.htm) |
