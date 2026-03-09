# FIR Function

Performs "Finite Impulse Response" digital filtering on supplied vector. This function performs the operation:

\[ y\_n = x\_n \cdot c\_0 + x\_{n-1} \cdot c\_1 + x\_{n-2} \cdot c\_2 + \dots \]

Where:

|  |  |
| --- | --- |
| ???MATH???x???MATH??? | is the input vector (argument 1) |
| ???MATH???c???MATH??? | is the coefficient vector (argument 2) |
| ???MATH???y???MATH??? | is the result (returned value) |

The third argument provide the 'history' of ???MATH???x???MATH??? i.e. ???MATH???x\_{-1}???MATH???, ???MATH???x\_{-2}???MATH??? etc. as required.

Below is the simple case of a four sample rolling average.

User's should note that using this function applied to raw transient analysis data will not produce meaningful results as the values are unevenly spaced. If you apply this function to simulation data, you must either specify that the simulator outputs at fixed intervals (select the Output at .PRINT step option in the **Simulator** > **Choose Analysis...** dialog box) or you must interpolate the results using the  [Interp](func_interp.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | vector to be filtered |
| 2 | real array | Yes |  | filter coefficients |
| 3 | real array | No | All zero | initial conditions |

### Returns

Return type: real array. If argument 1 is an XY vector, the return value will be an XY vector

### See Also

* [IIR](func_iir.htm)

### Example

Suppose a vector VOUT exist in the current group (simulation results). The following will plot VOUT with a 4 sample rolling average applied

```
Plot FIR(vout, [0.25, 0.25, 0.25, 0.25])
```

Alternatively, the following does the same

```
Plot FIR(vout, 0.25*unitvec(4))
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_fir) | | |
| [◄ FindModel](func_findmodel.htm) |  | [Floor ▶](func_floor.htm) |
