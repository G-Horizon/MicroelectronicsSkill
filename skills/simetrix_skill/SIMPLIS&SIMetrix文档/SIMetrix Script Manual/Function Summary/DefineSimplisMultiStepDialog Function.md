# DefineSimplisMultiStepDialog Function

Opens a dialog box used to define SIMPLIS multi step analyses.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Configuration |
| 2 | string array | Yes |  | Sweep values |

#### Argument 1

4 element string array used to initialise the dialog box as defined by the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Sweep mode: 'Parameter' or 'MonteCarlo' |
| 1 | Parameter name |
| 2 | Step type: 'Decade', 'Linear' or 'List' |
| 3 | Group curves (true/false) |

#### Argument 2

Sweep values. If step type is decade or linear, values define start, stop and number of steps. Otherwise defines list of values.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definesimplismultistepdialog) | | |
| [◄ DefineShiftRegDialog](func_defineshiftregdialog.htm) |  | [DeleteConfigCollection ▶](func_deleteconfigcollection.htm) |
