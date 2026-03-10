# GetLastCommand Function

Retrieve last command issued by a menu or toolbar with a specified command group definition. This is used for operations such as "repeat last place".

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Command group |

#### Argument 1

Name of a command group. These are arbitrary strings that may be supplied to a  [DefMenu](com_defmenu.htm)  or  [DefButton](com_defbutton.htm)  command using the `/comgroup` switch.

### Returns

Return type: string

If a menu or button defined with a `/comgroup` specification is executed, the command executed is stored. This function retrieves the most recent with the specified comgroup value.

### Notes

Menus and buttons used for placing components on a schematic are defined using the comgroup value 'place'. So `GetLastCommand('place')` always returns the command used for the most recent place operation.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlastcommand) | | |
| [◄ GetLaplaceErrorMessage](func_getlaplaceerrormessage.htm) |  | [GetLastError ▶](func_getlasterror.htm) |
