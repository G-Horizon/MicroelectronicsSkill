# DefineFourierProbeDialog Function

Opens dialog to edit fixed Fourier Probe

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Values to initialise dialog |

#### Argument 1

Values to initialise dialog

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Axis Type | Setting of Axis Type group in Axis/Graph Options sheet. Possible values: |  |  | | --- | --- | | 'auto' | Auto Select | | 'selected' | Use Selected | | 'axis' | Use New Y-Axis | | 'grid' | Use New Grid | | 'digital' | Digital | | No default. Value must be specified. |
| 1 | Graph Type | Setting of Graph Options group in Axis/Graph Options sheet. Possible values: |  |  | | --- | --- | | 'add' | Add To Selected | | 'newsheet' | New Graph Sheet | | 'newwindow' | New Graph Window | | No default. Value must be specified. |
| 2 | Axis name | Entry in Axis Name in Probe Options sheet | <<empty>> |
| 3 | Persistence | Entry in Persistence box in Probe Options sheet | <<empty>> |
| 4 | Graph name | Entry in Graph Name in Probe Options sheet | <<empty>> |
| 5 | Curve label | Curve label control in Define Curve sheet | <<empty>> |
| 6 | Analysis | Setting for Analyses check boxes in "Probe Options" sheet. Single string comprising a combination of "ac", "dc" and "tran" separated by the pipe symbol ('|'). An empty string will cause all boxes to be checked and "none" will clear all boxes. | <<empty>> |
| 7 | Plot on completion | State of Plot on completion only check box. |  |  | | --- | --- | | 'true' Checked |  | | 'false' Not checked |  | | 'false' |
| 8 | Disable curve name | If true, the curve label box is disabled | 'false' |
| 9 | Display order | String to specify curve display order | <<empty>> |
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
| 25 | Curve colour | Colour of curve as an RGB value. May be passed directly to the .GRAPH colour parameter | <<empty>> |
| 26 | All analyses disabled | Disables all analyses for this probe. | 0 |
| 27 | Help context id |  |  |
| 28 | Measurement type | Not used with this function |  |
| 29 | Output type | Not used with this function |  |
| 30 | Edge type | Not used with this function |  |
| 31 | Probe type | Not used with this function |  |
| 32 | AC power mode | Not used with this function |  |
| 33 | createMode | Not used with this function |  |
| 34 | probeExpression | Not used with this function |  |
| 35 | Fundamental frequency | Frequency setting in Signal info group |  |
| 36 | Start frequency | Start frequency entry in Frequency display group |  |
| 37 | Stop frequency | Stop frequency entry in Frequency display group |  |
| 38 | Number of FFT points | Num. points entry in FFT interpolation group |  |
| 39 | FFT order | Order entry in FFT interpolation group |  |
| 40 | Fourier method | Possible values: |  |  | | --- | --- | | 'continuous' | Use continuous fourier | | 'interpolated' | Use interpolated FFT | | 'continuous' |
| 41 | Window function | Possible values: |  | | --- | | 'rectangular' | | 'hanning' | | 'hamming' | | 'blackman' | | 'hanning' |
| 42 | Start of data span | Start value in Data span group | 0 |
| 43 | End of data span | End value in Data span group | 0.01 |
| 44 | Use specified span | True/False : |  |  | | --- | --- | | False | Use transient analyis parameters | | True | Specify | |  |
| 45 | Know fundamental frequency | Setting in Signal info group | False |
| 46 | Resolution | Resolution entry in Frequency display group | 100 |
| 47 | Plot options | 'mag', 'db' or 'phase' | "mag' |
| 48 | Run time calculation time limit |  |  |
| 49 | Default resolution |  |  |
| 50 | Number of divisions |  |  |

### Returns

Return type: string array

The function returns a string array with the same format as the argument. If the user selects Cancel, the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definefourierprobedialog) | | |
| [◄ DefineFourierDialog](func_definefourierdialog.htm) |  | [DefineIdealTxDialog ▶](func_defineidealtxdialog.htm) |
