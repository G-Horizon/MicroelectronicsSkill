# EditDigInitDialog Function

Opens a dialog box used to define a digital initial condition

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial setting |

#### Argument 1

The argument is a real array of length 2 which defines the initial settings of the dialog box as follows:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| 1 | Initial state: |  |  | | --- | --- | | 1 | ONE | | 0 | ZERO | |
| 2 | Initial Strength: |  |  | | --- | --- | | 1 | Strong | | 0 | Resistive | |

### Returns

Return type: real array

The function returns a real array of length 2 with the same format as argument 1 described above. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editdiginitdialog) | | |
| [◄ EditDeviceDialog](func_editdevicedialog.htm) |  | [EditFileDefinedPWLDialog ▶](func_editfiledefinedpwldialog.htm) |
