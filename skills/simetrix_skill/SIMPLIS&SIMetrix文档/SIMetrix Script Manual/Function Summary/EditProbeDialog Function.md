# EditProbeDialog Function

Opens a dialog to define a schematic fixed probe

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial settings |

#### Argument 1

The argument is a string array of length 25 which defines how the various controls are initialised. This array has the same format for  [EditAxisDialog](func_editaxisdialog.htm)  and  [DefineCurveDialog](func_definecurvedialog.htm) . Not all the elements are relevant to this function. The following table describes the elements that are used:

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Axis Type | Setting of Axis Type group in Axis/Graph Options sheet. Possible values: |  |  | | --- | --- | | 'auto' | Auto Select | | 'selected' | Use Selected | | 'axis' | Use New Y-Axis | | 'grid' | Use New Grid | | 'digital' | Digital | | No default. Value must be specified. |
| 1 | Graph Type | Not used with this function |  |
| 2 | Axis name | Entry in Axis Name in Probe Options sheet | <<empty>> |
| 3 | Persistence | Entry in Persistence box in Probe Options sheet | <<empty>> |
| 4 | Graph name | Entry in Graph Name in Probe Options sheet | <<empty>> |
| 5 | Curve label | Curve label control in Probe Options sheet | <<empty>> |
| 6 | Analysis | Setting for Analyses check boxes in "Probe Options" sheet. Single string comprising a combination of "ac", "dc" and "tran" separated by the pipe symbol ('|'). An empty string will cause all boxes to be checked and "none" will clear all boxes. | <<empty>> |
| 7 | Plot on completion | State of Plot on completion only check box. |  |  | | --- | --- | | 'true' Checked |  | | 'false' Not checked |  | | 'false' |
| 8 | reserved for future use | Not used with this function |  |
| 9 | reserved for future use | Not used with this function |  |
| 10 | X axis graduation | Setting of Log|Lin|Auto for X Axis in Axis Scales sheet. Possible values: |  |  | | --- | --- | | 'lin' | Lin | | 'log' | Log | | 'auto' | Auto | | 'auto' |
| 11 | X axis scale options | Setting of scale options for X Axis in Axis Scales sheet. Possible values: |  |  | | --- | --- | | 'nochange' | No Change | | 'defined' | Defined | | 'auto' |
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
| 22 | Y-expression | Not used with this function |  |
| 23 | X-expression | Not used with this function |  |
| 24 | Vector filter | Not used with this function |  |
| 25 | Curve colour | Colour of curve as an RGB value. May be passed directly to the .GRAPH colour parameter | <<empty>> |
| 26 | All analyses disabled | Disables all analyses for this probe. | 0 |
| 27 | Physical Probe Type |  |  |
| 28 | Measurement type |  |  |
| 29 | Output type |  |  |
| 30 | Edge type |  |  |
| 31 | Probe type |  |  |
| 32 | AC power mode |  |  |
| 33 | Create mode |  |  |
| 34 | Probe expression |  |  |
| 35 | Multi-step mode |  |  |
| 36 | Number of histogram bins |  |  |
| 37 | Use default histogram bins |  |  |
| 38 | Display advanced statistics |  |  |
| 39 | Set grapg tab/caption to name |  |  |
| 40 | Separate curves |  |  |
| 41 | Persistence default |  |  |

### Returns

Return type: string array

The function returns a string array with the same format as the argument. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editprobedialog) | | |
| [◄ EditPotDialog](func_editpotdialog.htm) |  | [EditPropertyDialog ▶](func_editpropertydialog.htm) |
