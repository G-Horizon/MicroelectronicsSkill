# EditCurveMarkerDialog Function

Opens a dialog intended for editing the characteristics of curve markers.

The Properties sheet behaves in the same way as the  [EditObjectPropertiesDialog](func_editobjectpropertiesdialog.htm)  function and is initialised by the functions arguments. The Edit sheet allows the edit and display of certain properties as defined in the following table:

|  |  |
| --- | --- |
| **Property Name** | **Affects Control** |
| Label | Label |
| LabelJustification | Text Alignment box. One of these values: |  |  | | --- | --- | | -1 | Automatic | | 0 | Left-Bottom | | 1 | Centre-Bottom | | 2 | Right-Bottom | | 3 | Left-Middle | | 4 | Centre-Middle | | 5 | Right-Middle | | 6 | Left-Top | | 7 | Centre-Top | | 8 | Right-Top | |
| Font | Font. String defining font specification |

If any of the controls in the Edit sheet are changed, the corresponding property values in the Properties sheet will reflect those changes and vice-versa.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Property names |
| 2 | string array | Yes |  |  |
| 3 | string array | No |  | Property types |

#### Argument 2

Property values

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editcurvemarkerdialog) | | |
| [◄ EditCrosshairDimensionDialog](func_editcrosshairdimensiondialog.htm) |  | [EditDeviceDialog ▶](func_editdevicedialog.htm) |
