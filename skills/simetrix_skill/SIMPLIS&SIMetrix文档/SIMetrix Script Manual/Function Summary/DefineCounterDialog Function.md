# DefineCounterDialog Function

Opens a dialog box to define a digital counter.

Argument is a real array which specifies the initial values for each control as follows:

|  |  |
| --- | --- |
| 0 | Number of bits |
| 1 | Maximum count (default = ???MATH???2^{\text{number of bits}}-1???MATH???) |
| 2 | 1 = Has reset, 0 = does not have reset (default 0) |
| 3 | Clock to out delay (default 10n) |

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial values |

### Returns

Return type: real array

The function returns a real array of length 4 with the same format as the argument described above. If the user selects "Cancel" the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definecounterdialog) | | |
| [◄ DefineBusPlotDialog](func_definebusplotdialog.htm) |  | [DefineCurveDialog ▶](func_definecurvedialog.htm) |
