# ShellOld Command

Launches an application. This behaves identically to the Shell command implemented on version 4.5 and earlier.

```
ShellOld [/wait] [/hide] [/icon] [/command] <command-name>
```

### Parameters

|  |  |
| --- | --- |
| /command | Calls system command processor to execute  *command-string* . This is necessary to run internal commands such as Copy and Move. The command processor is usually CMD.EXE |
| /console |  |
| /hide | Start the program with the main window initially hidden. |
| /icon | Start the program in a minimised state. |
| /wait | If specified, application is launched synchronously. This means that SIMetrix will not continue until the application has closed. |
| command-name | File system path to executable file. This would usually be a binary executable but may be any file that is defined as executable by the operating system. If a full path is not specified, a search will be made for the file using the rules described in  [Shell](func_shell.htm) . |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_shellold) | | |
| [◄ Shell](com_shell.htm) |  | [Show ▶](com_show.htm) |
