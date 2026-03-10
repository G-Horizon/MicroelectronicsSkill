# OpenLinkedRun Command

Open a linked simulation run. Call this function prior to the  [Run](com_run.htm)  command in order to link them together. Linked runs create multi-division vectors in a single data group and are useful when sweeping some variable.

A linked run may be closed using  [CloseLinkedRun](com_closelinkedrun.htm) . It will also automatically close when control returns to the command line

### Parameters

|  |  |
| --- | --- |
| /labelprefix | Creates default label for each linked run. This is usually defined using /label with the  [Run](com_run.htm)  command, but if omitted will instead default to  *labelpref*  =  *runnumber*  where  *runnumber*  is a number starting at 1 and incrementing by 1 for each new run. Default is "Run" |

### See Also

* [CloseLinkedRun](com_closelinkedrun.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_openlinkedrun) | | |
| [◄ OpenGroup](com_opengroup.htm) |  | [OpenLogicDefinitionEditor ▶](com_openlogicdefinitioneditor.htm) |
