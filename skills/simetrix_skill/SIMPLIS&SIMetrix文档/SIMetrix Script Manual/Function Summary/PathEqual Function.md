# PathEqual Function

Compares two string arrays and returns a real array of the same length with each element holding the result of a string comparison between corresponding input elements. The string comparison assumes that the input arguments are file system path names and will choose case sensitivity according to the underlying operating system. The comparison will be case insensitive.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Path 1 |
| 2 | string array | Yes |  | Path 2 |

#### Argument 1

First pathname or pathnames to be compared.

#### Argument 2

Second pathname or pathnames to be compared.

### Returns

Return type: real array

Real array of the same length as the arguments. If the lengths of the arguments are different, an empty vector will be returned. Each element in the array will be either -1, 0, or +1. 0 means the two strings are identical (subject to case sensitivity as described above).

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_pathequal) | | |
| [◄ ParseSpiceLines](func_parsespicelines.htm) |  | [PerCycleTiming ▶](func_percycletiming.htm) |
