# ValueDialog Function

Opens a dialog box with up to 10 edit controls allowing numeric values to be entered.

The function returns an array representing the user selected value in each box. If cancelled it returns an empty vector.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | 1 | Initial edit control values |
| 2 | string | No | <<empty>> | Edit control labels |
| 3 | string | No | <<empty>> | Dialog box caption |
| 4 | string | No | <<empty>> |  |

#### Argument 1

The number of edit controls displayed is determined by the length of the first argument. If this is omitted, all 10 will be displayed. Argument 1 specifies the initial values set in each of the controls.

#### Argument 2

Supplies the text of the label displayed to the left of each edit control. The width of the dialog box will be adjusted to accommodate the length of this text.

#### Argument 3

Specifies the text in the title bar of the dialog box.

#### Argument 4

Attaches special characteristics for particular applications. The value of this argument and meaning is as follows:

|  |  |
| --- | --- |
| **Value** | **Action** |
| 'Switch' | For use to specify VC switches. Assumes box 1 is for 'On resistance' and box 2 for 'Off resistance'. Action is modified to ensure 'On resistance' < 'Off resistance' |
| 'Transformer' | For use to specify ideal transformers. Assumes box 1 is 'Turns ratio', box 2 'Primary Inductance' and box 3 is 'Coupling Factor' Hides up-down control for box 3. Min values for boxes 1 and 2 set to 1e-18 Box 3 range 0 to 0.999999 |
| 'TransmissionLine' | For use to specify lossless transmission lines. Assumes box 1 is 'Characteristic Impedance' and box 2 is 'Delay'. Sets box 1 minimum value to 1e-18 and box 2 minimum value to 1e-21 |

Any other value supplied for argument 4 will be treated as the default. In this case all boxes are allowed to vary over a range of -1e18 to +1e18. The function returns an array representing the user selected value in each box. If cancelled it returns an empty vector.

### Returns

Return type: real array

### See Also

* [NewValueDialog](func_newvaluedialog.htm)
* [BoolSelect](func_boolselect.htm)
* [EditSelect](func_editselect.htm)
* [RadioSelect](func_radioselect.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_valuedialog) | | |
| [◄ Val](func_val.htm) |  | [Vec ▶](func_vec.htm) |
