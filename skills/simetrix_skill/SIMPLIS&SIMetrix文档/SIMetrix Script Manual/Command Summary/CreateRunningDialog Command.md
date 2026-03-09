# CreateRunningDialog Command

Creates a dialog for displaying progress whilst a script is running.

### Parameters

|  |  |
| --- | --- |
| /abortcommand | Command to be executed when Abort accepted. Typically this would be a command to assign a global variable which the running script would test. For example, 'Let global:abortScript=1'. The script would test this value at appropriate times then exit cleanly. If this switch is omitted, the script will execute the  [ScriptAbort](com_scriptabort.htm)  command which will abort the execution of the script immediately. |
| /abortmessage | Message shown when pressing abort |
| /caption | Title bar caption. |
| /displaymessage | The message displayed inside the dialog |
| /status | Initial status message. |
| /steps | The number of progress steps that will occur. If 0 or not set, no progress bar will be shown. |

### See Also

* [UpdateRunningDialog](com_updaterunningdialog.htm)
* [DestroyRunningDialog](com_destroyrunningdialog.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_createrunningdialog) | | |
| [◄ CreateGroup](com_creategroup.htm) |  | [CreateSym ▶](com_createsym.htm) |
