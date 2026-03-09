# DelSchemProp Function

Deletes a user-defined schematic window property created using WriteSchemProp.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | number | No |  | Handle |

#### Argument 2

Handle to a schematic.

### Returns

Return type: real

The function returns an integer that indicates the success of the operation as follows:

|  |  |
| --- | --- |
| -1 | No schematic windows open |
| 0 | Success |
| 1 | Property does not exist |
| 2 | Property is not deleteable |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_delschemprop) | | |
| [◄ DeleteTreeProgress](func_deletetreeprogress.htm) |  | [DescendDirectories ▶](func_descenddirectories.htm) |
