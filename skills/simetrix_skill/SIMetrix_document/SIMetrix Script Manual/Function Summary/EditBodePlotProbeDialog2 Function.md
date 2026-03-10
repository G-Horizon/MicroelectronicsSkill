# EditBodePlotProbeDialog2 Function

Opens dialog box for editing the advanced Bode plot probe.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | Yes |  | Initial values for dialog box controls |

#### Argument 1

String array with 27 values as defined below:

|  |  |
| --- | --- |
| 0 | Graph name |
| 1 | History depth |
| 2 | Gain enabled |
| 3 | Gain curve label |
| 4 | Gain y-axis label |
| 5 | Gain vertical scale 0:db, 1:Linear |
| 6 | Gain auto y-axis limits |
| 7 | Gain auto grid spacing |
| 8 | Gain vertical axis maximum limit |
| 9 | Gain vertical axis minimum limit |
| 10 | Gain vertical axis grid spacing |
| 11 | Gain curve colour |
| 12 | Phase enabled |
| 13 | Phase curve label |
| 14 | Phase y-axis label |
| 15 | Phase polarity 0:normal 1: -180 degrees |
| 16 | Phase auto axis limits |
| 17 | Phase auto grid spacing |
| 18 | Phase vertical axis maximum limit |
| 19 | Phase vertical axis minimum limit |
| 20 | Phase vertical axis grid spacing |
| 21 | Phase curve colour |
| 22 | Num grids 0:1 grid 1:2 grids |
| 23 | Vertical order 0:phase above gain, 1: gain above phase |
| 24 | Save settings |
| 25 | Set tab/caption to graph name |
| 26 | Separate curves |

### Returns

String array in same format as argument 1 providing user's selected values. Returns an empty vector if the user cancels.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editbodeplotprobedialog2) | | |
| [◄ EditBodePlotProbeDialog](func_editbodeplotprobedialog.htm) |  | [EditCrosshairDimensionDialog ▶](func_editcrosshairdimensiondialog.htm) |
