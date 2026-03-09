# ReadF11Options Function

Read .OPTIONS line in the F11 window

### Arguments

No arguments

### Returns

Return type: string array

Array of semi-colon delimited strings providing details of any SIMetrix .OPTIONS statements located in the current schematic's F11 window. Each token in the string is defined in the following table:

|  |  |
| --- | --- |
| **Field** | **Description** |
| 0 | Option name |
| 1 | Value |
| 2 | Type - on eof 'BOOL', 'REAL', 'INT', 'STRING' or 'UNKNOWN' |

The function will not return option settings that are not recognised by the simulator. It will also not return option settings that are set to their default value.

### See Also

* [WriteF11Options](func_writef11options.htm)
* [WriteF11Lines](func_writef11lines.htm)
* [GetF11Lines](func_getf11lines.htm)
* [AppendTextWindow](com_appendtextwindow.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readf11options) | | |
| [◄ ReadF11Analyses](func_readf11analyses.htm) |  | [ReadFile ▶](func_readfile.htm) |
