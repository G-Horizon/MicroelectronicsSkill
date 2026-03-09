# TreeListDialog Function

Opens the following dialog box allowing the user to specify an item in tree structured list. ![](../../assets/TreeListDialog.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | strings |
| 2 | string array | No | ['Select Item', ", '0', 'sort', 'false'] | Options |

#### Argument 1

Specifies the items to be displayed in the tree list. These are arranged in semi-colon delimited fields with each field specifying a "branch" of the tree. For example, in the above diagram, the item shown as "Full" would be specified as an element of argument 1 as "Measure;Transient;RMS;Full".

#### Argument 2

An array of strings of max length 5 specifying various other characteristics as defined below:

|  |  |
| --- | --- |
| 0 | Dialog caption |
| 1 | Identifies an item to be initially selected using the same format as the entries in argument 1. |
| 2 | Initial expand level. '0' for no expansion, '1' expands first level of tree etc. |
| 3 | Items will be alphabetically sorted unless this is set to 'nosort' |
| 4 | Items may selected and the box closed by double clicking unless this item is set to 'true' |

### Returns

Return type: real

Returns index into argument 1 of selected item. If no item is selected, the function returns -1. If the user selects Cancel the function returns an empty vector.

### Example

The following will disply the dialog box shown in the above picture:

```
Show TreeListDialog(["'AC Measurements;3db low-pass', 'AC Measurements;band-pass',
+ 'Transient Measurements;Rise time', 'Transient Measurements;Fall time'"])
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_treelistdialog) | | |
| [◄ TranslateLogicalPath](func_translatelogicalpath.htm) |  | [True ▶](func_true.htm) |
