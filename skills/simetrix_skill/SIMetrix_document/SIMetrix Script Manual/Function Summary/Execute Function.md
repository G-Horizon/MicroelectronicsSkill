# Execute Function

Function calls the script defined in arg 1 and passes it the arguments supplied in arg 2- 8. The function's returned value is the script's first argument passed by reference. The Execute function is used internally to implement user functions that are registered with the RegisterUserFunction command. See  [User Defined Script Based Functions](applications_userdefinedscriptbasedfunctions.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Script name |
| 2 | any | No |  | Script argument 1 |
| 3 | any | No |  | ... Upto 8 args in total |

#### Argument 3

Script args 2-7

### Returns

Return type: Depends on called script

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_execute) | | |
| [◄ ev](func_ev.htm) |  | [ExistCommand ▶](func_existcommand.htm) |
