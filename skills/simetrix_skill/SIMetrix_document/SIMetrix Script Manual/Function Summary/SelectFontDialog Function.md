# SelectFontDialog Function

Opens a dialog box allowing the user to define a font. The box is initialised with the font specification supplied as an argument. The function returns the new font specification.

A second argument may be specified to identify the name of the object whose font is being edited. This is so that its font may be updated if the user presses the  *Apply*  button in the dialog box.

If the user cancels the box, the function returns an empty vector.

Font specifcations are strings that provide information about the type face, size, style and other font characteristics. Font specifications should only be used with functions and commands that are designed to accept them. The format of the font spec may change in future versions.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Default font | Initial font specification |
| 2 | string | No |  | Name of object being edited |

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectfontdialog) | | |
| [◄ SelectedWires](func_selectedwires.htm) |  | [SelectRows ▶](func_selectrows.htm) |
