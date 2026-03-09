# FileToString Function

Returns the entire contents of a file as a single string

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File name |
| 2 | string | No | 'auto' | Encoding |
| 3 | string | No | Function returns an empty vector on failure if this argiment is not supplied | Default output in the event of failure |

#### Argument 2

Character encoding assumed for input file. May be any value returned by the function  [GetCodecNames](func_getcodecnames.htm) . Examples include:

* 'utf-8' UTF8 encoding. This is the encoding used internally and for output
* 'utf-16' UTF16 also known as UCS-2
* 'Shift-JIS' Commonly used on Japanese systems

In addition the following special values may be used:

* 'locale' uses the default encoding for the system's locale
* 'auto' uses 'utf-8' if successful. Otherwise uses 'locale'

#### Argument 3

Default output in the event of failure

### Returns

Return type: String

String containing contents of file

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_filetostring) | | |
| [◄ Field](func_field.htm) |  | [FilterEditMenu ▶](func_filtereditmenu.htm) |
