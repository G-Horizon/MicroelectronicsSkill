# ParseSpiceLines Function

Parses a string in SPICE format and returns each line in a string array. Handles '+' continuation characters by combining to a single line. Whole comment lines (starting with '\*') are returned normally but in-line comments using ';' are removed.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Input string |

#### Argument 1

Input string

### Returns

Return type: String array

Each element of the array represents a complete SPICE line.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parsespicelines) | | |
| [◄ ParseSIMPLISInit](func_parsesimplisinit.htm) |  | [PathEqual ▶](func_pathequal.htm) |
