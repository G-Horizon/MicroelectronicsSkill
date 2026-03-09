# GetInstancePinLocs Function

Return an array of pin locations for the symbol identified by arguments 1 and 2.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Property name |
| 2 | string | No |  | Property value |
| 3 | string | No | 'relative' | Options |
| 4 | real | No | -1 | Schematic ID |

#### Argument 1

Property name to identify instance. Along with parameter 2, if these arguments are not supplied, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 2

Property value to identify instance. Along with parameter 1, if these arguments are not supplied, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 3

If set to 'absolute', the values returned will be relative to a fixed origin on the schematic. Otherwise they will be relative to the origin of the instance. The origin of an instance can be determined using the function  [InstPoints](func_instpoints.htm) .

#### Argument 4

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinstancepinlocs) | | |
| [◄ GetInstanceParamValues](func_getinstanceparamvalues.htm) |  | [GetInstsAtPoint ▶](func_getinstsatpoint.htm) |
