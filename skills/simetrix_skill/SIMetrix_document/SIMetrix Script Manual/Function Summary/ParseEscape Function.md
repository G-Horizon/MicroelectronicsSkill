# ParseEscape Function

Splits up the string supplied as argument 1 into substrings or tokens. The characters specified in argument 2 are treated as separators of the substrings. Separators preceded by a backslash (\) in the input string will be escaped and the string will not split on those separators. All escaped separators are replaced by the unescaped separators in the return string array.

For example, the following call to ParseEscape():

```
ParseEscape('A,List,of \, Delimited Items', ',')
```

returns:

```
A
List
of , Delimited Items
```

Note the return value has the escaped comma separator "\," replaced with ","

The default separators are space, comma and tab. User-defined, single character separators can be supplied as the second argument. Separators are case sensitive.

The same string parsed with the default separators of space, comma and tab:

```
ParseEscape('A,List,of \, Delimited Items')
```

returns:

```
A
List
of
,
Delimited
Items
```

This function doesn't return empty strings when two delimiters are found in adjacent positions in the input string. This behavior is the same as the  [Parse](func_parse.htm)  function. To preserve empty strings, use the  [Scan](func_scan.htm)  or  [ScanEscape](func_scanescape.htm)  functions. Using ParseEscape on a string with two adjacent delimiters:

```
ParseEscape('Two, separators', ' ,' )
```

returns:

```
Two
separators
```

While the same input string provided to  [ScanEscape](func_scanescape.htm)  :

```
ScanEscape('Two, separators', ' ,' )
```

returns:

```
Two

separators
```

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Input string |
| 2 | String | No | Space, tab, comma | Delimiters |

#### Argument 1

Input string

#### Argument 2

Delimiters

### Returns

Return type: string array

The input string split into a string array with the escaped delimiters replaced with unescaped delimiters.

### See Also

* [Parse](func_parse.htm)
* [Scan](func_scan.htm)
* [ScanEscape](func_scanescape.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parseescape) | | |
| [◄ ParseAnalysis](func_parseanalysis.htm) |  | [ParseLaplace ▶](func_parselaplace.htm) |
