# PropFlags2 Function

Returns the attribute flags for instances identified by arguments 3 and 4. See "Attribute flags" in the command  [Prop](com_prop.htm)  for details.

This function replaces PropFlags. Its behaviour is similar but the arguments have been rearranged and its behaviour in the event of no instance match is different.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name (for flags) |
| 2 | real | No | -1 | Schematic ID |
| 3 | string | No | Selected components | Property name (for id) |
| 4 | string | No | Instances with property name in arg 2 | Property value (for id) |

#### Argument 1

Property whose flags are to be returned.

#### Argument 2

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

#### Argument 3

ALong with agument 4, if present these arguments identify the instances to be examined. If only argument 3 is specified then all instances on the current schematic that possess that property will be used. If argument 4 is also present then the instance name and value must match argument 3 and 4 respectively. If neither are present the selected instances will be used.

#### Argument 4

See argument 3.

### Returns

Return type: string array

The function returns a string array of length equal to the number of instances identified by arguments 3 and 4. Each element will hold a flag value for the property specified in argument 1.

Note that this function compliments the functions  [PropValues2](func_propvalues2.htm)  and  [SymbolNames](func_symbolnames.htm)  and will return the same number of values and in the same order, provided the same instance identifying arguments are given.

The function will return an empty  *vector*  if no instances match arguments 3 and 4. This differs from PropFlags which returns an empty  *string*  in this situation. The behaviour of PropValues2 is much more convenient and it is recommended that this is used in all new scripts.

PropFlags2 will also return an empty vector if the specified schematic could not be found.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propflags2) | | |
| [◄ PropFlags](func_propflags.htm) |  | [PropFlagsAll ▶](func_propflagsall.htm) |
