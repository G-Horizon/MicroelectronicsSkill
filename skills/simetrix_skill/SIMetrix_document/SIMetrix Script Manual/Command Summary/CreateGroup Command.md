# CreateGroup Command

Creates a data group. All vectors (or variables) are organised into groups. Each simulation run creates a new group and all data for that simulation is placed there. For more information, see  [Groups](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__groups) .

```
CreateGroup [/title <title>] <label>
```

### Parameters

|  |  |
| --- | --- |
| /title | Optional title. This will be displayed in the box displayed when selecting a Change Data Group... menu. It is also returned by a call to Groups('title') |
| label | Base name of group. The actual group name will be appended by a number to make it unique. The new group will become the current group. To find the name actually used, you can call the function  [Groups](func_groups.htm)  immediately after calling this command. The first element of Groups (i.e. `Groups())[0]` is always the current group. |

### See Also

* [DelGroup](com_delgroup.htm)
* [OpenGroup](com_opengroup.htm)
* [Groups](func_groups.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_creategroup) | | |
| [◄ CreateFont](com_createfont.htm) |  | [CreateRunningDialog ▶](com_createrunningdialog.htm) |
