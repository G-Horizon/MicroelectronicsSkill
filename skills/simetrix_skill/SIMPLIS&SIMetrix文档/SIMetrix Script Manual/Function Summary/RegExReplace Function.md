# RegExReplace Function

This function compiles a regular expression from the second argument and searches for a regular expression match in the string supplied as the first argument. Where the regular expression matches, the replacement string is inserted into the input string. The return value is the input string with the replaced matches. If no match occurs, the input string is returned unaltered.

The third argument is the replacement string, which can contain backreferences.

The fourth argument is the offset into the input string to start the regular expression search.

In common with the other Regular Expression functions, this function is case  *insensitive*  by default. Also by default, the dot metacharacter character '.' does not match new line characters. You can change these behaviors using two options passed as the fifth argument.

The regular expression functions in SIMetrix/SIMPLIS support Perl-compatible regular expressions. Forward references, back references, alternation, capturing up to 99 groups, negative and positive look behind and ahead assertions are all supported. Regular expressions can be tested for validity with the  [RegExIsValid](func_regexisvalid.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to search |
| 2 | string | Yes |  | Regular expression |
| 3 | string | Yes |  | Replacement string |
| 4 | real | No | 0 | Character offset |
| 5 | string | No |  | Options |

#### Argument 1

The input string to find and replace where the regular expression match occurs.

#### Argument 2

The regular expression string.

#### Argument 3

The replacement string, which can contain backreferences.

#### Argument 4

The character position to start the regular expression search. 0 starts the search at the beginning of the input string.

#### Argument 5

Two options are supported :

* casesensitive
* dotmatchesall

Passing the first option 'casesensitive' makes the regular expression match case sensitive.The second option 'dotmatchesall' causes the dot('.') metacharacter to match new lines in the input string. You can pass both options as a string array:

```
[ 'casesensitive' , 'dotmatchesall' ]
```

### Returns

Return type: string

The input string with the regular expression replacements

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExContains](func_regexcontains.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

A simple example where the number of pins is replaced with '3':

```
RegExReplace( 'SIMPLIS_DVM_ADVANCED_LOAD_4T_RES_BODE', '\d' , '3')
```

returns 'SIMPLIS\_DVM\_ADVANCED\_LOAD\_3T\_RES\_BODE'. A more advanced example which produces the same result but a much more restrictive regular expression, and the second backreference.

```
RegExReplace( 'SIMPLIS_DVM_ADVANCED_LOAD_4T_RES_BODE', '^SIMPLIS_DVM_ADVANCED_LOAD_(\d)T(_.*)$' , 'SIMPLIS_DVM_ADVANCED_LOAD_3T\2' )
```

returns 'SIMPLIS\_DVM\_ADVANCED\_LOAD\_3T\_RES\_BODE'. A failing match and replace:

```
RegExReplace( 'res_z' , '^SIMPLIS_DVM_ADVANCED_LOAD_(\d)T(_.*)$' , 'SIMPLIS_DVM_ADVANCED_LOAD_3T\2' )
```

Returns the input string: 'res\_z'.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexreplace) | | |
| [◄ RegExp](func_regexp.htm) |  | [RegExSearch ▶](func_regexsearch.htm) |
