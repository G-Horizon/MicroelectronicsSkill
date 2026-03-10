# DefineRegisterDialog Function

Opens a dialog box to define a bus register.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial settings |

#### Argument 1

The argument is a real array of length 4 and defines the initial settings for the box controls as follows:

|  |  |
| --- | --- |
| 0 | Number of bits |
| 1 | 1 if "Has output enable" box checked. Otherwise 0. |
| 2 | Setup time |
| 3 | Clock delay |

### Returns

Return type: real array

The function returns a real array of length 4 with the same format as the argument described above. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_defineregisterdialog) | | |
| [◄ DefinePerfAnalysisDialog](func_defineperfanalysisdialog.htm) |  | [DefineRipperDialog ▶](func_defineripperdialog.htm) |
