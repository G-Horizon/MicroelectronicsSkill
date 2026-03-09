# MapArray Function

Creates an array of real or string items listed in argument 1 with array locations defined in argument 2.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real or string | Yes |  | Items to be included in result |
| 2 | real | Yes |  | Indexes for corresponding items in argument 1 |

#### Argument 1

Items to be included in result

#### Argument 2

Indexes for corresponding items in argument 1

### Returns

Return type: Same as argument 1

Array of the same type as argument 1 with length equal to the highest value found in argument 2.

The return value will be an array where each element is an item in argument 1 located at the index specified in the corresponding location in argument 2.

Unused locations will contain empty strings if argument 1 is of type string or -1 if argument 1 is of type real.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_maparray) | | |
| [◄ ManageMeasureDialog](func_managemeasuredialog.htm) |  | [max ▶](func_max.htm) |
