# CheckLaplaceExpression Function

Checks a Laplace expression for correctness

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Expression to be analysed |

#### Argument 1

Expression to be analysed

### Returns

Return type: real

Integer value from -1 to 4 signifying the validity of the Laplace expression.

|  |  |
| --- | --- |
| **Value** | **Description** |
| } |  |
| -1 | Unknown error in expression |
| 0 | Expression is valid |
| 1 | Syntax error in expression |
| 2 | Mismatched parantheses in expression |
| 4 | Expression uses an unknown function |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_checklaplaceexpression) | | |
| [◄ Char](func_char.htm) |  | [ChooseDir ▶](func_choosedir.htm) |
