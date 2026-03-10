# PWLDialog Function

Opens the dialog box shown below allowing the entry of X-Y pairs intended for the definition of piece-wise linear devices. ![](../../assets/PwlDialog.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | X-Y Pairs |
| 2 | string | No |  | Options |
| 3 | real array | No |  | Initial conidtion / value states |
| 4 | string | No |  | Conversion tool entry history |

#### Argument 1

X-Y Pairs to initialise box. The above example would be displayed after a call to:

```
Show pwldialog(['0','0.5','1','1.5','2','2.5'])
```

#### Argument 2

Up to seven element string array to define box labels:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Box caption. Default: 'Define PWL Source' |
| 1 | Label for X-Values column. Default: 'Time' |
| 2 | Label for Y-Values column. Default: 'Value' |
| 3 | Initial condition mode. May be: |  |  | | --- | --- | | 'none' | Default setting. No initial condition displayed | | 'segment' | Initial segment. Initial condition value is an integer with a minimum value of 1 and a maximum value equal to the number of rows. (Used for some SIMPLIS PWL devices).  **Use initial condition**  check box will not be shown. | | 'continuous' | Initial condition is a non-integral number.  **Use initial condition**  check box will be shown. | |
| 4 | Help context id. Default: '-1' (no help button shown) |
| 5 | Minimum number of segments. Default = '1' |
| 6 | Maximum number of segments. Default = '255' |
| 7 | Symmetric definition flag. '1' enables symmetric definition mode. Default '0'. |
| 8 | Enable repeat function. '1' enables repeat options used for signal source. The repeat function cannot be displayed at the same time as the initial condition options |

#### Argument 3

Real array with up to four elements. First element is the initial state of the 'Use initial condition' check box. Second element is the initial value of the initial condition edit box. Third element if defined sets the state of the 'Idle in POP' check box. Fourth element defines the number of repeat cycles. If set to zero the 'Repeat forever' button is checked.

#### Argument 4

A string containing the unit input and energy storage output history of the last conversion tool entry. The input and output X-Y points are concatenated with spaces and are then concatenated together with a '|' character.

### Returns

Return type: string array

The function returns the X-Y Pairs entered by the user in the same format as for argument 1. If initial conditions were enabled on input, there will be two additional elements at the end. The first will be either 'true' or 'false' to indicate whether 'Use initial condition' was checked and the second is the value of the initial condition.

If the repeat function is enabled, the number of repeat cycles will be the final element; however, if the component is a capacitor or inductor, the unit-to-energy storage coversion tool entry history will be the final element.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_pwldialog) | | |
| [◄ PWLCurveFit](func_pwlcurvefit.htm) |  | [QueryData ▶](func_querydata.htm) |
