# AddGraphCrossHair Function

Adds a new cursor to the current graph. Note that cursors must be switched on for this to work. This can be done with the command  [CursorMode](com_cursormode.htm) .

For more information on graph annotation objects, please refer to  [Graph Objects](applications_graphobjects.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | curve id |

#### Argument 1

Id of curve on which crosshair is intially placed. If the Id supplied is not valid, the cursor will be placed on an undetermined existing curve.

### Returns

Return type: string array

String array with three elements defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Id of new cursor |
| 1 | Id of cursor's horizontal dimension |
| 2 | Id of cursor's vertical dimension |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addgraphcrosshair) | | |
| [◄ AddConfigCollection](func_addconfigcollection.htm) |  | [AddModelFiles ▶](func_addmodelfiles.htm) |
