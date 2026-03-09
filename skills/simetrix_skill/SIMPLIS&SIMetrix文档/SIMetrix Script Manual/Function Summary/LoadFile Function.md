# LoadFile Function

Returns an array of strings holding lines of text from the file specified by argument 1.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File name |
| 2 | string | No | 'auto' | Encoding |

#### Argument 2

Character encoding assumed for input file. May be any value returned by the function  [GetCodecNames](func_getcodecnames.htm) . Examples include:

* 'utf-8' UTF8 encoding. This is the encoding used internally and for output
* 'utf-16' UTF16 also known as UCS-2
* 'Shift-JIS' Commonly used on Japanese systems

In addition the following special values may be used:

* 'locale' uses the default encoding for the system's locale
* 'auto' uses 'utf-8' if successful. Otherwise uses 'locale'

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_loadfile) | | |
| [◄ ln](func_ln.htm) |  | [LoadSensitivityReport ▶](func_loadsensitivityreport.htm) |
