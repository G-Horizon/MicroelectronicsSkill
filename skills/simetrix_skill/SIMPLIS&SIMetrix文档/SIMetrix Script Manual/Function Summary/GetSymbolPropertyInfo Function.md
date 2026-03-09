# GetSymbolPropertyInfo Function

Returns information about symbol editor symbol properties.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Property name |

### Returns

Return type: string array

Returns a string array of length 5 providing information on either a single property as defined in the argument or the currently selected properties.

If more than one property or pin is selected, the information provided in elements 0-2 will be either the property or the pin, however there are no rules to determine which. The displayed names used for pins are represented as properties and this function can be used to gain information about them. The equivalent property name for a pin is the pin name prefixed with $Pin$.

Format of result is as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Property name |
| 1 | Property flags value (see  [Prop Attribute flags](com_prop.htm)  for details.) |
| 2 | Property value |
| 3 | Number of properties selected |
| 4 | Number of pins selected |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsymbolpropertyinfo) | | |
| [◄ GetSymbolOrigin](func_getsymbolorigin.htm) |  | [GetSymbolPropertyNames ▶](func_getsymbolpropertynames.htm) |
