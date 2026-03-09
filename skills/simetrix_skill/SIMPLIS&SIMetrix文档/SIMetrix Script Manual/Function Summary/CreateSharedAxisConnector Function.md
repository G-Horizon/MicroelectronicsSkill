# CreateSharedAxisConnector Function

Creates a SharedAxis object to connect x-axes. Each grid has its own x-axis but these may be connected to other x-axes in the same graph. Connected x-axes share their properties such as the minimum and maximum limits.

To connect an x-axis, the SharedId property of the axis to the ID returned by this function. X-axes connected to the same ID will be connected.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | No | Current graph | Graph ID |

#### Argument 1

Graph ID

### Returns

Return type: String

SharedAxis ID

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_createsharedaxisconnector) | | |
| [◄ CreateNewTitleBlockDialog](func_createnewtitleblockdialog.htm) |  | [CreateShortcut ▶](func_createshortcut.htm) |
