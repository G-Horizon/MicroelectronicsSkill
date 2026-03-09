# SelectDialog Function

Opens a dialog box containing a list box. The list box is filled with string items supplied in argument 2. The return value is the index or indexes of the items in the list box selected by the user.

This function is used by a number of the standard menus.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Options |
| 2 | string array | Yes |  | List box entries |

#### Argument 1

There are a number of options available and these are specified in argument 1. This is an array of strings of length up to 7. The meaning of each element is as follows:

|  |  |  |
| --- | --- | --- |
| **Index** | **Possible values** | **Description** |
| 0 |  | Dialog box caption |
| 1 |  | Message above list box |
| 2 | 'Multiple', 'Single' | If 'single', only one item may be selected. Otherwise any number of items can be selected. |
| 3 | 'Sorted', " | If 'sorted', items in list are arranged in alphabetical order. Otherwise they are in same order as supplied. |
| 4 |  | Index of item to select at start. Only effective if 'single' selected for index 2. This is an integer but must be entered as a string e.g. '2'. |
| 5 |  | Initial string in edit box |
| 6 |  | Default return value if none selected |

### Returns

Return type: real array

The return value is the index or indexes of the items in the list box selected by the user, or empty if the user cancels.

### Example

```
SelectDialog(['Caption','Message','single',",'1'],
['Fred','John','Bill'])
```

Will place strings 'Fred', 'John' and 'Bill' in the list box with 'John' selected initially. The strings will be in the order given (not sorted).

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectdialog) | | |
| [◄ SelectDevice](func_selectdevice.htm) |  | [SelectedProperties ▶](func_selectedproperties.htm) |
