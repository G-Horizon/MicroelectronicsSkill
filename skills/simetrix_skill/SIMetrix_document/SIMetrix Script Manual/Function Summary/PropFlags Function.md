# PropFlags Function

Returns the attribute flags for instances identified by arguments 2 and 3. See "Attribute Flags" in the command  [Prop](com_prop.htm)  for details. This function has been superseded by  [PropFlags2](func_propflags2.htm)  and it is not recommended for new scripts. PropFlags2 has rearranged arguments allowing the schematic handle to be specified without requiring the property value to provided. It also has more convenient behaviour in the situation when there is no instance match.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name (for flags) |
| 2 | string | No | Selected components | Property name (for id) |
| 3 | string | No | Instances with property name in arg 2 | Property value (for id) |
| 4 | real | No | -1 | Schematic ID |

#### Argument 1

Property whose flags are to be returned.

#### Argument 2

Along with argument 3, if present these arguments identify the instances to be examined. If only argument 2 is specified then all instances on the current schematic that possess that property will be used. If argument 3 is also present then the instance name and value must match argument 2 and 3 respectively. If neither are present the selected instances will be used.

#### Argument 3

See argument 2.

#### Argument 4

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

The function returns a string array of length equal to the number of instances identified by arguments 2 and 3. Each element will hold a flag value for the property specified in argument 1.

The function will return an empty vector if the specified schematic could not be found. If no instance matches arguments 2 and 3, an empty  *string*  will be returned.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propflags) | | |
| [◄ Progress](func_progress.htm) |  | [PropFlags2 ▶](func_propflags2.htm) |
