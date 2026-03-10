# BoolSelect Function

Opens a dialog box with any number of check boxes. The return value is a real vector containing the user's check box settings. 1 means checked, 0 means not checked. The number of check boxes displayed is the smaller of the length of arguments 1 and 2. If neither argument is supplied, 6 check boxes will be displayed without labels.

If the user cancels the operation, an empty value is returned. This can be checked with the function  [length](func_length.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No |  | Initial check box settings |
| 2 | string | No |  | Labels |
| 3 | string | No |  | Dialog Box Caption |
| 4 | string | No |  | GroupBox Title |
| 5 | string | No |  | Descriptive Text |

### Returns

Return type: real array

### See Also

* [EditSelect](func_editselect.htm)
* [RadioSelect](func_radioselect.htm)
* [ValueDialog](func_valuedialog.htm)

### Example

The following dialog box is displayed after a call to:

```
BoolSelect([0,1,0], ['Label1', 'Label2', 'Label3'], 'Caption', 'Group title',
+ 'Select these options')
```

![](../../assets/BoolSelect.png)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_boolselect) | | |
| [◄ avg](func_avg.htm) |  | [Branch ▶](func_branch.htm) |
