# Shell Command

Launches an application.

```
Shell [/wait] [/displayStdout] [/displayStderr] [/command] <command-string>
```

### Parameters

|  |  |
| --- | --- |
| /command | Calls system command processor to execute  *command-string* . This is necessary to run internal commands such as Copy and Move. The command processor is usually CMD.EXE. |
| /displayStderr |  |
| /displayStdout | Displays in the message window any standard output from the program. |
| /noConnectOutPipes |  |
| /wait | If specified, application is launched synchronously. This means that SIMetrix will not continue until the application has closed. |
| command-string | File system path to executable file. This would usually be a binary executable but may be any file that is defined as executable by the operating system. If a full path is not specified, a search will be made for the file using the rules described in the function  [Shell](func_shell.htm) . |

### Notes

Console mode applications will be launched without the console. To run a console mode application in a manner such that the console is displayed, use the command  [ShellOld](com_shellold.htm) .

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_shell) | | |
| [◄ SetUnits](com_setunits.htm) |  | [ShellOld ▶](com_shellold.htm) |
