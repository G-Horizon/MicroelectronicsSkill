# CurveFitLogY Function

As  [CurveFit](func_curvefit.htm)  but applies a logarithm function to the Y-data prior to evaluating the curve fit function

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real array | Yes |  | Vector 1 for comparison |
| 2 | Real array | Yes |  | Vector 2 for comparison |

#### Argument 1

Vector 1 for comparison

#### Argument 2

Vector 1 for comparison

### Returns

Return type: Real

Scalar value indicating the difference between the two vectors. 0 means they are identical over their overlapping range. The function will return 1.0 if one argument is the reciprocal of the other

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_curvefitlogy) | | |
| [◄ CurveFitLogX](func_curvefitlogx.htm) |  | [cv ▶](func_cv.htm) |
