# Shell Function

Runs an external program and returns its exit code.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path to executable file |
| 2 | string | No |  | Options |
| 3 | string | No | stdout and stderr output directed to message window | File to receive redirected output |

#### Argument 1

File system path to executable file. This would usually be a binary executable but may be any file that is defined as executable by the operating system.

1. The directory where the SIMetrix binary is located
2. The current directory
3. *windows*  \ SYSTEM32.  *windows*  is the location of the Windows directory.
4. *windows*  \ SYSTEM
5. The windows directory
6. The directories listed in the PATH environment variable

;

#### Argument 2

String array containing one or more of the options defined in the following table:

|  |  |
| --- | --- |
| 'wait' | If specified, the function will not return until the called process has exited. |
| 'command' | Calls OS command line interpreter to execute the command supplied. This can be used to execute system commands such as 'copy' and 'move'. |
| 'stdout' | Stdout from the process is displayed in the command shell message window. Requires either 'wait' or file redirection see argument 3 |
| 'stderr' | Stderr from the process is displayed in the command shell message window. Requires either 'wait' or file redirection see argument 3 |
| 'console' | Opens a console window to execute the process. Disables stdout and stderr |

#### Argument 3

If stdout or/and stderr are specified, the output can be optionally directed to a file. Use this argument to specify the file to receive the output

### Returns

Return type: real array

Returns a real array of length 3 as defined below:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Process exit code. If the process is still running when this function returns, this value will be 0. |
| 1 | Error code as follows: |  |  | | --- | --- | | 0 | Process launched successfully | | 1 | Command processor not found. (  *command*  options specified) | | 2 | Cannot find file | | 3 | File is not executable | | 4 | Access denied | | 5 | Process launch failed | | 6 | Unknown failure | |
| 2 | PID of process. This will be -1 if the process is no longer running |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_shell) | | |
| [◄ SetUnion](func_setunion.htm) |  | [ShellExecute ▶](func_shellexecute.htm) |
