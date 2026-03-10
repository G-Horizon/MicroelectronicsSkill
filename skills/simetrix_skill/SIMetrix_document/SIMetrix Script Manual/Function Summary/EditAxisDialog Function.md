# EditAxisDialog Function

Opens a dialog box used to edit graph axes

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial settings |

#### Argument 1

The argument is a string array of length 25 which defines how the various controls are initialised. This array has the same format as  [DefineCurveDialog](func_definecurvedialog.htm)  and  [EditProbeDialog](func_editprobedialog.htm)  but not all the elements are used here. The following table describes the elements that are used.

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0-10 |  | Not used with this function |  |
| 11 | X axis scale options | Setting of scale options for X Axis in Axis Scales sheet. Possible values: |  |  | | --- | --- | | 'nochange' No Change |  | | 'auto' Auto scale |  | | 'defined' Defined |  | | 'auto' |
| 12 | Y axis graduation | Not used with this function |  |
| 13 | Y axis scale options | Setting of scale options for X Axis in Axis Scales sheet. Possible values as for X axis. | 'auto' |
| 14 | X axis min limit | Min value for X Axis in Axis Scales sheet. Must be specified as a string. | 0 |
| 15 | X axis max limit | Max value for X Axis in Axis Scales sheet. Must be specified as a string. | 1 |
| 16 | Y axis min limit | Min value for Y Axis in Axis Scales sheet. Must be specified as a string. | 0 |
| 17 | Y axis max limit | Max value for Y Axis in Axis Scales sheet. Must be specified as a string. | 1 |
| 18 | X axis label | Axis Label setting for X-Axis group in Axis Labels sheet | <<empty>> |
| 19 | X axis units | Axis Units setting for X-Axis group in Axis Labels sheet | <<empty>> |
| 20 | Y axis label | Axis Label setting for Y-Axis group in Axis Labels sheet | <<empty>> |
| 21 | Y axis units | Axis Units setting for Y-Axis group in Axis Labels sheet | <<empty>> |
| 22 | Y-expression | Not used with this function |  |
| 23 | X-expression | Not used with this function |  |
| 24 | Vector filter | Not used with this function |  |

### Returns

Return type: string array

The function returns a string array with the same format as the argument. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editaxisdialog) | | |
| [◄ EditArcDialog](func_editarcdialog.htm) |  | [EditBodePlotProbeDialog ▶](func_editbodeplotprobedialog.htm) |
