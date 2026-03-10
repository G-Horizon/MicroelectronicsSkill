# ScriptPause Command

Pauses a script. Execution can later be resumed with  [ScriptResume](com_scriptresume.htm)  or single stepped with ScriptStep. Note that this command is often executed from a key or menu item which has been defined with the direct execution option specified (option flag 5 or `/immediate` for  [DefMenu](com_defmenu.htm)  ). ScriptPause is assigned to shift-F2 by default. Note that it is not possible to use the normal user interface while a script is paused. The main use of script pause is to allow single-stepping for debug purposes.

Scripts can be single stepped by executing ScriptPause immediately before starting the script. If the EchoOn option is also enabled, each line of the script as it is executed will be displayed in the message window. See  [Debugging Scripts](scriptlanguage_executingscripts.htm#scriptlanguage_executingscripts__debuggingscripts) .

### See Also

* [ScriptStep](com_scriptstep.htm)
* [ScriptResume](com_scriptresume.htm)
* [ScriptAbort](com_scriptabort.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_scriptpause) | | |
| [◄ ScriptAbort](com_scriptabort.htm) |  | [ScriptResume ▶](com_scriptresume.htm) |
