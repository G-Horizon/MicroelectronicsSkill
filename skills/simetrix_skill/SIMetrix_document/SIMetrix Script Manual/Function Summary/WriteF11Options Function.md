# WriteF11Options Function

Write SIMetrix simulator options to the F11 window.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Option values |

#### Argument 1

Array of semi-colon delimited string in form:

name;value;type

|  |  |
| --- | --- |
| name | Name of option |
| value | Value of option |
| type | Type. One of 'BOOL', 'INT', 'REAL' or 'STRING' |

The given type determines how the value is interpreted. REAL values can use engineering suffixes, e.g. 1k will be interprted as 1000. BOOL options can have values of 'true' or '1' to indicate a true condition. All other values will be treated as false. STRING values will entered literally.

Unlike  [ReadF11Options](func_readf11options.htm)  , this function does not check that the option names entered are valid.

### Returns

### See Also

* [ReadF11Options](func_readf11options.htm)
* [WriteF11Lines](func_writef11lines.htm)
* [GetF11Lines](func_getf11lines.htm)
* [AppendTextWindow](com_appendtextwindow.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writef11options) | | |
| [◄ WriteF11Lines](func_writef11lines.htm) |  | [WriteIniKey ▶](func_writeinikey.htm) |
