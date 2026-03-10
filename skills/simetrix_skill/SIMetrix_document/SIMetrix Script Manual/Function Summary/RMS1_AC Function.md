# RMS1\_AC Function

Returns the root mean square value of the supplied vector offset by its mean between the ranges specified by arguments 2 and 3. If the values supplied for argument 2 and/or 3 do not lie on sample points, second order interpolation will be used to estimate y values at those points.

Offsetting the input data by its mean effectively AC couples the data so that any DC component in the data is removed.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Vector |
| 2 | real | No | Start of input vector | Start x value |
| 3 | real | No | End of input vector | End x value |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_rms1_ac) | | |
| [◄ RMS1](func_rms1.htm) |  | [rnd ▶](func_rnd.htm) |
