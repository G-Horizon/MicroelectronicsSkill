# NewPassiveDialog Function

Opens a dialog box intended to select values for passive components such as resistors and capacitors. The dialog below is displayed after executing the following:

```
Let paramNames = ['temp','tc1','tc2']
Let paramValues = [",","]
Show NewPassiveDialog('1k',['Select Value','e24'], paramNames, paramValues)
```

![](../../assets/PassiveDialog.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Initial value |
| 2 | string array | No | ['Select value', 'E12'] | [message series] |
| 3 | string array | No | <<empty>> | Parameter names |
| 4 | string array | No | <<empty>> | Parameter values |

#### Argument 1

Initial value displayed in "Result" box. "Base" and "Decade" will be adjusted accordingly.

#### Argument 2

Two element string array:

|  |  |
| --- | --- |
| 0 | Message displayed at the top of the box. |
| 1 | Initial setting of preferred value series. Possible values: 'E6, 'E12', 'E24' |

#### Argument 3

String array defining list of parameter names. See argument 4.

#### Argument 4

String array defining list of parameter values. If arguments 3 and 4 are supplied the "Parameters..." button will be visible. This button opens another dialog box that provides the facility to edit these parameters' values.

### Returns

Return type: string array

The function returns a string array in the following form:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Value in "Result" box |
| 1 | Number of parameter values |
| 2 | The values of the parameters in the order they were passed (onwards values) |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_newpassivedialog) | | |
| [◄ NetWires](func_netwires.htm) |  | [NewValueDialog ▶](func_newvaluedialog.htm) |
