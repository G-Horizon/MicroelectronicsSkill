# InstNets2 Function

Returns an array of strings holding the netnames of a schematic instance defined by arguments 1 to 3.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Schematic ID |
| 2 | string | Yes |  | Property name |
| 3 | string | Yes |  | Property value |
| 4 | string | No |  | Options |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If -1 the currently selected schematic will be used.

#### Argument 2

Property name to identify instance. Along with parameter 3, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 3

Property value to identify instance. Along with parameter 2, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 4

If set to 'full', the full hierarchical path of the net names will be supplied. Otherwise the local names will be returned.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_instnets2) | | |
| [◄ InstNets](func_instnets.htm) |  | [InstPins ▶](func_instpins.htm) |
