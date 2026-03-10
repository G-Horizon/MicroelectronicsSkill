# Parse Function

Splits up the string supplied as argument 1 into substrings or tokens. The characters specified in argument 2 are treated as separators of the substrings. For example, the following call to Parse():

```
Parse('c:\simetrix\work\amp.sch', '\')
```

returns:

```
'c:'
'simetrix'
'work'
'amp.sch'
```

If the second argument is omitted, spaces and tab characters will be treated as delimiters. If a space is include in the string of delimiters, tab characters will be automatically added.

If the third arguments is present and equal to 'quoted' the function will treat strings enclosed in double quotes as single indivisible tokens.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Input string |
| 2 | string | No | Space, tab, comma | Delimiters |
| 3 | string | No | <<empty>> | Options |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parse) | | |
| [◄ OptimiserWriteXMLString](func_optimiserwritexmlstring.htm) |  | [ParseAnalysis ▶](func_parseanalysis.htm) |
