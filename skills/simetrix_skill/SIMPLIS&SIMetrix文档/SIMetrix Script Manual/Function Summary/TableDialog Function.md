# TableDialog Function

Displays a spreadsheet style table to allow the user to enter tabular data. See example below for a picture.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Geometry |
| 2 | string array | No |  | Cell initial values |

#### Argument 1

Real array of length 2. First element is the number of rows initially displayed and the second element is the number of columns. Note that these are just the initial values. The user may subsequently add or delete rows and columns.

#### Argument 2

An array of strings to define the initial cell entries. If not supplied. the cells will begin empty.

Each element in the array is a semi-colon delimited string and defines a complete row. The cell entries are sequentially loaded from the delimited fields in each row.

### Returns

Return type: string array

Return value will be in the same format at argument 2 and provide the contents of the cells as entered by the user.

### Example

A call to:

```
TableDialog([5,3],["'Device;Length;Width;', 'Q2;1u;0.35u;',
+ 'Q3;2.25u;0.35u;', 'Q4;2.25u;0.35u;', 'Q5;2.25u;0.35u;'"])
```

will show this dialog: ![](../../assets/TableDialog.png)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_tabledialog) | | |
| [◄ SystemWidgetExistsInSelectedWindow](func_systemwidgetexistsinselectedwindow.htm) |  | [TableEditor ▶](func_tableeditor.htm) |
