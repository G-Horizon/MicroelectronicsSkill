# DefKey Command

DefKey is used to define custom key strokes.

```
DefKey <key-label> [<command-string> [<options>]]
```

### Parameters

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| key-label | Code to signify key to define. See table below for list of possible labels. All labels may be suffixed with one of the following:  |  |  | | --- | --- | | :SCHEM | Key defined only when a schematic window is currently active | | :GRAPH | Key defined only when a graph window is currently active | | :SHELL | Key defined only when the command shell is currently active. | | :SYMBOL | Key defined only when a symbol editor window is currently active |  If no suffix is provided the key definition will be active in all windows. Valid key labels are:  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | F1 | F2 | F3 | F4 | F5 | F6 | | F7 | F8 | F9 | F10 | F11 | F12 | | INS | DEL | HOME | END | PGUP | PGDN | | LEFT | RIGHT | UP | DOWN | TAB | BACK | | ESC | NUM1 | NUM2 | NUM4 | NUM5 | NUM6 | | NUM7 | NUM8 | NUM9 | NUM0 | NUM\* | NUM/ | | NUM+ | NUM- | NUM. |  |  |  |  Additionally, all letter and number keys, referred to by letter/number alone. The space bar can be used (\_SPACE), but must always be shifted.  Shifted keys are keys that have shift, control or alt also pressed at the same time. Any of the above keys can be prefixed with any combination of 'S' for shift, 'C' for control or 'A' for alt. Note that in windows, the right hand ALT key performs the same action as CONTROL-ALT. |
| command-string | A command line command or commands to be executed when the specified key is pressed. Multiple commands must be separated by semi-colons (';'). Unless the command string has no spaces, it must wholly enclosed in double quotation marks ("). |
| option-flag | A number between 0 and 5 to specify the manner in which the command is executed. These are as follows:  |  |  | | --- | --- | | 0, 4 | Default. Command is echoed and executed. Any text already in command line is overwritten. | | 5 | Immediate mode. Command is executed immediately even if another operation - such as a simulation run or schematic editing operation - is currently in progress. For other options the command is not executed until the current operation is completed. Only a few commands can be assigned with this option. |  The following commands can be used with the flag set to immediate mode:   * [Cancel](com_cancel.htm) * [DefMenu](com_defmenu.htm) * DefKey * [Echo](com_echo.htm) * [Let](com_let.htm) * [Move](com_move.htm) * [Pan](com_pan.htm) * [Pause](com_pause.htm) * [Quit](com_quit.htm) * [RotInst](com_rotinst.htm) * [Select](com_select.htm) * [ScriptAbort](com_scriptabort.htm) * [ScriptPause](com_scriptpause.htm) * [ScriptResume](com_scriptresume.htm) * [Shell](com_shell.htm) * [Wire](com_wire.htm) * [Zoom](com_zoom.htm)   Note, the command  [Let](com_let.htm)  can be used to set a global variable which can then be tested in running script. This is a convenient method of providing user control of script execution. |

### Notes

Unshifted letter and number key definitions will not function when a text edit window such as the simulator command window (F11) is active. Space bar definitions must always be shifted. The same codes can be used for menu short cuts. See  [DefMenu](com_defmenu.htm) . Key definition will be lost when SIMetrix exits. To make a key or menu definition permanent you can place the command to define it in the startup script. To do this, select command shell menu **File** > **Options** > **Edit Startup Script** and add the line above.

### Example

To define control-R to place a resistor on the schematic sheet, enter the command:

```
DefKey CR "inst res" 4
```

The built in definition for F12 to zoom out a schematic is

```
DefKey F12:SCHEM "zoom out" 4
```

This definition only functions when a schematic is active. A similar definition for F12:GRAPH zooms out a graph when a graph window is active.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_defkey) | | |
| [◄ DefineToolBar](com_definetoolbar.htm) |  | [DefMenu ▶](com_defmenu.htm) |
