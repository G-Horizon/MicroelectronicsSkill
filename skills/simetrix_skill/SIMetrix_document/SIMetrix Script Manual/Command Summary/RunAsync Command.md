# RunAsync Command

Spawns a new simulator process and runs specified netlist.

RunAsync has the benefit over  [Run](com_run.htm)  in that it is possible to carry on working in the front end normally while the simulation runs in the background. The disadvantage is that the asynchronous process cannot communicate with the front end. This means that incremental graph updates are not possible and the data for the simulation needs to be manually loaded after the simulation is complete.

To load the data use the  [OpenGroup](com_opengroup.htm)  command.

```
RunAsync <netlist> [<datafile>]
```

### Parameters

|  |  |
| --- | --- |
| netlist | Path to simulation netlist |
| datafile | Path to data file. If omitted, data will be saved to a temporary file in the temporary data directory. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_runasync) | | |
| [◄ Run](com_run.htm) |  | [RunCurrentScript ▶](com_runcurrentscript.htm) |
