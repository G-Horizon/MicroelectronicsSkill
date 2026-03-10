# DefineLogicGateDialog Function

Opens a dialog box to define a logic gate. This provides new functionality to support custom digital interfaces. For compatibility with version 9.2 and earlier use DefineLogicGateDialog\_Legacy

The argument is a real array of length 7 and defines the initial settings for the box controls as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Number of inputs |
| 1 | Propagation delay |
| 2 | Gate type: |  |  | | --- | --- | | 0 | AND | | 1 | NAND | | 2 | OR | | 3 | NOR | | 3 | Number of inverted inputs | | 4 | If argument 2 supplied, index into arg 2 of input bridge | | 5 | If argument 2 supplied, index into arg 2 of output bridge | | 6 | Supply voltage | |

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | initial settings |

### Returns

Return type: real array

The function returns a real array of length 7 with the same format as the argument described above. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definelogicgatedialog) | | |
| [◄ DefineLaplaceDialog](func_definelaplacedialog.htm) |  | [DefinePerfAnalysisDialog ▶](func_defineperfanalysisdialog.htm) |
