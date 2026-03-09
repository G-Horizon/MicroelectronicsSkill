# SearchDialog Function

Opens search dialog using data supplied as an argument

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | Yes |  | Data for search |
| 2 | String | No | '0' | Sets Model check box state |

#### Argument 1

Array of strings providing search data. Each element should have 3 or 4 fields separated by semi-colons. Field 0 is the part number or description Field 1 is a description displayed in the status bar when selected Field 2 is a unique index that will be returned by the function Field 3 can be set to 'model' in which case it will only be presented if the 'Model' check box is checked

#### Argument 2

If set to '1' the model check box will be checked

### Returns

String array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_searchdialog) | | |
| [◄ Search](func_search.htm) |  | [SearchModels ▶](func_searchmodels.htm) |
