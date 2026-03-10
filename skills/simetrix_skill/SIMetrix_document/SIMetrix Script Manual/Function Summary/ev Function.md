# ev Function

Special function used to evaluate a sequence of expressions without requiring multiple Let statements. Useful for schematic TEMPLATEs and similar.

This function may be supplied with up to 8 arguments. All arguments except the last is ignored by the function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | any type | Yes |  | vector |
| 2 | any type | No |  | vector |
| 3 | ... Up to 8 arguments in total | No |  |  |

### Returns

Return type: real/complex array

The function returns the value of the last argument supplied

### Notes

The purpose of this function is to allow the evaluation of intermediate variables withing a single expression. This is useful when the expression is in a schematic or graph template, for example, where there is only the facility available to enter a single expression. For example:

```
ev(x=3,x*x)
```

returns 9. The first argument is evaluated and assigns 3 to x. The second argument is then evaluated using the value of x assigned in argument 1. In a script, it would be more conventional to use the 'Let' command to assign x. But if the expression was used in a template property, there is no facility to execute commands, so this would not be possible.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_ev) | | |
| [◄ EscapeStringEncode](func_escapestringencode.htm) |  | [Execute ▶](func_execute.htm) |
