# YFromX Function

Returns array of values specifying the vertical value of the specified vector at the given x value.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | Input vector |
| 2 | real | Yes |  | X value |
| 3 | real | No | 2 | Interpolation order (1 or greater) |

### Returns

Return type: real XY array

Returns an array of values (usually a single value) specifying the vertical value of the specified vector (argument 1) at the given x value (argument 2). If the given x-value is out of range an empty result (see page 28) is returned. The sampled input vector is interpolated to produce the final result. Interpolation order is specified by argument 3.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_yfromx) | | |
| [◄ YDatum](func_ydatum.htm) |  | [Command Summary ▶](commandsummary.htm) |
