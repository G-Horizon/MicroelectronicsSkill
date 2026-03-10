# GetMenuItems Function

Returns all menu item names in the specified menu.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Menu path |
| 2 | string | No |  | Options |

#### Argument 1

Specifies the path for the menu as it would be provided to the command  [DefMenu](com_defmenu.htm)  but without the menu item name. For example, the command to define the command shell's New Schematic menu is similar to:

```
DefMenu "Shell|&File|&New Schematic" "NewSchem /ne"
```

`Shell|&File` is the menu path and this what the GetMenuItems function expects.

#### Argument 2

Can be set to 'recurse'. This instructs the function to recurse into sub-menus and list all menu definitions. The definitions are given as semi-colon delimited strings providing the menu accelerator (if present), a unique ID and the full path of the menu.

### Returns

Return type: string array

Returns a string array listing all the menu item names.

### Example

```
GetMenuItems('Shell|&File')
```

returns all the menu items in the command shell's File menu.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getmenuitems) | | |
| [◄ GetMD5String](func_getmd5string.htm) |  | [GetModelFiles ▶](func_getmodelfiles.htm) |
