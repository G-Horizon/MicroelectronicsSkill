# ReadFile Function

Returns an array of strings holding lines of text from the file specified by argument 1.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File name |
| 2 | string | Yes | 'utf8' | Encoding option |

#### Argument 2

Can be 'mbcs' or 'utf8'. If 'utf8' the file is assumed to be encoded using UTF8. If 'mbcs' encoding uses the system default

### Returns

Return type: string array

### See Also

* [LoadFile](func_loadfile.htm)  Perfoms a similar operation but with more encoding options including the ability to auto-detect UTF8

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readfile) | | |
| [◄ ReadF11Options](func_readf11options.htm) |  | [ReadIniKey ▶](func_readinikey.htm) |
