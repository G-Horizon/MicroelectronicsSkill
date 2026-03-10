# UpDownDialog Function

Opens the following dialog box to allow the user to rearrange the order of a list of strings. ![](../../assets/UpDownDialog.png) The box displays the strings given in argument 1 in the order supplied. The user can rearrange these using the up and down arrow buttons. When the user presses OK the function return the strings in the new order. If the user cancels the box the function returns an empty vector.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Strings to sort |
| 2 | string | No | 'Select Item Order' | Box caption |

### Returns

Return type: string array

The strings in the new order, or an empty string if cancel is pressed.

### Example

The following statement will open the box as shown in the above picture

```
Show UpDownDialog(['Vout', 'Osc', 'Vp', 'Comp', 'Sense', 'Vfb', 'Refv', 'Gnd'], 'Select Pin Order')
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_updowndialog) | | |
| [◄ unitvec](func_unitvec.htm) |  | [UserParametersDialog ▶](func_userparametersdialog.htm) |
