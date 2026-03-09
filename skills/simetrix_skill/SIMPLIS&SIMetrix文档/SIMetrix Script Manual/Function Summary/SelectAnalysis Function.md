# SelectAnalysis Function

This is a special purpose function. It opens the 'Choose Analysis' dialog box. The return value from this function is simply determined by how the user closes the box. The main operation of the dialog box happens independently of the function call mechanism. Return values are:

|  |  |
| --- | --- |
| No schematic | 3 |
| Run button | 2 |
| Cancel button | 1 |
| OK button | 0 |

The dialog box will not open if there is no current schematic.

The function reads the schematic's text window and translates any analysis controls present including any preceded by a single comment character. It uses the information gained to initialise the dialog box's controls. After the user has made a selection and closed the box, the controls in the schematic text window are updated. This mechanism means that analysis modes are stored with a schematic. Also, the user is free to select analysis modes by manually editing the controls in the text window. Any such changes will be reflected in subsequent calls to SelectAnalysis.

### Arguments

No arguments

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectanalysis) | | |
| [◄ Select2Dialog](func_select2dialog.htm) |  | [SelectColourDialog ▶](func_selectcolourdialog.htm) |
