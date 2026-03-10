# NewValueDialog Function

General purpose user input function. A call to NewValueDialog opens a dialog box with an arbitrary number of controls of 5 different types. Any mix of the different types may be used. The following is an example with 8 controls of two different types: ![](../../assets/NewValueDialog.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Control definitions |
| 2 | string | Yes |  | Initial values |
| 3 | string | Yes |  | Options |

#### Argument 1

This is a string array of length equal to the total number of controls required. Each element of the array defines the control's label, type and valid range of values. The array elements are of the form:

```
label [:type [:range]]
```

Where:

|  |  |
| --- | --- |
| `label` | is a text string defining the control's label, which may not contain the characters ':' or '|'. |
| `type` | is one of the following: |  |  | | --- | --- | | REAL | Default if  *type*  omitted. Displays an edit control with an up-down spinner. Spinner increments in 1:2:5 steps. | | INT or INTEGER | Displays an edit control with an up-down spinner. Spinner increments linearly with step size of 1. | | STRING | Displays an edit control | | BOOL | Displays a check box | | LIST | Displays a drop down list with entries defined by  *range* . | |
| `range` | Valid range of values for control delimited by '|'. Ignored for STRING and BOOL types and compulsory for LIST type. For REAL and INTEGER types, one or two values may be supplied representing the minimum and maximum valid values. The user will not be able to enter values outside this defined range. For LIST types the range defines the entries in the list. |

#### Argument 2

This is a string array which must have the same number of elements as argument 1. Each element defines the initial value for the control. For BOOL types use the values "true" and "false".

#### Argument 3

Function options. Currently there is only one and that is the dialog box caption.

### Returns

Return type: string array

### Example

The following call would display the dialog as shown above.

```
Show NewValueDialog(['RIN::0', 'ROUT::0', 'TH', 'HYSTWD::0', 'VOL',
+ 'VOH', 'TRIG_COND:LIST:0_TO_1|1_TO_0', 'IC:LIST:0|1'],
+ ['10Meg', '100', '2', '0.1', '0', '5', '0_TO_1', '0'], ['Edit
+ Device Parameters'])
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_newvaluedialog) | | |
| [◄ NewPassiveDialog](func_newpassivedialog.htm) |  | [norm ▶](func_norm.htm) |
