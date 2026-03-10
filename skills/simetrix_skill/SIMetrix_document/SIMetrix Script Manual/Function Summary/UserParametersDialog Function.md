# UserParametersDialog Function

Opens the following dialog box and enters the names and values specified in the arguments. ![](../../assets/UserParametersDialog.png) The user may edit any of the values by double clicking an entry or pressing the space bar. The function returns a string array holding the new values for each parameter.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Names |
| 2 | string | Yes |  | Values |
| 3 | string | No | 'Edit Device Parameters' | Title |

### Returns

Return type: string array

### Example

The following would open a dialog box as shown in the above picture:

```
Show UserParametersDialog(['ACRES', 'DTEMP', 'L', 'M', 'SCALE', 'TC1', 'TC2', 'TEMP', 'W'],
+ [", '10.3', ", '1.0', '120u', ", ", ", '5u'])
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_userparametersdialog) | | |
| [◄ UpDownDialog](func_updowndialog.htm) |  | [Val ▶](func_val.htm) |
