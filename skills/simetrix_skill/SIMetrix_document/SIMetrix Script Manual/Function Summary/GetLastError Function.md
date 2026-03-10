# GetLastError Function

Returns a string with one of three values signifying the status of the most recent command executed.

The command switches /noerr and /quiet (see  [Command Switches](scriptlanguage_statementscommands.htm#scriptlanguage_statementscommands__commandswitches)  ) can be used to effectively disable non-fatal errors. This function allows customised action in the event of an error occurring. For example, if a simulation fails to converge, the run command yields an error. This function can be used to take appropriate action in these circumstances.

When a fatal error occurs, the command will abort unconditionally and this function returns 'Fatal'.

### Arguments

No arguments

### Returns

Return type: string

Returns a string with one of three values signifying the status of the most recent command executed. The three values are:

|  |  |
| --- | --- |
| 'OK' | Command executed without error |
| 'Error' | One or more errors occurred in the most recent command |
| 'Fatal' | The most recent command was not recognised or the evaluation of a braced substitution failed. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlasterror) | | |
| [◄ GetLastCommand](func_getlastcommand.htm) |  | [GetLastGraphObjectAdded ▶](func_getlastgraphobjectadded.htm) |
