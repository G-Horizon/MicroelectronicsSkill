# RunCurrentScript Command

Runs the script currently open in the text editor. The script must have been opened using the  [OpenScript](com_openscript.htm)  command, created with the  [NewScript](com_newscript.htm)  command or recovered from a restore session operation. The script will be run as it is displayed in the editor including any unsaved edits.

### Notes

When a script is run using this command it will be referred to by the path of the file in the editor if there is one. If there isn't (i.e. the editor has never been saved, the script will be referred to as '<LocalScript>' in any error messages. This will also be the return value from the  [ScriptName](func_scriptname.htm)  function.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_runcurrentscript) | | |
| [◄ RunAsync](com_runasync.htm) |  | [RunSIMPLIS ▶](com_runsimplis.htm) |
