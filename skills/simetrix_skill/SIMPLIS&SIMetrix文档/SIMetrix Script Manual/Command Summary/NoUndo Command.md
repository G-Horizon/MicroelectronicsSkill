# NoUndo Command

Inhibits saving to undo buffer until command returns to the command line. This allows multiple operation to be treated as one for the purposes of the Undo feature. For example, suppose you have a script that edits a number of schematic instances. Normally, if you run the script then select Undo, only the most recent change will be undone. The user would need to select Undo many times to return the circuit to the state before the script was run. If NoUndo is called at the start of the script, Undo will return the schematic to the start state in a single operation.

### Parameters

|  |  |
| --- | --- |
| /nocapture | Normally NoUndo, saves the current state so that the next undo operation will restore the state to immediately before NoUndo was called. The /nocapture switch inhibits this. |
| /release | Restores undo buffer save operations. This happens automatically when control returns to the command line. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_noundo) | | |
| [◄ NoPaint](com_nopaint.htm) |  | [OpenAsciiFile ▶](com_openasciifile.htm) |
