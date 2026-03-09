# WriteF11Lines Function

Writes lines directly to the F11 window overwriting any existing lines.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Lines |

#### Argument 1

Lines to write in the form of a string array. Each element in the array creates a new line.

### Returns

Return type: real

Returns 1.0 if the function is successful otherwise returns 0.0. The function will only fail if there are no schematics open.

### See Also

* [ReadF11Options](func_readf11options.htm)
* [WriteF11Options](func_writef11options.htm)
* [GetF11Lines](func_getf11lines.htm)
* [AppendTextWindow](com_appendtextwindow.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writef11lines) | | |
| [◄ WriteConfigSetting](func_writeconfigsetting.htm) |  | [WriteF11Options ▶](func_writef11options.htm) |
