# SaveRhs Command

Creates a file containing every node voltage, inductor current and voltage source current calculated at the most recent analysis point. The values generated can be read back in as nodesets to initialise the dc operating point solution. There are a number of applications for this command - see notes below.

```
SaveRhs [/nodeset] <filename>
```

### Parameters

|  |  |
| --- | --- |
| /nodeset | If specified the values are output in the form of a .nodeset command which can be read back in directly. Only node voltages are output if this switch is specified. Otherwise, currents in voltage sources and inductors are also output. |
| filename | File where output is written. |

### Notes

This command is intended as an aid to DC operating point convergence. Sometimes the dc operating point solution is known from a previous run but took a long time to calculate. By applying the known solution voltages as nodesets prior to the operating point solution, the new DC bias point will be found much more rapidly. The method is tolerant of minor changes to the circuit. The old solution may not be exact, but if it is close this may be sufficient for the new solution to be found quickly. If SaveRhs is executed after an AC analysis, the values output will be the real part only.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_saverhs) | | |
| [◄ SaveGroup](com_savegroup.htm) |  | [SaveSnapShot ▶](com_savesnapshot.htm) |
