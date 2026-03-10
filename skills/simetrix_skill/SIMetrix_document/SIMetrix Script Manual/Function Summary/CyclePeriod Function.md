# CyclePeriod Function

Returns the time between zero crossing pairs with the same slope direction. It can be used for plotting frequency vs time by using 1/CyclePeriod.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY vector | Yes |  | Input vector |
| 2 | real | Yes |  | Baseline |
| 3 | real | No | 2 | Interpolation order |
| 4 | real | No | 0 | X start position (0, 1 or 2) |

#### Argument 1

Input vector to be processed.

#### Argument 2

Baseline for zero-crossing detection.

#### Argument 3

Interpolation order, may be 1 or 2. The actual zero crossing point from which the measurements are based are calculated by interpolation from points either side of the zero-crossing. This sets the order of the interpolation algorithm.

#### Argument 4

Can be 0, 1 or 2. This shifts the x-axis of the result. So for example if the input vector is a 1kHz sine wave, the first element of the result will be the duration of the first cycle - i.e 1mS. What this argument does is set what the x value will be. If set to 0, it will be 1mS - i.e the location of the end of the first cycle. If set to 1, it will be 0.5mS - i.e the location of the end of the first half-cycle and if set to 2, it will be 0, i.e the start of the input.

### Returns

Return type: real XY Array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_cycleperiod) | | |
| [◄ cv](func_cv.htm) |  | [Date ▶](func_date.htm) |
