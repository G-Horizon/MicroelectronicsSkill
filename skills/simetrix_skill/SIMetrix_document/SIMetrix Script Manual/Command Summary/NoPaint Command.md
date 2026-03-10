# NoPaint Command

This command has no effect unless executed from within a script. It inhibits all updates to graphs until script execution is complete. This is useful when a number of operations are performed on a graph. By calling this command at the start of a script, multiple graph operations can be performed much faster and more smoothly.

Use the /stack switch to restore painting when the current script completes. Without this the NoPaint state will not be automatically cleared until complete control returns to the command line. This means that if a graph operation using NoPaint is executed while running a simulation, the paint operation may not actually be seen until the simulation is complete or paused.

### Parameters

|  |  |
| --- | --- |
| /reenable | Flag to indicate whether to re-enable painting or not. Default is false. |
| /stack | Instructs to restore NoPaint state to the starting state (either on or off) when current script completes. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_nopaint) | | |
| [◄ NewVerilogHDL](com_newveriloghdl.htm) |  | [NoUndo ▶](com_noundo.htm) |
