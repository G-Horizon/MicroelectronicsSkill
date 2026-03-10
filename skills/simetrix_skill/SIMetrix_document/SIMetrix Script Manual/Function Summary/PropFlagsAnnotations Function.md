# PropFlagsAnnotations Function

Returns the flags for the requested property. This will search selected annotations only within a schematic. There are optional filters for choosing elements with a particular property, or property and value combination, along with options to select a specific schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name to retrieve flags for |
| 2 | string | No |  | Filter property name |
| 3 | string | No |  | Filter property value |
| 4 | real | No | -1 | Schematic ID |

#### Argument 1

The name of the property that we are returning the flags for.

#### Argument 2

If set, will only select elements that have this property in them.

#### Argument 3

If set, will only select elements that have the property stated by argument 2, with the value stated by this argument.

#### Argument 4

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

Returns the property flags for all applicable properties. Each row of the resulting array will be a different element's property flag.

### See Also

* [PropFlagsAll](func_propflagsall.htm)
* [PropFlagsWires](func_propflagswires.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propflagsannotations) | | |
| [◄ PropFlagsAll](func_propflagsall.htm) |  | [PropFlagsWires ▶](func_propflagswires.htm) |
