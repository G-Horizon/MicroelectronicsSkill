# LPF Function

Applies a continuous time single pole low pass filter to input data. Unlike the  [IIR](func_iir.htm)  and  [FIR](func_fir.htm)  functions, this function does not require the input data to be sampled. That is it can use simulation data directly without requiring interpolation.

This function can be used with multi-division data.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | Input data |
| 2 | Real | Yes |  | Time constant |
| 3 | Real | No | First input value | Initial condition |

#### Argument 1

Input data. This is expected to be an XY vector with both X and Y values. The function will return an empty vector if this is not the case.

#### Argument 2

Time constant

#### Argument 3

Initial condition. Specifies the output value for the first point

### Returns

Return type: real XY array

Result

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_lpf) | | |
| [◄ log10](func_log10.htm) |  | [mag ▶](func_mag.htm) |
