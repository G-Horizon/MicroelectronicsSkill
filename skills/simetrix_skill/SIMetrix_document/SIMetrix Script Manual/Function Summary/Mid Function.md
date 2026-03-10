# Mid Function

Returns a string constructed from a sub string of argument 1. First character is at index specified by argument 2 while argument 3 is the length of the result. The first character is at index 0.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String |
| 2 | real | Yes |  | Start index |
| 3 | real | No | to end of string | Length of result |

### Returns

Return type: string

### See Also

* [Char](func_char.htm)

### Example

```
Mid('Hello World!', 6, 5)
```

will return 'World'.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_mid) | | |
| [◄ MessageBox](func_messagebox.htm) |  | [min ▶](func_min.htm) |
