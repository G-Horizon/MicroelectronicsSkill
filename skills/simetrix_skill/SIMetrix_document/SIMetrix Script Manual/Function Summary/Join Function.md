# Join Function

Joins the input string array passed as argument 1 with the separator passed as argument 2. Returns a single string with all array elements joined with the common separator.

The separator can be any string, including an empty string. Common uses for this function include joining together the ComboBox control for the  [NewValueDialog](func_newvaluedialog.htm)  function, among many other uses.

This function is much faster than looping when joining large string arrays, for example a file read in by  [ReadFile](func_readfile.htm) . This is due to the binary implementation of the function which is much faster than looping in a script.

This function differs significantly from  [JoinStringArray](func_joinstringarray.htm) . The Join function returns a single string.  [JoinStringArray](func_joinstringarray.htm)  returns the concatenation of two arrays, which is a string array.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String Array | Yes |  | List to Join |
| 2 | String | Yes |  | Separator string |

#### Argument 1

List to Join

#### Argument 2

The string to join the array with. May be empty.

### Returns

Return type: string

Joined string.

### See Also

* [JoinStringArray](func_joinstringarray.htm)
* [Parse](func_parse.htm)
* [Scan](func_scan.htm)
* [ParseEscape](func_parseescape.htm)
* [ScanEscape](func_scanescape.htm)

### Example

A call to:

```
Join( [ 'a' , 'b' , 'c' ] , '|' )
```

will return the string 'a|b|c'. Joining on an empty string:

```
Join( [ 'a' , 'b' , 'c' ] , " )
```

will return the string 'abc'. Joining a string array of one element:

```
Join( [ 'a' ] , ',' )
```

will return the string 'a'. In this case the separator is ignored. Reading in a file as a single string:

```
Let file_array = ReadFile( 'data.txt' )
Let file_as_string = Join( file_array , " )
```

The resulting variable file\_as\_string will be a single string containg all the text of the data.txt file.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_join) | | |
| [◄ Jitter](func_jitter.htm) |  | [JoinStringArray ▶](func_joinstringarray.htm) |
