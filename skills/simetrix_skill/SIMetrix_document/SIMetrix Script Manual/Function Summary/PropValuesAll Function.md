# PropValuesAll Function

Returns the values for the requested property. This will search all selected elements within a schematic. There are optional filters for choosing elements with a particular property, or property and value combination, along with options to select a specific schematic.

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

* [PropValuesAnnotations](func_propvaluesannotations.htm)
* [PropValuesWires](func_propvalueswires.htm)

### Example

The following would return all of the value for the `ref` property with the selected schematic, for elements that have the property `MODEL` set to `X` :

```
PropValuesAll('ref','model','X')
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_propvaluesall) | | |
| [◄ PropValues2](func_propvalues2.htm) |  | [PropValuesAnnotations ▶](func_propvaluesannotations.htm) |
