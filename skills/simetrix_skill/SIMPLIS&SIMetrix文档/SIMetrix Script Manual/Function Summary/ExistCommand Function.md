# ExistCommand Function

Test if a script command is a valid command.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Command name |

### Returns

Return type: real

Returns 1.0 if the command is available otherwise 0.0

### Notes

There are two situations where a documented command may not be available:

* The command is not implemented in the currently executing version of the application.
* The command is not enabled with the current license. A few commands are 'licensed' and are not available with all products.

### See Also

* [ExistFunction](func_existfunction.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_existcommand) | | |
| [◄ Execute](func_execute.htm) |  | [ExistDir ▶](func_existdir.htm) |
