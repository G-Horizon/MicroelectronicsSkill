# Instances Function

Returns array of property values of property name specified as argument. A value will be returned for every instance on the schematic that possesses that property. (An instance is a schematic item represented by a symbol - components, ground symbols etc.) For example, Instances('ref') would return every component reference in the schematic.

Note that every instance has a unique 'Handle' property which is automatically assigned. This makes it possible to access every instance on the schematic.

The second argument is a schematic handle as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

The function will return an empty vector if no schematic is open or argument 2 is invalid. An empty  *string*  will be returned if no instance possess the specified property. The latter behaviour is not always convenient but is retained for backward compatibility. The function  [PropValues2](func_propvalues2.htm)  , with appropriate arguments, will return an empty  *vector*  when there is no match, and thus easier to use in many cases.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | real | No | -1 | Schematic ID |

#### Argument 2

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_instances) | | |
| [◄ InputSchem](func_inputschem.htm) |  | [InstNets ▶](func_instnets.htm) |
