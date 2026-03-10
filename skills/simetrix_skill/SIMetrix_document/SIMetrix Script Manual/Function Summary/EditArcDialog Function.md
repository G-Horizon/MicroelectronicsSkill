# EditArcDialog Function

Opens a dialog box used to define an arc circle or ellipse for the symbol editor.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | 90 | initial start to finish angle |
| 2 | real | No | 1 | initial ellipse height/width |

#### Argument 1

Initial value for start to finish angle.

#### Argument 2

Initial value for ellipse height/width.

### Returns

Return type: real array

If the user selects Cancel the function returns an empty vector, otherwise the following real array of length 2 is produced:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Start to finish angle |
| 1 | Ellipse height/width |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editarcdialog) | | |
| [◄ Distribution](func_distribution.htm) |  | [EditAxisDialog ▶](func_editaxisdialog.htm) |
