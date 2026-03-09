# EditGraphTextBoxDialog Function

Opens a dialog intended for editing the characteristics of text box objects for graphs.

The Properties sheet behaves in the same way as the  [EditObjectPropertiesDialog](func_editobjectpropertiesdialog.htm)  and is initialised by the function's arguments. The Edit sheet shown above allows the edit and display of certain properties as defined in the following table:

|  |  |
| --- | --- |
| **Property Name** | **Affects Control** |
| Label | Label |
| Colour | Background Colour. An integer defining the RGB |
| value |  |
| Font | Font. String defining font specification |

If any of the controls in the Edit sheet are changed, the corresponding property values in the Properties sheet will reflect those changes and vice-versa.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Property names |
| 2 | string array | Yes |  | Property values |
| 3 | string array | No |  | Property types |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editgraphtextboxdialog) | | |
| [◄ EditGraphMeasurement](func_editgraphmeasurement.htm) |  | [EditJumperDialog ▶](func_editjumperdialog.htm) |
