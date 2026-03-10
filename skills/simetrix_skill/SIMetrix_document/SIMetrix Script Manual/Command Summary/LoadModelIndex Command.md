# LoadModelIndex Command

Forces model library indexes to be re-checked and loaded. Model library indexes are binary files that allow the rapid location of simulation models. When SIMetrix starts, it checks that the indexes are up to date by comparing file dates. If any files have been changed, the appropriate index file will be rebuilt. When this process is complete, the indexes are read in to memory for fast access.

This command forces SIMetrix to repeat the above procedure. This may be necessary if additional files are added to a directory where models reside while SIMetrix is running. SIMetrix can usually detect this automatically if the drive is local but cannot always do so for network drives.

Note the menu **Model Library** > **Rebuild Catalog** calls this command.

The work of reloading indexes is actually performed by the simulator in the background so this command returns immediately even though the process can take several seconds. If you start a simulation immediately after executing this command, there will be a pause until the reload is complete.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_loadmodelindex) | | |
| [◄ ListOptions](com_listoptions.htm) |  | [LoadSimulatorStyleSheet ▶](com_loadsimulatorstylesheet.htm) |
