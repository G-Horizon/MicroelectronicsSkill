# RegExStrStr Function

This function compiles a regular expression from the second argument and searches for a regular expression match in the string supplied as the first argument. The return value is a the index where the pattern match occurs, or an empty vector if no matches are found in the input string.

The third argument is the offset into the input string to start the regular expression search.

In common with the other Regular Expression functions, this function is case  *insensitive*  by default. Also by default, the dot metacharacter character '.' does not match new line characters. You can change these behaviors using two options passed as the fourth argument.

The regular expression functions in SIMetrix/SIMPLIS support Perl-compatible regular expressions. Forward references, back references, alternation, capturing up to 99 groups, negative and positive look behind and ahead assertions are all supported. Regular expressions can be tested for validity with the  [RegExIsValid](func_regexisvalid.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to search |
| 2 | string | Yes |  | Regular expression |
| 3 | real | No | 0 | Character offset |
| 4 | string | No |  | Options |

#### Argument 1

The input string to find regular expression matches.

#### Argument 2

The regular expression string.

#### Argument 3

The character position to start the regular expression search. 0 starts the search at the beginning of the input string.

#### Argument 4

Two options are supported :

* casesensitive
* dotmatchesall

Passing the first option 'casesensitive' makes the regular expression match case sensitive.The second option 'dotmatchesall' causes the dot('.') metacharacter to match new lines in the input string. You can pass both options as a string array:

```
[ 'casesensitive' , 'dotmatchesall' ]
```

### Returns

Return type: real

A real number indicating the index into the input string where the regular expression match occurs. If no match is found, returns an empty vector.

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExContains](func_regexcontains.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

Find the index where a phrase starts:

```
RegExStrStr( 'abcdef' , 'de' )
```

returns 3 because 'de' starts at the fourth character, or index=3 in the input string 'abcdef'. Using alternation, find the location where the input string contains 'bc' or 'de':

```
RegExStrStr('abcdef', 'de|bc' )
```

returns 1 because 'bc' matches at the second character, or index=1 of the input string 'abcdef'. A failing match:

```
RegExStrStr( 'abcdef' , '^xyz' )
```

returns an empty vector. You can check the length of the return with the  [Length](func_length.htm)  function.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexstrstr) | | |
| [◄ RegExSplit](func_regexsplit.htm) |  | [RelativePath ▶](func_relativepath.htm) |
