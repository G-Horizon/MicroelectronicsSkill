# XFromY Function

Returns an array of values specifying the horizontal location(s) where the specified vector (argument 1) crosses the given y value (argument 2). If the vector never crosses the given value, an empty result is returned. The sampled input vector is interpolated to produce the final result. Interpolation order is specified by argument 3.

Argument 4 specifies edge direction. If set to 0 either direction will be accepted. If set to 1 only positive edges will be detected and if set to -1 only negative edges will be detected.

Note that unlike other functions that use interpolation, XFromY can only use an interpolation order of 1 or 2. If a value larger than 2 is specified, 2 will be assumed.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | Input vector |
| 2 | real | Yes |  | Y value |
| 3 | real | No | 2 | Interpolation order (1 or 2) |
| 4 | real | No | 0 | Direction |

### Returns

Return type: real XY array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_xfromy) | | |
| [◄ XDatum](func_xdatum.htm) |  | [XMLCountElements ▶](func_xmlcountelements.htm) |
