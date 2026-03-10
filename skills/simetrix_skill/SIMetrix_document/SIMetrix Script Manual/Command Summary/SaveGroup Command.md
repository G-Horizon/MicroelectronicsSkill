# SaveGroup Command

Saves the current group in binary format. Data groups can be opened with  [OpenGroup](com_opengroup.htm)

```
SaveGroup [/force] [/version version] [<filename>]
```

### Parameters

|  |  |
| --- | --- |
| /force | If is specified, any existing file will be overwritten. Otherwise the command will fail and display an error message |
| /version | Ignored. Retained for backward compatibility. |
| filename | Save to the  *filename* . Data can later be restored with the command  [OpenGroup](com_opengroup.htm) . If  *filename*  is not specified, a dialog box will be opened allowing the user to choose from available files. |

### See Also

* [CreateGroup](com_creategroup.htm)
* [DelGroup](com_delgroup.htm)
* [Groups](func_groups.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_savegroup) | | |
| [◄ SaveGraph](com_savegraph.htm) |  | [SaveRhs ▶](com_saverhs.htm) |
