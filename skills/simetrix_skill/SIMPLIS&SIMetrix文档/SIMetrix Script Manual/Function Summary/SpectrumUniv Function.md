# SpectrumUniv Function

General purpose function performs a Fourier analysis on a vector. This function is used by the schematic's fixed Fourier probe.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real vector | Yes |  | Input signal |
| 2 | real vector | Yes |  | Configuration |

#### Argument 1

Input signal

#### Argument 2

real vector to configure operation on function.

|  |  |
| --- | --- |
| **Index** | **Description** |
| } |  |
| 0 | Method |
|  | 0: FFT |
|  | 1: Continuous Fourier |
| 1 | Output |
|  | 0: complex |
|  | 1: magnitude |
|  | 2: dB |
|  | 3: phase (degrees) |
|  | 4: dBuV |
| 2 | Use default resolution. Continuous Fourier only |
|  | 0: Use resolution in arg3 |
|  | 1: Use default resolution |
| 3 | Resolution. Continuous Fourier only |
| 4 | Start frequency |
|  | Actual start frequency will be N\*actual\_resolution where N is an integer |
| 5 | Stop frequency |
|  | FFT: max Numpoints\*resolution/2. Defaults to Numpoints\*resolution/2 if <=0. |
|  | Continuous Fourier: fails if<=0 |
| 6 | Know fundamental frequency |
| 7 | Fundamental frequency |
| 8 | FFT only - number of points - must be ???MATH???2^N???MATH???. |
|  | If not next value that is ???MATH???2^N???MATH??? is used |
| 9 | FFT only - interp order |
| 10 | 0: Time interval defined by arg12 and arg11 |
|  | 1: Use all time data |
| 11 | t start (if arg10=0) |
| 12 | t stop (if arg10=0) |
| 13 | Window |
|  | 0: Rectangular |
|  | 1: Hanning |
|  | 2: Hamming |
|  | 3: Blackman |
| 14 | Max calculation time - aborts if exceeds this value. |

### Returns

Return type: complex array

Fourier spectrum of input

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_spectrumuniv) | | |
| [◄ Spectrum](func_spectrum.htm) |  | [SplitPath ▶](func_splitpath.htm) |
