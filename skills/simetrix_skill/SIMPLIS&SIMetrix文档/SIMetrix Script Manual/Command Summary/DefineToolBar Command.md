# DefineToolBar Command

Defines the buttons for a user defined toolbar created using the command  [CreateToolBar](com_createtoolbar.htm) . To define the buttons for a pre-defined toolbar, the associated option setting must be set using the command  [Set](com_set.htm) .

```
DefineToolBar <toolbar-name> <button-defs>
```

### Parameters

|  |  |
| --- | --- |
| /reserveundefined | Undefined buttons are stored and added to the toolbar automatically if defined at a later time |
| toolbar-name | Name of toolbar. This must be a toolbar created using  [CreateToolBar](com_createtoolbar.htm) . |
| button-defs | Semi-colon delimited list of button names to add to the toolbar. Buttons may either be one defined using  [CreateToolButton](com_createtoolbutton.htm)  or one of the pre-defined types shown in the table below. The '-' character may also be used to specify a spacer  For a list of buttons, see  [Pre-defined Buttons](applications_buttons.htm) .  The graphic images for all pre-defined buttons are built-in to the program, but the image files from which they were created can be found on the install CD. |

### See Also

* [DefButton](com_defbutton.htm)
* [GetToolButtons](func_gettoolbuttons.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_definetoolbar) | | |
| [◄ DefButton](com_defbutton.htm) |  | [DefKey ▶](com_defkey.htm) |
