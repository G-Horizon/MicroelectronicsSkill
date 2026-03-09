# DefineShiftRegDialog Function

Open a dialog box to define a shift register.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial settings |

#### Argument 1

The argument is a real array of length 2 and defines the initial settings of the box controls as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Number of inputs |
| 1 | Clock to out delay |

### Returns

Return type: real array

The function returns a real array of length 3 with the same format as the argument described above. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_defineshiftregdialog) | | |
| [◄ DefineSaturableTxDialog](func_definesaturabletxdialog.htm) |  | [DefineSimplisMultiStepDialog ▶](func_definesimplismultistepdialog.htm) |
