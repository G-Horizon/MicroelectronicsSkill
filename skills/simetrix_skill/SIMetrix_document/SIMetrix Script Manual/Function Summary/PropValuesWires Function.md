# PropValuesWires Function

Returns the values for the requested property. This will search selected wires only within a schematic. There are optional filters for choosing elements with a particular property, or property and value combination, along with options to select a specific schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name to retrieve values for |
| 2 | string | No |  | Filter property name |
| 3 | string | No |  | Filter property value |
| 4 | real | No |  | Schematic handle |

#### Argument 1

The name of the property to return the values for.

#### Argument 2

If set, will only choose elements that have this property in them.

#### Argument 3

If set, will only choose elements that have the property stated by argument 2, with the value stated by this argument.

#### Argument 4

Handle to a particular schematic. If not set, uses the currently highlighted schematic.

### Returns

Return type: string array

Returns the property values for all applicable properties. Each row of the resulting array will be a different element's property flag.

### See Also

* [PropValuesAll](func_propvaluesall.htm)
* [PropValuesAnnotations](func_propvaluesannotations.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propvalueswires) | | |
| [◄ PropValuesAnnotations](func_propvaluesannotations.htm) |  | [PutEnvVar ▶](func_putenvvar.htm) |
