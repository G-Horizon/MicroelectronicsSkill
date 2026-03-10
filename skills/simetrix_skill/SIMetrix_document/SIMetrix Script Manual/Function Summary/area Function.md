# area Function

Calculates the area under the curve of the argument.

This function returns a single value that can be used for measurements. The  [integ](func_integ.htm)  function may be used to obtain a vector of the area. area(arg) is equivalent to the value of (integ(arg))[length(arg)-1]

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Vector |
| 2 | real | No | 0.0 | Start x value |
| 3 | real | No | Final x value in data | End x value |

#### Argument 1

Vector to process. Must have a reference - e.g. x-values

#### Argument 2

Value on x-axis where the start of the curve area is located

#### Argument 3

Value on x-axis where the end of the curve area is located

### Returns

Return type: real

Area under curve

### Example

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_area) | | |
| [◄ AppendSensitivityData](func_appendsensitivitydata.htm) |  | [arg ▶](func_arg.htm) |
