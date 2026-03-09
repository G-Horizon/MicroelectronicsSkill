# RegExSplit Function

This function compiles a regular expression from the second argument and splits the first argument into a string array where the regular expression defines the delimiters. If no delimiters are found in the input string, the input string is returned unaltered. To split a string on a single character which is also escaped, see the  [ScanEscape](func_scanescape.htm)  and  [ParseEscape](func_parseescape.htm)  functions.

In common with the other Regular Expression functions, this function is case  *insensitive*  by default. Also by default, the dot metacharacter character '.' does not match new line characters. You can change these behaviors using two options passed as the third argument.

The regular expression functions in SIMetrix/SIMPLIS support Perl-compatible regular expressions. Forward references, back references, alternation, capturing up to 99 groups, negative and positive look behind and ahead assertions are all supported. Regular expressions can be tested for validity with the  [RegExIsValid](func_regexisvalid.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to split |
| 2 | string | Yes |  | Regular expression |
| 3 | string | No |  | Options |

#### Argument 1

The input string to split on the regular expression match.

#### Argument 2

The regular expression string.

#### Argument 3

Two options are supported:

* casesensitive
* dotmatchesall

Passing the first option 'casesensitive' makes the regular expression match case sensitive. The second option 'dotmatchesall' causes the dot ('.') metacharacter to match new lines in the input string. You can pass both options as a string array:

```
[ 'casesensitive' , 'dotmatchesall' ]
```

### Returns

Return type: string array

The input string tokenized on the regular expression.

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExContains](func_regexcontains.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)

### Example

A simple example where the input string is split on a literal underscore character

```
RegExSplit( 'PARAM_MODEL_NAME' , '_' )
```

returns the array:

```
'PARAM'
'MODEL'
'NAME'
```

A more complex example using a negative look behind assertion. This splits the string on the underscore as long as the previous letter isn't a 'L'.

```
RegExSplit( 'PARAM_MODEL_NAME' , '(?<!L)_' )
```

The return value is the two elements:

```
'PARAM'
'MODEL_NAME'
```

An example where the regular expression is not found in the input string:

```
RegExSplit( 'PARAM_MODEL_NAME' , 'z' )
```

Returns the input string: 'PARAM\_MODEL\_NAME'

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexsplit) | | |
| [◄ RegExSearchAll](func_regexsearchall.htm) |  | [RegExStrStr ▶](func_regexstrstr.htm) |
