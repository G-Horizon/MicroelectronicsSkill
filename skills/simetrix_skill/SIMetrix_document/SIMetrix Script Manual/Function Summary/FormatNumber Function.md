# FormatNumber Function

Formats a real value or vector of values and returns a string representation.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | number or vector of numbers |
| 2 | real | Yes |  | significant digits |
| 3 | string | No | 'eng' | format |

#### Argument 3

Format options are:

|  |  |
| --- | --- |
| 'eng' | (default if omitted). Formats the number using engineering units |
| 'noeng' | Normal format. Will use 'E' if necessary |
| 'int' | Integer format. Returns integer rounded to nearest value. Note rounding is |
| in the same direction for negative and positive values. -1.2 -> -1, -1.7 -> -2.0 |  |
| '%' | Formats as a percentage |

### Returns

Return type: string or string array

String representation of input data

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_formatnumber) | | |
| [◄ floorv](func_floorv.htm) |  | [Fourier ▶](func_fourier.htm) |
