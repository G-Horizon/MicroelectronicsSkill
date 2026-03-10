# PropOverrideStyle Function

Returns the override style of the selected property, if one exists. Override styles are used in the schematic and symbol editors to assign a different font style to a property. Uses the currently selected schematic/symbol editor.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | No |  | Options |

#### Argument 2

Set to "pin" to declare property name as a pin name

### Returns

Return type: string

The override style name, if any, used by the property with the name specified.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propoverridestyle) | | |
| [◄ PropFlagsWires](func_propflagswires.htm) |  | [PropValue ▶](func_propvalue.htm) |
