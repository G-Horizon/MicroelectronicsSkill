# GetNearestNet Function

Returns information about the schematic net nearest the mouse cursor

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array of length 3 providing information on the net nearest the mouse cursor. The elements of the array are defined in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Local net name e.g. V1\_P. |
| 1 | Net name prefixed with hierarchical path e.g. U1.V1\_P |
| 2 | '1' if the net is a bus connections, otherwise '0' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getnearestnet) | | |
| [◄ GetNamedSymbolPropValue](func_getnamedsymbolpropvalue.htm) |  | [GetNextDefaultStyleName ▶](func_getnextdefaultstylename.htm) |
