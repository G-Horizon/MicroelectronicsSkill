# DefineArbSourceDialog Function

Opens a dialog box to define an arbitrary source:

Argument is a string array which specifies the initial values for each control as follows:

|  |  |
| --- | --- |
| **Element index** | **Description** |
| 0 | Expression |
| 1 | Number of input voltages. (Default 1. Must be entered as a string) |
| 2 | Number of input currents. (Default 0. Must be entered as a string) |
| 3 | Output config: |
|  | 0: Single ended voltage (default) |
|  | 1: Single ended current |
|  | 2: Differential voltage |
|  | 3: Differential current |
|  | (value must be entered as a string) |

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial values |

### Returns

Return type: string array

The function returns a string array of length 4 with the same format as the argument described above.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definearbsourcedialog) | | |
| [◄ DefineADCDialog](func_defineadcdialog.htm) |  | [DefineBusPlotDialog ▶](func_definebusplotdialog.htm) |
