# Spectrum Function

Simple function that computes the Fourier spectrum of input data using FFT with basic settings. Uses Hanning Window and second order interpolation.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Input data |
| 2 | Real | Yes |  | Number of points |
| 3 | Real | No | 0 | Start time |
| 4 | Real | No | Last time point | End time |

#### Argument 1

Input data to be processed

#### Argument 2

Number of points. If a number that is not a binary power is provided, the next highest binary power will be used For example if this argument is 1000, the value 1024 will be used

#### Argument 3

Start time

#### Argument 4

End time

### Returns

Return type: Complex

Input data converted to time domain using the FFT algorithm

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_spectrum) | | |
| [◄ SourceDialog](func_sourcedialog.htm) |  | [SpectrumUniv ▶](func_spectrumuniv.htm) |
