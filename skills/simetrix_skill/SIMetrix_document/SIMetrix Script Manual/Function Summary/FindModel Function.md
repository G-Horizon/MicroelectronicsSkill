# FindModel Function

Returns the file path and line number of a simulator model given its name and type

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Model name |
| 2 | string | Yes |  | Model letter |
| 3 | string | No | 'SIMetrix' | Simulator type |

#### Argument 1

Model name, this is either the name in a .MODEL statement or the name in a .SUBCKT statement.

#### Argument 2

Model letter, e.g 'Q' for BJTs, 'D' for diodes and 'X' for subcircuits.

#### Argument 3

Simulator type, i.e 'SIMetrix' or 'SIMPLIS'

### Returns

Return type: String array

String array of length 2 holding the file name and line number of the definition of the specified model.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_findmodel) | | |
| [◄ FindGraphMeasurement](func_findgraphmeasurement.htm) |  | [FIR ▶](func_fir.htm) |
