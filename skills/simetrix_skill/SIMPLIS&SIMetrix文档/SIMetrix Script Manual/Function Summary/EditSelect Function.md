# EditSelect Function

Opens a dialog box containing any number of edit controls allowing the user to enter text values. The number of edit controls is the smaller of the lengths of arguments 1 and 2. If no arguments are given, 6 controls will be displayed with blank labels. Function returns string vectors containing user entries for each control. If cancel is selected, a single empty string is returned.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty>> | initial edit control entries |
| 2 | string | No | <<empty>> | labels |
| 3 | string | No | <<empty>> | dialog box caption |

### Returns

Return type: string array

### See Also

* [BoolSelect](func_boolselect.htm)
* [RadioSelect](func_radioselect.htm)
* [ValueDialog](func_valuedialog.htm)

### Example

The following dialog box will be displayed on a call to:

```
EditSelect(['Init 1','Init 2'],['Label 1','Label 2'],'Enter Text')
```

![](../../assets/EditSelect.png)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editselect) | | |
| [◄ EditReactiveDialog](func_editreactivedialog.htm) |  | [EditSimplisLaplaceFilterDialog ▶](func_editsimplislaplacefilterdialog.htm) |
