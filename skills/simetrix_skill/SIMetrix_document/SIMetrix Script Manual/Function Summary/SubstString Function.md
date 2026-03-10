# SubstString Function

Replaces a substring in a string. This function is case sensitive.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to process |
| 2 | string | Yes |  | Search string |
| 3 | string | Yes |  | Substitute string |
| 4 | string | No |  | Options |

#### Argument 1

Input string.

#### Argument 2

Substring searched in input string. This is case sensitive when it searches.

#### Argument 3

The substring defined in argument 2 found in the input string is replaced with this value. If arg 4 is set to 'all' all substrings found will be replaced, otherwise only the first will be replaced.

#### Argument 4

Options. If set to 'all', then all substrings located in the string will be replaced. Otherwise, only the first occurrence will be replaced.

### Returns

Return type: string

Result of string substitution. Note that only the first occurrence of the substring is replaced.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_subststring) | | |
| [◄ SubstProbeExpression](func_substprobeexpression.htm) |  | [sum ▶](func_sum.htm) |
