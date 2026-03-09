# fft Function

Performs a Fast Fourier Transform on supplied vector. The number of points used is the next binary power higher than the length of argument 1.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | vector |
| 2 | string | No | 'Hanning' | window function |

#### Argument 2

Values are either 'Hanning' (default) or 'None'.

### Returns

Return type: complex XY array

### Notes

User's should note that using this function applied to raw transient analysis data will not produce meaningful results as the values are unevenly spaced. If you apply this function to simulation data, you must either specify that the simulator outputs at fixed intervals (select the Output at .PRINT step option in the **Simulator** > **Choose Analysis...** dialog box) or you must interpolate the results using the  [Interp](func_interp.htm)  function. The FFT plotting menu items run a script which interpolate the data if it detects that the results are unevenly spaced. Use of these menus does not require special consideration by the user.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_fft) | | |
| [◄ fd](func_fd.htm) |  | [Field ▶](func_field.htm) |
