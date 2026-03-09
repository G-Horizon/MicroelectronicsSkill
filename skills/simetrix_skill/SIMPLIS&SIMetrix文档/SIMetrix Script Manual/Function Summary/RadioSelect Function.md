# RadioSelect Function

Opens a dialog box with any number of radio buttons. The number of buttons visible depends on the length of argument 2. Six will be displayed if it is omitted.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | 1 | Number of buttons initially selected |
| 2 | string | No | empty | Button labels |
| 3 | string | No | Dialog box caption | Other labels |
| 4 | string | No |  | Help context ID |

#### Argument 1

The number of buttons initially selected.

#### Argument 2

Specifies the labels for each button.

#### Argument 3

String array up to length 3. First element is dialog box caption and the second element is text label displayed above radio buttons. If a third element is present, a check box will also be displayed underneath the radio buttons. The third element defines the label for this check box

#### Argument 4

Specifies a help context id and if present a Help button will be displayed. This is used by some internal scripts.

### Returns

Return type: real

The return value identifies the selected button with the top most being 1. If the user cancels the function returns 0. If the check box is displayed, the return value will have length 2 with the second element holding the state of the check box.

### See Also

* [BoolSelect](func_boolselect.htm)
* [EditSelect](func_editselect.htm)
* [ValueDialog](func_valuedialog.htm)
* [NewValueDialog](func_newvaluedialog.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_radioselect) | | |
| [◄ QueryData](func_querydata.htm) |  | [Range ▶](func_range.htm) |
