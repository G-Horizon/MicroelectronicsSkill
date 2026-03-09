# EditPotDialog Function

Opens a dialog to define a potentiometer

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial settings |

#### Argument 1

The argument is a real array of length 3 and defines the initial settings as follows:

|  |  |
| --- | --- |
| 0 | Resistance |
| 1 | Wiper position (0 to 1) |
| 2 | Run simulation after position changed check box state: |  |  | | --- | --- | | 1 | checked | | 0 | not checked | |

### Returns

Return type: real array

The function returns a string array with the same format as the argument. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editpotdialog) | | |
| [◄ EditPinDialog](func_editpindialog.htm) |  | [EditProbeDialog ▶](func_editprobedialog.htm) |
