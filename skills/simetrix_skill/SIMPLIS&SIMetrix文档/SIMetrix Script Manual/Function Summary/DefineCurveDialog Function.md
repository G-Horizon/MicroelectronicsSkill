# DefineCurveDialog Function

Opens the dialog box used to define a curve for plotting. See menu **Probe** > **Add Curve...** or **Plot** > **Add Curve...** in the graph window.

The argument is a string array of length 25 which defines how the various controls are initialised. This array has the same format for  [EditAxisDialog](func_editaxisdialog.htm)  and  [EditProbeDialog](func_editprobedialog.htm) . Not all the elements are relevant to this function. The following table describes the elements that are used:

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Axis Type | Setting of Axis Type group in Axis/Graph Options sheet. Possible values: |  |  | | --- | --- | | 'auto' | Auto Select | | 'selected' | Use Selected | | 'axis' | Use New Y-Axis | | 'grid' | Use New Grid | | 'digital' | Digital | | 'detachedgrid' | Detached New Grid | | No default. Value must be specified. |
| 1 | Graph Type | Setting of Graph Options group in Axis/Graph Options sheet. Possible values: |  |  | | --- | --- | | 'add' | Add To Selected | | 'newsheet' | New Graph Sheet | | 'newwindow' | New Graph Window | | No default. Value must be specified. |
| 2 | Axis name | Not used with this function |  |
| 3 | Persistence | Not used with this function |  |
| 4 | Graph name | Not used with this function |  |
| 5 | Curve label | Curve label control in Define Curve sheet | <<empty>> |
| 6 | Analysis | Not used with this function |  |
| 7 | Plot on completion | Not used with this function |  |
| 8 | reserved for future use | Not used with this function |  |
| 9 | reserved for future use | Not used with this function |  |
| 10 | X axis graduation | Setting of Log|Lin|Auto for X Axis in Axis Scales sheet. Possible values: |  |  | | --- | --- | | 'lin' | Lin | | 'log' | Log | | 'auto' | Auto | | 'auto' |
| 11 | X axis scale options | Setting of scale options for X Axis in Axis Scales sheet. Possible values: |  |  | | --- | --- | | 'nochange' | No Change | | 'auto' | Auto scale | | 'defined' | Defined | | 'auto' |
| 12 | Y axis graduation | Setting of Log|Lin|Auto for Y Axis in Axis Scales sheet. Possible values as for X axis. | 'auto' |
| 13 | Y axis scale options | Setting of scale options for X Axis in Axis Scales sheet. Possible values as for X axis. | 'auto' |
| 14 | X axis min limit | Min value for X Axis in Axis Scales sheet. Must be specified as a string. | 0 |
| 15 | X axis max limit | Max value for X Axis in Axis Scales sheet. Must be specified as a string. | 1 |
| 16 | Y axis min limit | Min value for Y Axis in Axis Scales sheet. Must be specified as a string. | 0 |
| 17 | Y axis max limit | Max value for Y Axis in Axis Scales sheet. Must be specified as a string. | 1 |
| 18 | X axis label | Axis Label setting for X-Axis group in Axis Labels sheet | <<empty>> |
| 19 | X axis units | Axis Units setting for X-Axis group in Axis Labels sheet | <<empty>> |
| 20 | Y axis label | Axis Label setting for Y-Axis group in Axis Labels sheet | <<empty>> |
| 21 | Y axis units | Axis Units setting for Y-Axis group in Axis Labels sheet | <<empty>> |
| 22 | Y-expression | Contents of Y expression edit box | <<empty>> |
| 23 | X-expression | Contents of X expression edit box, if enabled | <<empty>> |
| 24 | Vector filter | Subcircuit filter selection in Available Vectors group. Possible values: |  |  | | --- | --- | | 'all' | All | | 'top' | Top level | | sub circuit name | Select a subcircuit name. | |  |
| 25 | Detached x-axis | State of Detached x-axis check box | <<empty>> |

The available vectors list box is initialised with the names of vectors in the current group.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial values |

### Returns

Return type: string array

The function returns a string array with the same format as the argument. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definecurvedialog) | | |
| [◄ DefineCounterDialog](func_definecounterdialog.htm) |  | [DefineDACDialog ▶](func_definedacdialog.htm) |
