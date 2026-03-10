# PWLCurveFit Function

Returns a real vector weith a Piecewise Linear Approximation of the input real array. The number of PWL segments is determined by the second argument. See the argument definitions for specialized curve fits and additional options.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | The XY input vector |
| 2 | real | Yes |  | The number of segments |
| 3 | string | No |  | Specifies the use of a specialized algorithm |
| 4 | real | No |  | Fix the last PWL point? |
| 5 | real | No |  | Optional parameters |

#### Argument 1

The vector to process. Must have a reference (x values).

#### Argument 2

The number of segments of the resulting piecewise linear approximation.

#### Argument 3

Sets the type of algorithm to use. Can be 'generic', 'diode', 'capacitor', or 'inductor'.

#### Argument 4

Fixes the last PWL point to be the last data point of the input vector

#### Argument 5

Optional parameters for the 'generic', 'diode', and 'inductor' algorithms. For 'diode', a number (resistance) greater than 0 will force the first segment to have a slope of 1/resistance. 0 will force the first segment to have a slope of 0. For 'inductor', 1 will symmetrically fit the curve around (0,0). For 'generic', 1 will curve fit through point (0,0).

### Returns

Return type: real array

----

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_pwlcurvefit) | | |
| [◄ PutEnvVar](func_putenvvar.htm) |  | [PWLDialog ▶](func_pwldialog.htm) |
