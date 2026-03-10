# StyleNames Function

Returns a list of existing style names. If no schematic is open, only global styles will be returned

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Optional arguments |

#### Argument 1

If set, each element can provide an optional argument. Options are:

|  |  |
| --- | --- |
| **Argument** | **Description** |
| global | Returns only global styles. |
| NotProperty | Returns only styles that are not property styles. |
| Property | Returns only styles that are property styles. |

### Returns

Return type: string array

List of in use style names.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_stylenames) | | |
| [◄ StyleLineTypes](func_stylelinetypes.htm) |  | [SubstChar ▶](func_substchar.htm) |
