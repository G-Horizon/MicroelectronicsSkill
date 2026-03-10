# GetToolButtons Function

Returns name and description for available tool buttons.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | All | Button class |

#### Argument 1

Class name of buttons. With no user defined buttons, this can be empty or 'component'. If 'component' only buttons intended for placing schematic symbols will be returned. Otherwise all buttons available will be returned.

If user defined buttons have been created using the  [CreateToolButton](com_createtoolbutton.htm)  command, this argument may be set to any value used for the /class switch in which case only buttons defined with that /class switch value will be returned.

### Returns

String array of button specifications. Each entry contains two values separated by a semi-colon. The first value is the name of the button as can be used to add buttons to a toolbar using the command  [DefineToolBar](com_definetoolbar.htm) . The second value is a description of the button.

### See Also

* [CreateToolBar](com_createtoolbar.htm)
* [DefButton](com_defbutton.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gettoolbuttons) | | |
| [◄ GetToolBarDefinition](func_gettoolbardefinition.htm) |  | [GetTouchstoneErrors ▶](func_gettouchstoneerrors.htm) |
