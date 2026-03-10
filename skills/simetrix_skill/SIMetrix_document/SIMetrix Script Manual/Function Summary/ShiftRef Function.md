# ShiftRef Function

Returns a real vector which is a copy of the original vector, but with the reference (x-axis) values shifted by the amount specified by the second argument. If the second argument is not provided, the function returns the original vector shifted so that the first data point has a reference value of 0. The y-values of the vector are unaffected by this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | The input vector |
| 2 | real | No |  | The value to shift the reference value by |

#### Argument 1

The vector to process

#### Argument 2

The x axis will be shifted by this amount.

### Returns

Return type: real array

The original vector, with the reference shifted by the amount specified by the second argument, or, if the second argument is not provided, the vector is shifted so the reference vector is shifted to zero.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_shiftref) | | |
| [◄ ShellExecute](func_shellexecute.htm) |  | [sign ▶](func_sign.htm) |
