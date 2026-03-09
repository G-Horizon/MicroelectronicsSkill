# Select2Dialog Function

Opens a dialog box with two list boxes allowing the user to select two values.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | No |  | Initial values |
| 2 | String array | No |  | List entries |

#### Argument 1

Five element string array. Values as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | List box 1 initial selection |
| 1 | List box 2 initial selection |
| 2 | Message at top of box |
| 3 | Message under left hand list box |
| 4 | Message under right hand list box |

#### Argument 2

Two element array. The first element carries the items to be placed in the left hand list box. The second element carries the items to be placed in the right hand list box. Items are separated by a pipe ('|') symbol.

### Returns

Return type: string array

Two element array. First element carries the selected value from the left hand list box while the second value holds the selected value from the right hand list box.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_select2dialog) | | |
| [◄ Seconds](func_seconds.htm) |  | [SelectAnalysis ▶](func_selectanalysis.htm) |
