# CollectGarbage Command

Deletes temporary vectors. This command is only needed for scripts running endless or very long loops. SIMetrix creates temporary vectors when calculating vector expressions. These do not get deleted until control is returned to the command line. In the case of a script that calculates many expressions, it is possible for the memory used by the temporary vectors to become excessive. Calling CollectGarbage at regular intervals will resolve this problem.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_collectgarbage) | | |
| [◄ CloseTextEditor](com_closetexteditor.htm) |  | [CombineMenu ▶](com_combinemenu.htm) |
