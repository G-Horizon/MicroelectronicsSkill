# GetFontSpec Function

Returns the current font specification for the object whose name is passed to argument 1. Valid object names can be obtained from the GetFonts function (page 163). The return value may be used to initialise the SelectFontDialog (page 286) which allows the user to define a new font.

The return value represents the font of the object as a string consisting of a number of values separated by semi-colons. The values define the font in terms of its type face, size, style and other characteristics. However, these values should not be used directly as the format of the string may change in future versions of the product. The return value should be used only as an argument to functions or commands that accept a font definition. E.g. The  [SelectFontDialog](func_selectfontdialog.htm)  function and  [EditFont](com_editfont.htm)  command.

If the object name passed is not recognised the function will return the definition for the default font.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Object name |

### Returns

Return type: string

string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfontspec) | | |
| [◄ GetFonts](func_getfonts.htm) |  | [GetFreeDiskSpace ▶](func_getfreediskspace.htm) |
