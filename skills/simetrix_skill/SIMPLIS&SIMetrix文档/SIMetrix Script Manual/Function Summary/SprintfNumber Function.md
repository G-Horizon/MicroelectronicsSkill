# SprintfNumber Function

Returns a string formatted according to a format specification.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Format |
| 2 | real ... | No |  | Arguments 1-8: values |

#### Argument 1

Format specification. The format used is essentially the same as that used for the 'printf' range of functions provided in the 'C' programming language. However, only real arguments are supported and so only format types %e, %E, %f, %g and %G are supported.

#### Argument 2

Values used for '%' format specs in the format string. Upto 8 argument values may be used.

### Returns

Return type: string

Formatted string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_sprintfnumber) | | |
| [◄ SplitString](func_splitstring.htm) |  | [sqrt ▶](func_sqrt.htm) |
