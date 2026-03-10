# ManageMeasureDialog Function

Opens dialog box used to manage graph measurements.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Measurements |

#### Argument 1

String array defining measurements to be entered into the dialog box. Each string is a semi-colon delimited line with each element defined in the following table:

|  |  |
| --- | --- |
| **Token index** | **Description** |
| 0 | Label listed in list box |
| 1 | Expression |
| 2 | Format template |
| 3 | Label as displayed on graph |
| 4 | Full description |
| 5 | Needs cursors on: 0 or 1 |
| 6 | Is custom measurement: 0 or 1 |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_managemeasuredialog) | | |
| [◄ ManageDataGroupsDialog](func_managedatagroupsdialog.htm) |  | [MapArray ▶](func_maparray.htm) |
