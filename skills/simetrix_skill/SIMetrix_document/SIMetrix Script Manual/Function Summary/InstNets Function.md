# InstNets Function

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Options |

#### Argument 1

Returns an array of strings holding netnames for each pin of the selected schematic instance. Circuit must have been netlisted for the result of the function to be meaningful. This function is used by the power script to find the power dissipated in a device.

If argument 1 is set to 'flat' the resulting netnames will be stripped of hierarchical references.

The function will return with an error if no instances are selected or more than one instance is selected.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_instnets) | | |
| [◄ Instances](func_instances.htm) |  | [InstNets2 ▶](func_instnets2.htm) |
