# DefMenu Command

Defines custom menu. Supersedes DefItem.

```
DefMenu [/immediate] [/shortcut] [/norepeat] [/id <command-id>] [/comgroup <command-group>] <menu-path> [ <command-string> [ <when-enabled> ]]
```

### Parameters

|  |  |
| --- | --- |
| /comgroup | This can be used with the function  [GetLastCommand](func_getlastcommand.htm) . GetLastCommand returns the text of the most recent command executed which specifed the supplied command group value. The command  [DefButton](com_defbutton.htm)  also uses this feature. |
| /forceUpdateCommand | If set, this will force any update that occurs to also update the command, even if the command is an empty string. |
| /forceUpdateExpression | If set, this will force any update that occurs to also update the expression, even if the expression is an empty string. |
| /id | This item is used by the edit menu GUI. It is not needed for regular use. |
| /immediate | Immediate mode. Command is executed immediately even if another operation - such as a simulation run or schematic editing operation - is currently in progress. For other options the command is not executed until the current operation is completed. Only a few commands can be assigned with this option. These are:   * [Abort](com_abort.htm) * [AbortSIMPLIS](com_abortsimplis.htm) * [Cancel](com_cancel.htm) * DefMenu * [DefKey](com_defkey.htm) * [Echo](com_echo.htm) * [Let](com_let.htm) * [Move](com_move.htm) * [Pan](com_pan.htm) * [Pause](com_pause.htm) * [Quit](com_quit.htm) * [RotInst](com_rotinst.htm) * [Select](com_select.htm) * [ScriptAbort](com_scriptabort.htm) * [ScriptPause](com_scriptpause.htm) * [ScriptResume](com_scriptresume.htm) * [Shell](com_shell.htm) * [Wire](com_wire.htm) * [Zoom](com_zoom.htm) |
| /noRepeat | Do not save menu action in "repeat last menu" buffer. This must be used for any menu that recalls a previously executed menu. |
| /pos | Position of menu. '1' means the top position. If omitted, the menu is placed at the bottom. Position must also take into account any link breaks within a menu. |
| /shortcut | Specify key or key combination to activate menu. Key description is placed on right hand side of menu item. For list of possible values see  [DefKey](com_defkey.htm)  , but note that key pad keys (e.g. NUM1, NUM\* etc.) cannot be assigned as menu shortcuts. Also note that DefKey has precedence in the event of the key or key combination being defined by both DefKey and DefMenu. |
| menuname | Composed of strings separated by pipe symbol: '|'. First name must be one of the following:  |  |  | | --- | --- | | AsciiFileEditor Schematic ASCII file text editor |  | | GraphMain Graph main menu |  | | LogicDefinitionEditor Logic definition file text editor |  | | NetlistEditor Netlist/Model file text editor |  | | ScriptEditor Script file text editor |  | | Shell Command shell menu |  | | SimetrixMain Schematic main menu - SIMetrix mode |  | | SimplisMain Schematic main menu - SIMPLIS mode |  | | SymbolMain Symbol editor fixed menu |  | | TextEditor Basic text editor |  | | VerilogAEditor Verilog-A file text editor |  | | VerilogHDLEditor Verilog-HDL file text editor |  | | WebView Web browser |  | | Graph Graph context menu |  | | Simetrix Schematic context menu SIMetrix mode |  | | Simplis Schematic context menu - SIMPLIS mode |  | | Symbol Symbol editor context menu |  |  The menuname for fixed menus must be followed by two or more names separated by '|' . The first is the menu name as it appears on the menu bar. The second can be the name of a menu item (which is actioned when selected) or a sub menu containing menu items or further sub menus. Sub menus can be nested to any level.  Use the '&' symbol to define an underlined ALT-key access letter.  The menuname for context menus must be followed by at least one name. Sub menus may also be defined for these.  To define a menu separator use the item text '-' Note that if any of the menu name contains spaces it must be enclosed in quotation marks.  Names defined using the CombineMenu command may also be used. The names SchemMain and Schem are defined in the standard startup script using  [CombineMenu](com_combinemenu.htm)  and provide compatibility with version 7.2 and earlier  See examples below. |
| when-enabled | A Boolean expression specifying under what circumstances the menu should be enabled. (The menu text turns grey when disabled). If omitted the menu will always be enabled. The expression may contain the following values:  |  |  | | --- | --- | | SchemOpen | TRUE when there is at least one schematic open. | | InstSelected | TRUE when at least one component is selected on the selected schematic | | Selected | TRUE when at least one component or at least one wire is selected on the current schematic | | PropertiesSelected | TRUE if schematic properties are selected | | ClipboardEmpty | TRUE if there is no schematic clipboard data available | | SimPaused | TRUE when the simulator has been paused. | | SimRunning | TRUE when the simulator is running. | | CircuitLoaded | TRUE when a circuit has been loaded to the simulator. (This happens when ever a simulation is run. A circuit can be unloaded with the Reset command). | | GraphOpen | TRUE when there is at least one graph window open. | | GraphCursorOn | TRUE when graph cursors are switched on | | GraphObjectSelected | TRUE if any graph annotation object, such as a legend box, is currently selected. | | CurvesSelected | TRUE if any curves are selected | | LiveMode | TRUE when a command has not completed. | | Never | Always FALSE i.e menu permanently disabled. |  These values can be combined with the operators:  |  |  | | --- | --- | | && | logical AND | | || | logical OR | | == | equals | | != | not equal | | ! | NOT |  Parentheses may also be used. Note that this expression is not related to vector expressions or the expressions that can be used in netlists or the command line.  Expressions enclosed in curly braces may also be used. Such expressions may contain any script expression to make customised menu enables. Care should be taken when using this feature and it should be used sparingly. Expressions can take a long time to evaluate and this will lead to sluggish menu activation response. |

### Notes

You can use DefMenu to redefine an existing menu. In this situation the position of the menu will not change but the command it executes and any shortcut key can be altered. Note that  *menuname*  is not case-sensitive, so if an existing menu exists the existing menu will be modified. This allows filenames to be used for menu names. Note that it isn't possible to add or remove a top level main menu definition while the window is open. For schematic, graph and symbol editor windows, this means that the definition of a new top level menu will not take effect until the windows are closed and reopened. For the command shell, top level main menu definitions can only be made in the startup script which runs before the command shell is visible. This restriction only applies to the top level menu, that is the menu name that is permanently visible in the menu bar. Menu items and sub menus under the top level menu can be added, removed and redefined at will.

### Example

The following are definitions for some of the standard menus. Definitions for all the standard menus can be found on the install CD in the Scripts folder. (A CD image may be downloaded from our web site if you do not have the physical CD). Change value schematic popup menu by calling the value script. (Note this must be entered on one line)

```
DefMenu "Schem|Change &Value" "value /ne" "InstSelected && !LiveMode"
```

Separator in schematic popup

```
DefMenu "Schem|-"
```

Graph popup to enable cursors

```
DefMenu "Graph|Cursors &On" "cursormode /ne on" "!LiveMode"
```

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_defmenu) | | |
| [◄ DefKey](com_defkey.htm) |  | [Del ▶](com_del.htm) |
