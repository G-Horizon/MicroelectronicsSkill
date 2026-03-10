# MeasureDialog Function

Opens dialog for specifying graph measurements.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Dialog data |
| 2 | string array | No |  | Initial settings |
| 3 | string array | No |  | Condition |

#### Argument 1

Dialog data. Format the same as for argument 1 in the function  [ManageMeasureDialog](func_managemeasuredialog.htm)  except the final token is not required.

#### Argument 2

String array containing initial values. List in same format as return value

#### Argument 3

If set 'haveCursors' indicates to dialog box that graph cursors are enabled.

### Returns

Return type: string array

String array of length 10 providing user selections. Fields defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Measurement selection from list box |
| 1 | '1' if Cursor span box is checked |
| 2 | '1' if AC coupled box is checked |
| 3 | '1' if Integral cycles box is checked |
| 4 | Graph label custom definition |
| 5 | Expression custom definition |
| 6 | '1' if Save to pre-defined box is checked |
| 7 | Format template custom definition |
| 8 | Label for custom definition |
| 9 | Long description for custom definition |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_measuredialog) | | |
| [◄ Mean1](func_mean1.htm) |  | [MessageBox ▶](func_messagebox.htm) |
