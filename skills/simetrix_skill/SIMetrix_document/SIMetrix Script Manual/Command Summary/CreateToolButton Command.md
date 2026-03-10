# CreateToolButton Command

Creates or redefines a tool bar button. This command creates the properties of the button but not the command it executes when it is pressed. To define the command, use  [DefButton](com_defbutton.htm) .

```
CreateToolButton [/toggle] [/shortcut key] [/class class-name] <name> [<graphic> [<hint>]]
```

### Parameters

|  |  |
| --- | --- |
| /class | This is used with the function  [GetToolButtons](func_gettoolbuttons.htm)  to select buttons according to their function. Set this value to 'component' if you wish the button to be displayed in the GUI which selects component button. |
| /shortcut | Specifies a shortcut key that will perform the same action as the tool button. For key codes see  [DefKey](com_defkey.htm) . |
| /toggle | If specified, the button will have a toggle action and will have two commands associated with it. One command will be executed when the button is pressed and another when it is released. The 'Wire' pre-defined button is defined in this manner. |
| name | Name of button. This may be one of the pre-defined types described in  [DefineToolBar](com_definetoolbar.htm)  in which case this command will redefine its properties. You may also specify a new name to create a completely new button. |
| graphic | Graphical image to be displayed on the button. This may be one of the pre-defined images listed in  [DefineToolBar](com_definetoolbar.htm)  or you may use a user defined image specified in a file. The file must be located at simetrix-root/support/images.  where simetrix-root is the top level directory in the SIMetrix tree.  The file may use windows bitmap (.bmp), portable network graphic (.png) or JPEG (.jpg) formats. The PNG format supports masks and this format must be used if transparent areas are needed in the graphic. |
| hint | Text that describes the operation of the button. This will be displayed when the user passes the mouse cursor over the button. |

### See Also

* [CreateToolBar](com_createtoolbar.htm)
* [GetToolButtons](func_gettoolbuttons.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_createtoolbutton) | | |
| [◄ CreateToolBar](com_createtoolbar.htm) |  | [CursorMode ▶](com_cursormode.htm) |
