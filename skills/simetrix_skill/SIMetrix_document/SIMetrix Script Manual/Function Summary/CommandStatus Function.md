# CommandStatus Function

Obtain information about the current script execution context

### Arguments

No arguments

### Returns

Return type: real array

Four element array. Elements described in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Drag and drop: 1 if current script was called as a result of a drag and drop operation, otherwise 0 |
| 1 | GUI Action: 1 if the current script was called by a GUI action such as a menu operation. 0, if called by a remote command. Refer to  [ProcessingGuiAction](func_processingguiaction.htm)  for a more detailed explanation |
| 2 | Processing accelerator: 1 if the current script was called by an accelerator key, otherwise 0 |
| 3 | Running startup command: 1 if current script was called by a startup command provide on the SIMetrix.exe command line |

### See Also

* [ProcessingAccelerator](func_processingaccelerator.htm)
* [ProcessingDragAndDrop](func_processingdraganddrop.htm)
* [ProcessingGuiAction](func_processingguiaction.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_commandstatus) | | |
| [◄ CollateVectors](func_collatevectors.htm) |  | [CompareSymbols ▶](func_comparesymbols.htm) |
