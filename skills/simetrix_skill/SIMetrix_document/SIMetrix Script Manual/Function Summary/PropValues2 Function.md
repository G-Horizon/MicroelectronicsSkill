# PropValues2 Function

Returns a property value for instances identified by arguments 3 and 4.

This function replaces  [PropValues](func_propvalues.htm) . Its behaviour is similar but the arguments have been rearranged and its behaviour in the event of no instance match is different and more convenient.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name whose value is required |
| 2 | real array | No | -1 | Schematic handle and options |
| 3 | string | No | Use selected components if omitted | Property name to identify instance |
| 4 | string | No | All instances with property name in arg2 | Property value to identify instance |

#### Argument 1

Property whose value is to be returned.

#### Argument 2

First element is a schematic handle as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If equal to -1, the currently selected schematic will be used.

A second element may be supplied and if non-zero, the results will be sorted by location. Otherwise they will not be sorted.

If a third element is present and set to a non-zero value, symbolic properties will be resolved.

If a fourth element is provided and set to a non-zero value, the function will not return instances that are disabled.

#### Argument 3

Along with argument 4, if present these arguments identify the instances to be examined. If only argument 2 is specified then all instances on the specified schematic that possess that property will be used. If argument 3 is also present then the instance name and value must match argument 2 and 3 respectively. If neither are present the selected instances will be used.

#### Argument 4

See argument 3.

### Returns

Return type: string array

The function returns a string array of length equal to the number of instances identified by arguments 2 and 3. Each element will hold a value for the property specified in argument 1.

Note that this function is analogous to the functions  [PropFlags2](func_propflags2.htm)  and  [SymbolNames](func_symbolnames.htm)  and for identical values of arguments 3 and 4 will return an array of the same length and in the same order.

The function will return an empty  *vector*  if no instances match arguments 3 and 4. This differs from PropValues which returns an empty  *string*  in this situation. The behaviour of PropValues2 is much more convenient and it is recommended that this is used in all new scripts.

PropValues2 will also return an empty vector if the specified schematic could not be found.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propvalues2) | | |
| [◄ PropValues](func_propvalues.htm) |  | [PropValuesAll ▶](func_propvaluesall.htm) |
