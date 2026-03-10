# CurveEditDialog Function

Open dialog box to edit curve labels and colours.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | Yes |  | Initial values for dialog box controls |

#### Argument 1

String array consisting of pairs of values. The first element in each pair defines the current label and the second value defines the curve colour using the HTML format. The dialog box will display a single label/colour editor for each pair entered

### Returns

Return type: String array

Values entered by user. First array element will contain the text 'restoredefaults' if the Restore Defaults check box is checked. Otherwise this entry will be an empty string.

The remaining entries are in the same format as the argument and define the label/colour choices entered by the user.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_curveeditdialog) | | |
| [◄ CreateTimer](func_createtimer.htm) |  | [CurveFit ▶](func_curvefit.htm) |
