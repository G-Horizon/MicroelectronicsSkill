# EscapeString Function

Process string to replace escaped characters with literals.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | input string |
| 2 | string | Yes |  | options |

#### Argument 1

Input string

#### Argument 2

Set to 'replacespaces' to enable \ s which is substituted with a single space

### Returns

Return type: string

Returns the input string but with the following character sequences substituted with their literal values as follows:

|  |  |
| --- | --- |
| \ t | Replaced with a tab character. (ASCII code 9) |
| \ n | Replaced with a new line character. (ASCII code 10) |
| \ r | Replaced with a carriage return character. (ASCII code 13) |
| \ f | Replaced with a form feed character. (ASCII code 12) |
| \ s | Replaced with a single space. Enabled is arg2 set to 'replacespaces'. Can be used to create strings that contain no spaces. |
| \ \ | Replaced by a single '\' |
| '\' followed by any other character | Replaced by the character following the '\'. The '\' itself is omitted. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_escapestring) | | |
| [◄ erfc](func_erfc.htm) |  | [EscapeStringEncode ▶](func_escapestringencode.htm) |
