# DefineADCDialog Function

Opens a dialog box to define an analog to digital converter. Argument is a real array which specifies the initial values for each control as follows:

|  |  |
| --- | --- |
| **Element index** | **Description** |
| 0 | Number of bits |
| 1 | Convert time (default 1u) |
| 2 | Maximum conversion rate (default 2Meg) |
| 3 | Offset voltage (default 0) |
| 4 | Range (default 5) |

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial values |

### Returns

Return type: real array

The function returns a real array of length 5 with the same format as the argument described above. If the user selects "Cancel" the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_defineadcdialog) | | |
| [◄ DCSourceDialogStr](func_dcsourcedialogstr.htm) |  | [DefineArbSourceDialog ▶](func_definearbsourcedialog.htm) |
