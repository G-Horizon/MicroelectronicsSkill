# EscapeStringEncode Function

Process string and replace literals with escaped characters. Performs the reverse operation to  [EscapeString](func_escapestring.htm)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | input string |

#### Argument 1

Input string

### Returns

Return type: string

Returns the input string but with the following literal values substituted with character sequences as follows:

|  |  |
| --- | --- |
| **Literal value** | **Replaced with:** |
| Tab character (ASCII code 9) | \ t |
| New line character (ASCII code 10) | \ n |
| Carriage return character (ASCII code 13) | \ r |
| Form feed character (ASCII code 12) | \ f |
| '\' | \ \ |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_escapestringencode) | | |
| [◄ EscapeString](func_escapestring.htm) |  | [ev ▶](func_ev.htm) |
