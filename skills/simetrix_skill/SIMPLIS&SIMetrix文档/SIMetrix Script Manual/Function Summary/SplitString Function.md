# SplitString Function

Takes two values, the string and the sub string token. Returns the token removed and the string split into new sub-strings.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Input string |
| 2 | string | Yes |  | token |

### Returns

Return type: string array

String array containing the component parts of the string

### Example

SplitString('fred/bill/jill', 'bill') ['fred/', '/jill'] SplitString('fred/bill/bill/jill', 'bill') ['fred/', '/', '/jill']

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_splitstring) | | |
| [◄ SplitPath](func_splitpath.htm) |  | [SprintfNumber ▶](func_sprintfnumber.htm) |
