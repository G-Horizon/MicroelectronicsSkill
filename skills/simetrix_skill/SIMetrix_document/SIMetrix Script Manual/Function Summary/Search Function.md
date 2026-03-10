# Search Function

Searches a list of strings for one or more items supplied in argument 1 for the item(s) supplied in argument 2. Function returns a real array of length equal to the length of argument 2. The return value is an array of reals.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | List to search |
| 2 | string | Yes |  | Items to search in list |
| 3 | string | No |  | Options |

#### Argument 1

List to search.

#### Argument 2

Items to search in list.

#### Argument 3

Legacy option. Set to 'path' if the items being searched are file system paths. This is to enable case-sensitive searching on systems that use case-sensitive file names.

### Returns

Return type: real array

Array of indexes into argument 1 for the items found in argument 2. If a string in argument 2 is not found, the return value for that element will be -1.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_search) | | |
| [◄ ScriptName](func_scriptname.htm) |  | [SearchDialog ▶](func_searchdialog.htm) |
