# FilterFile Function

\*\*\* UNSUPPORTED \*\*\* See [Unsupported Functions and Commands](scriptlanguage_unsupportedfunctionscommands.htm) for more information.

Processes a file specified by arg 1 and returns a string array containing any lines in the file that start with any of the keywords specified by arg 2. If arg 3 = 'strip', the lines will be returned with the keyword removed.

If arg3='spice', the input file will be filtered to remove inline comments and join lines connected using the '+' continuation character. Note that with arg3='spice' normal '\*' comments pass through unmodified as long as they are not embedded between '+' continuation lines.

This function was developed for internal testing and was used to extract control lines from netlists. It may have other uses.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | file name |
| 2 | string array | Yes |  | keywords |
| 3 | string | No |  | option |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_filterfile) | | |
| [◄ FilterEditMenu](func_filtereditmenu.htm) |  | [FilterNested ▶](func_filternested.htm) |
