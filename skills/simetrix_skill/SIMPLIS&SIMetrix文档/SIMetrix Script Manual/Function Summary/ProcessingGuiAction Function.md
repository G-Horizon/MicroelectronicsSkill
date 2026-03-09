# ProcessingGuiAction Function

Detects if the current script was called by a GUI action. Most scripts are called from a GUI action such as a menu or key press. Typing in the name of the scripts at the command line is also classed as a GUI action. This function will return 1 for such calls.

Scripts can also be called remotely using the /s switch on the SIMetrix.exe command line and also using the SxCommand utility. Such calls are classed as non-GUI. This function will return 0 for such calls.

### Arguments

No arguments

### Returns

Return type: real

1 if the current script was called by a GUI action, otherwise 0

### See Also

* [ProcessingAccelerator](func_processingaccelerator.htm)
* [ProcessingDragAndDrop](func_processingdraganddrop.htm)
* [CommandStatus](func_commandstatus.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_processingguiaction) | | |
| [◄ ProcessingDragAndDrop](func_processingdraganddrop.htm) |  | [Progress ▶](func_progress.htm) |
