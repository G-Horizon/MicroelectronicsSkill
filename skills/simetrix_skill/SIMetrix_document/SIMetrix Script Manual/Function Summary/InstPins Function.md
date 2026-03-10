# InstPins Function

Returns an array of strings holding pin names for each pin of either the selected instance or an instance identified by one or both arguments.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Property name |
| 2 | string | No |  | Property value |
| 3 | real | No | -1 | Schematic ID |

#### Argument 1

Property name to identify instance. Along with argument 2, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

#### Argument 2

Property value to identify instance. Along with argument 1, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

#### Argument 3

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_instpins) | | |
| [◄ InstNets2](func_instnets2.htm) |  | [InstPoints ▶](func_instpoints.htm) |
