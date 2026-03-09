# SelectedProperties Function

Returns information about selected properties.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | 'Handle' | Property name |

#### Argument 1

Property whose value will be used to identify the instance that possesses the selected property.

### Returns

Return type: string array

Returns an array of length equal to 3 times the number of properties selected. Currently, however, it is only possible to select one property at a time so the return value will be either of length zero or length 3. The elements in each group of three are as defined in the table.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Value of instance property identified in argument 1. This is used to identify the instance that possesses the selected property. |
| 1 | Name of selected property |
| 2 | Value of selected property |

### Notes

Properties can only be selected if the 'selectable' attribute is enabled.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectedproperties) | | |
| [◄ SelectDialog](func_selectdialog.htm) |  | [SelectedStyleInfo ▶](func_selectedstyleinfo.htm) |
