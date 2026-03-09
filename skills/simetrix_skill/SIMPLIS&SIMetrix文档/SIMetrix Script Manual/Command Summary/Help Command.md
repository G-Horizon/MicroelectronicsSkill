# Help Command

Opens the SIMetrix help system.

```
Help [/file <filename>] /contents | /context <context-id> | <topic>
```

### Parameters

|  |  |
| --- | --- |
| /contents | Opens help in main contents page |
| /context | Included only for backward compatibility. 'Help /context id' does the same as 'Help id' |
| /file | If specified, help will be obtained from  *filename* . Otherwise help file will be SIMetrix.chm |
| topic | If specified, help system will display page relating to  *topic* . If  *topic*  does not exist, a list of available topics will be displayed. |

### Example

To display help on the .TRAN simulator directive type:

```
Help .tran
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_help) | | |
| [◄ GroupSelected](com_groupselected.htm) |  | [HideCurve ▶](com_hidecurve.htm) |
