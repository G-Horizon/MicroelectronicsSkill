# AppendGroup Command

Appends a data group with another group. Appending a group joins vectors with the same name and type in both groups to add a new division. (Refer to  [Multi-division Vectors](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__multidivisionvectors)  )

This is used for Multi-core multi-step SIMPLIS simulations. Each SIMPLIS process runs independently creating its own data file. When the processes have completed their simulations, the data files are loaded to create groups which are then appended using this command. The end result is a multi-division vector which looks the same as if it were created by a conventional single-core run.

```
AppendGroup <group> <appending-group>
```

### See Also

* [CreateGroup](com_creategroup.htm)
* [DelGroup](com_delgroup.htm)
* [OpenGroup](com_opengroup.htm)
* [Groups](func_groups.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_appendgroup) | | |
| [◄ Anno](com_anno.htm) |  | [AppendTextWindow ▶](com_appendtextwindow.htm) |
