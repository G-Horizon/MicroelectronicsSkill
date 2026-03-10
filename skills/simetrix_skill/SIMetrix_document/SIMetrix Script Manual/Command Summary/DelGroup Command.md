# DelGroup Command

Deletes specified groups. See  [Groups](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__groups)  for more information.

```
DelGroup [/cleanUp] [/noDelete] /all | <Group-Name> [Group-Name] ...
```

### Parameters

|  |  |
| --- | --- |
| /all | If specified all groups except the user group are destroyed. |
| /cleanUp | Inhibits delete of associated temporary data file. This file will only be deleted any way if the option variable DataGroupDelete is set to OnDelete. |
| /noDelete | Specify this switch if the associated data file is going to be reused as it may speed up the read operation especially if the data was created by a simulation that was paused. If the file will be deleted then this switch has no benefit but will do no harm other than to slow the execution of this command a little. |

### See Also

* [CreateGroup](com_creategroup.htm)
* [OpenGroup](com_opengroup.htm)
* [Groups](func_groups.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_delgroup) | | |
| [◄ DeleteToolBar](com_deletetoolbar.htm) |  | [DelLegendProp ▶](com_dellegendprop.htm) |
