# DefineFourierDialog Function

Opens the Define Fourier dialog box used to specify a fourier transform. This is similar to the  [DefineCurveDialog](func_definecurvedialog.htm)  but has an extra tabbed sheet to define the fourier analysis options. Select menu **Probe** > **Fourier** > **Arbitrary...** to see how this dialog box looks.

The function takes an argument that is a string array with up to 37 elements which initialises the controls in the dialog box. The first 25 have the same function as for the  [DefineCurveDialog](func_definecurvedialog.htm)  () function. The remaining are described in the following table:

|  |  |  |
| --- | --- | --- |
| **Index** | **Description** | **Default** |
| 0-24 | See  [DefineCurveDialog](func_definecurvedialog.htm) |  |
| 25 | Fundamental Frequency | 100 |
| 26 | Frequency display - Start Frequency | <<empty>> |
| 27 | Frequency display - Stop Frequency | 10K |
| 28 | Number of points for FFT interpolation | 256 if arg 2 not specified. See below |
| 29 | Interpolation order for FFT | 2 |
| 30 | Fourier method. Possible values: |  |  | | --- | --- | | 'continuous' | Use continuous fourier | | 'interpolated' | Use interpolated FFT | | 'continuous' |
| 31 | Window function. Possible values: |  | | --- | | 'rectangular' | | 'hanning' | | 'hamming' | | 'blackman' | | 'hanning' |
| 32 | Start of data span | 0 |
| 33 | End of data span | 0.01 |
| 34 | Use specified span: TRUE/FALSE | FALSE |
| 35 | Know fundamental frequency: TRUE/FALSE | FALSE |
| 36 | Resolution | 100 |
| 37 | Plot options - 'mag', 'db' or 'phase' |  |

A second argument may be specified to provide time domain information. Usually this would be the 'time' vector created by the simulation. The vector is analysed to find the start time, stop time and number of interpolation points. The number of interpolation points is calculated from the number of points in the time vector and is the next highest integral power of 2.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial values |
| 2 | real array | No |  | sample vector |

### Returns

Return type: string array

The function returns a string array with the same format as the argument. If the user selects Cancel, the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definefourierdialog) | | |
| [◄ DefineDACDialog](func_definedacdialog.htm) |  | [DefineFourierProbeDialog ▶](func_definefourierprobedialog.htm) |
