# ScanEscape Function

Splits up the string supplied as argument 1 into substrings or tokens. The characters specified in argument 2 are treated as separators of the substrings. Separators preceded by a backslash (\) in the input string will be escaped and the string will not split on those separators. All escaped separators are replaced by the unescaped separators in the return string array.

For example, the following call to ScanEscape():

```
ScanEscape('A,List,of \, Delimited,,Items', ',')
```

returns:

```
A
List
of , Delimited

Items
```

Note the return value has the escaped comma separator "\," replaced with "," and the empty token between "Delimited" and "Items" is preserved.

The default separator is semi-colon, which is the same as the  [Scan](func_scan.htm)  function. User-defined, single character separators can be supplied as the second argument. Separators are case sensitive. Unlike the  [Scan](func_scan.htm)  function, the ScanEscape function can be provided with multiple delimiters.

To demonstrate the difference between the  [ParseEscape](func_parseescape.htm)  and ScanEscape functions, consider the same string parsed with the  [ParseEscape](func_parseescape.htm)  function:

```
ParseEscape('A,List,of \, Delimited,,Items', ',')
```

returns:

```
A
List
of , Delimited
Items
```

Note that the empty token between "Delimited" and "Items" is removed by the  [ParseEscape](func_parseescape.htm)  function.

Like  [Scan](func_scan.htm)  , the ScanEscape function can return a minimum length result by providing a integer as the third argument. For example, the following call to ScanEscape():

```
ScanEscape('A,List,of \, Delimited,,Items', ',', 7)
```

returns two empty strings, filling out indexes 5 and 6 in the return string array:

```
A
List
of , Delimited

Items
```

This can save testing the length of the return value to determine if an optional token was provided.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | String to scan |
| 2 | String | No | semi-colon | Delimiters |
| 3 | Real | No | 0 | Minimum number of return values |

#### Argument 1

String to scan

#### Argument 2

Delimiters. Semi-colon if omitted.

#### Argument 3

If present, forces the result to be a minimum size. For example, if the input string had two tokens but this argument was set to three, the result would be a string array of length 3 with the third element an empty string. In many applications, this can save testing the length of the return value to determine if an optional token was provided.

### Returns

Return type: string array

Returns tokens as an array of strings with the escaped delimiters replaced with unescaped delimiters. Empty fields are treated as a separate token.

### See Also

* [Parse](func_parse.htm)
* [Scan](func_scan.htm)
* [ParseEscape](func_parseescape.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_scanescape) | | |
| [◄ Scan](func_scan.htm) |  | [ScriptName ▶](func_scriptname.htm) |
