# EditCrosshairDimensionDialog Function

Opens a dialog intended for editing the characteristics of cursor crosshair dimensions.

The Properties sheet behaves in the same way as the  [EditObjectPropertiesDialog](func_editobjectpropertiesdialog.htm)  function and is initialised by the function's arguments. The Edit sheet allows the edit and display of certain properties as defined in the following table:

|  |  |
| --- | --- |
| **Property Name** | **Affects Control:** |
| Label1 | Label 1 |
| Label2 | Label 2 |
| Label3 | Label 3 |
| Style | Contents of Style box. One of six values: |  |  | | --- | --- | | Auto | Automatic, Show Difference | | Internal | Internal, Show Difference | | External | External, Show Difference | | P2P1 | Show Absolute | | P2P1 | AutoAutomatic, Show Difference, Show Absolute | | None | No controls selected | |
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
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editcrosshairdimensiondialog) | | |
| [◄ EditBodePlotProbeDialog2](func_editbodeplotprobedialog2.htm) |  | [EditCurveMarkerDialog ▶](func_editcurvemarkerdialog.htm) |
