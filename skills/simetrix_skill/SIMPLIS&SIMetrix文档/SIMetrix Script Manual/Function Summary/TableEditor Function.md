# TableEditor Function

Displays a table of combo boxes to allow select tabular data

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Combo box entries |
| 2 | string array | Yes |  | Initial selection and row count |
| 3 | string array | Yes |  | Column, row and button labels |

#### Argument 1

Array of strings the length of which determines the number of columns. Each entry is a '|' delimited list of strings that are used to fill the combo boxes in each cell in the corresponding column.

#### Argument 2

Array of strings expected to be the same length as argument 1. Specifies the initial value for the combo boxes. Can be '|' delimited in which case number of tokens determines number of rows filled for the corresponding column.

#### Argument 3

Length 3 array of strings providing column, row and button labels. The first element is a '|' delimited string containing the column labels. The second element is a '|' delimeted string containing the row labels. The third element is 1 or 2 '|' delimited strings containing the labels for the 'Add Row' and 'Remove Row' buttons respectively.

Any or all of the elements may be empty strings in which case the default row and column labels are '1', '2', '3' etc and the button labels are 'Add Row' and 'Remove Row'.

### Returns

Return type: string array

Array of strings of length equal to the number of columns. Each element is a '|' delimited string with each token holding the selected value for the corresponding row

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_tableeditor) | | |
| [◄ TableDialog](func_tabledialog.htm) |  | [tan ▶](func_tan.htm) |
