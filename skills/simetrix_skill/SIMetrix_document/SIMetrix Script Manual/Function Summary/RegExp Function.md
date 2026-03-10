# RegExp Function

Match an input string to a sequence of regular expressions. The first expression is matched to to the input string and the result returned in the first element of the return array. If the expression does not match from the first character of the input string, the pattern matching will advance to subsequent characters until a match is found. The process is then repeated for subsequent expressions until all have been processed or no match is found.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String array | Yes |  | Array of regular expressions |
| 2 | String | Yes |  | Input string |

#### Argument 1

Array of regular expressions. The input string is matched in sequence

#### Argument 2

Input string

### Returns

Return type: String array

First element is either 'CompleteMatch' or 'InCompleteMatch'. 'CompleteMatch' will be returned if all regular expressions are matched to the input string without skipping any characters.

Subsequent fields contain the parts of the string that match the corresponding regular expression.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexp) | | |
| [◄ RegExMatch](func_regexmatch.htm) |  | [RegExReplace ▶](func_regexreplace.htm) |
