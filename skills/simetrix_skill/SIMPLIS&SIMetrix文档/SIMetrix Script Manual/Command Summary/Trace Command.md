# Trace Command

The trace command is used to set up a simulation trace while a simulation is running. To set up a trace before a simulation is started, use the .TRACE or .GRAPH simulator controls.

```
Trace signal-name trace-id
```

### Parameters

|  |  |
| --- | --- |
| signal-name | Net name or pin name for voltage or current to be traced. |
| trave-id | Integer value used to group traces together on the same graph. All traces with the same  *trace-id*  will go to the same graph. |

### Notes

Traces set up with this command only remain in effect until the end of the simulation. A Trace command executed before a simulation starts will have no effect.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_trace) | | |
| [◄ TitleSchem](com_titleschem.htm) |  | [Undo ▶](com_undo.htm) |
