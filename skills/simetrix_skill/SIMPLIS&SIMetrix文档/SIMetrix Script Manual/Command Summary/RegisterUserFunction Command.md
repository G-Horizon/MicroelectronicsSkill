# RegisterUserFunction Command

Creates a user defined function based on a script.

```
RegisterUserFunction <Function-Name> <Script-Name> [<min-number-args>] [<max-number-args>]
```

### Parameters

|  |  |
| --- | --- |
| Function-Name | Name of function. This must start with a letter and contain only letters, digits and underscores. The name must not be one of the built-in functions. |
| Script-Name | Name of script that will be called to execute function. |
| min-number-args | Minimum number of arguments required by the function. Range 0 - 7. Default=0 |
| max-number-args | Maximum number of arguments that may be supplied to the function. Range 0 - 7. Default=7 |

### Notes

When an expression is evaluated that calls the function defined by this command, the specified script will be called. The script receives the arguments to the function through its argument numbers 2-8. (There is a maximum limit of seven arguments). The function's returned value is the script's first argument passed by reference. Further details including an example are given in  [User Defined Script Based Functions](applications_userdefinedscriptbasedfunctions.htm) .

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_registeruserfunction) | | |
| [◄ RedrawGraph](com_redrawgraph.htm) |  | [RenameLibs ▶](com_renamelibs.htm) |
