# GetInstanceConvergenceInfo Function

Returns convergence information about a device. Requires ".OPTIONS advConvReport" to be specified in the simulation netlist.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Device reference |
| 2 | Real | No | 0 | Start index |
| 3 | Real | No |  | Output option |

#### Argument 1

Device reference

#### Argument 2

Start index

#### Argument 3

If omitted, the return value is a string array providing all information available for the specified device.

Otherwise an integer value may be specified which defined the item to be returned as a numeric array.

### Returns

Return type: See notes for argument 3

See notes for argument 3

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinstanceconvergenceinfo) | | |
| [◄ GetInstanceBounds](func_getinstancebounds.htm) |  | [GetInstanceParamValues ▶](func_getinstanceparamvalues.htm) |
