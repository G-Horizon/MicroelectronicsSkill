# DefineDACDialog Function

Opens a dialog box to define an analog to digital converter.

Argument is a real array which specifies the initial values for each control as follows:

|  |  |
| --- | --- |
| 0 | Number of bits |
| 1 | Output slew time (10n) |
| 2 | Offset voltage (default 0) |
| 3 | Range (default 5) |

The function returns a real array of length 4 with the same format as the argument described above. If the user selects "Cancel" the function returns an empty vector.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Initial values |

### Returns

Return type: real array

The function returns a real array of length 4 with the same format as the argument described above. If the user selects "Cancel" the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definedacdialog) | | |
| [◄ DefineCurveDialog](func_definecurvedialog.htm) |  | [DefineFourierDialog ▶](func_definefourierdialog.htm) |
