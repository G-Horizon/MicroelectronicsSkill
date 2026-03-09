# DefButton Command

Defines the command executed when a button is pressed.

```
DefButton [/immediate] [/comgroup <command-group>] <button-name> <command> [<upCommand>] [/menu <menu-item-title>] [/features <features-required-for-menu-item>]
```

### Parameters

|  |  |
| --- | --- |
| /comgroup | This can be used with the function  [GetLastCommand](func_getlastcommand.htm) . GetLastCommand returns the text of the most recent command executed which specifed the supplied command group value. The command  [DefMenu](com_defmenu.htm)  also uses this feature. |
| /immediate | If specified, the command will be enabled for immediate execution. That is the command will be executed immediately even if another command - such as a simulation run - is currently in progress. This will only be accepted when the command specified is one of a small number of built-in command enabled for immediate execution. For the list of commands, see the command  [DefMenu](com_defmenu.htm) . You may not call a script if immediate execution is specified. |
| /menu | Flags whether this entry is a submenu of the button. |
| button-name | Name of button. Either a pre-defined button as listed in the command  [DefineToolBar](com_definetoolbar.htm)  or a new button created with  [CreateToolButton](com_createtoolbutton.htm) . |
| command | Command to be executed when the button is pressed. If `/immediate` is  *not*  specified this may be any valid command including a script. |
| up-command | Command to be executed when a toggle button is released. The button must be defined to have a toggle action using the `/toggle` switch for the command  [CreateToolButton](com_createtoolbutton.htm) . |

### See Also

* [GetToolButtons](func_gettoolbuttons.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_defbutton) | | |
| [◄ CurveEditCopy](com_curveeditcopy.htm) |  | [DefineToolBar ▶](com_definetoolbar.htm) |
