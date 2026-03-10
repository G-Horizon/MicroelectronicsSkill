# Interp Function

Interpolates the data in argument 1 either to a fixed number of points or at a specified interval.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Vector to be interpolated |
| 2 | real | Yes |  | Number of points |
| 3 | real | No | 2 | Interpolation order |
| 4 | real | No |  | Mode |

#### Argument 1

Vector to be interpolated. The data should have a reference (x-values, see  [Vector References](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__vectorreferences)  ) but this is not compulsory when interpolating using a fixed number of points as opposed to a fixed interval.

#### Argument 2

Either the number of points or the x interval depending on the mode. (See argument 4 below)

#### Argument 3

Interpolation order. This can be any integer 1 or greater but in practice there are seldom reasons to use values greater than 4. If interpolating a signal containing fast pulses, interpolation order should be set to 1.

#### Argument 4

Two element boolean array, that is its values should be either TRUE (1) or FALSE (0). The second element specifies the mode. If 0 (FALSE) then the function uses the fixed number of points mode and argument 2 provides the number of points. If 1 (TRUE) the mode is fixed interval mode and argument 2 specifies the interval. The first element is only used with fixed number of points mode. If TRUE the final point of the interpolated result will coincide with the final point of the input vector and the interval between points is T/(N-1) where T is the interval of the whole input vector and N is the number of points. If FALSE the interval is T/N and the final point is at a location T/N before the final input point. The latter behaviour is compatible with earlier versions and is also what should be used if the function is interpolating data to be used by the FFT function.

### Returns

Return type: real array. If argument 1 is an XY vector, the return value will be an XY vector

Returns the interpolated data.

### Notes

The Interp function overcomes some of the problems caused by the fact that raw transient analysis results are unevenly spaced. It is used by the FFT plotting scripts to provide evenly spaced sample points for the function  [fft](func_fft.htm) .

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_interp) | | |
| [◄ integ](func_integ.htm) |  | [IsComplex ▶](func_iscomplex.htm) |
