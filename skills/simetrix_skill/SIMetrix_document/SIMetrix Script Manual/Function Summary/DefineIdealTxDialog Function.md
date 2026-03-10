# DefineIdealTxDialog Function

Opens a dialog box to define an ideal transformer.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Inductance factor, coupling factors, number of windings |
| 2 | real array | Yes |  | Number of turns for primary windings |
| 3 | real array | Yes |  | Number of turns for secondary windings |
| 4 | string | No |  | options |

#### Argument 1

Real array of size 6. Function of each element is described below:

|  |  |
| --- | --- |
| 0 | Inductance factor, AL. L = AL \* N\*N |
| 1 | Coupling factor primary to primary |
| 2 | Coupling factor secondary to secondary |
| 3 | Coupling factor primary to secondary |
| 4 | Number of primaries |
| 5 | Number of secondaries |

#### Argument 2

Real array of values representing the number of turns for each primary winding.

#### Argument 3

Real array of values representing the number of turns for each secondary winding.

#### Argument 4

If set to 'nonind', the box design will that used for non-inductive transformers. These do not show inductance related parameters.

### Returns

Return type: real array

The function returns, the settings selected by the user in a single real array with the same format as the three arguments concatenated together. If the user selects Cancel the function returns an empty vector.

### Notes

The dialog box design has changed significantly with version 8.20 compared to earlier versions. Functionally it is compatible if the number of turns in primary 1 is kept at 1. The earlier designs returned turns ratios and no facility was provided to set the number of turns for the first primary.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_defineidealtxdialog) | | |
| [◄ DefineFourierProbeDialog](func_definefourierprobedialog.htm) |  | [DefineLaplaceDialog ▶](func_definelaplacedialog.htm) |
