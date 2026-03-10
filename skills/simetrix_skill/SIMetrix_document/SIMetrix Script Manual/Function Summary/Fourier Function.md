# Fourier Function

Calculates the fourier spectrum of the data in argument 1. The function uses the 'Continuous Fourier' technique which numerically integrates the Fourier integral. Because this technique does not require the input data to be sampled at evenly spaced points, it doesn't suffer from frequency aliasing. This is the main drawback of the more commonly used FFT (Fast Fourier Transform) algorithm. However, the Continuous Fourier algorithm is much slower then the FFT, sometimes dramatically so.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | data |
| 2 | real | Yes |  | Fundamental frequency |
| 3 | real | Yes |  | Number of frequency terms |
| 4 | real array | No |  | options |

#### Argument 1

The input data. This is expected to possess a reference i.e. x-values

#### Argument 2

Specifies the fundamental frequency. All terms calculated will be an integral multiple of this.

#### Argument 3

Specifies the number of frequency terms to be calculated.

#### Argument 4

This is optional and can be a 1 or 2 element array. The first element is the first frequency to be calculated expressed as a multiple of the fundamental. The default value is 0 i.e. the DC term is calculated first. The second element is the integration order used and may be 1 or 2.

### Returns

Return type: complex XY array

The result of the calculation and will be a complex array with length equal to argument 3.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_fourier) | | |
| [◄ FormatNumber](func_formatnumber.htm) |  | [FourierOptionsDialog ▶](func_fourieroptionsdialog.htm) |
