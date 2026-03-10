# RegExContains Function

This function compiles a regular expression from the second argument and searches for a regular expression match in the string supplied as the first argument. The return value is a 1 if one or more matches of the regular expression exist, 0 if no matches are found in the input string.

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

The input string to test if there is one or more matches to the regular expression.

#### Argument 2

The regular expression string.

#### Argument 3

The character position to start the regular expression search. 0 starts the search at the beginning of the input string.

#### Argument 4

Two options are supported:

* casesensitive
* dotmatchesall

Passing the first option 'casesensitive' makes the regular expression match case sensitive. The second option 'dotmatchesall' causes the dot ('.') metacharacter to match new lines in the input string. You can pass both options as a string array:

```
[ 'casesensitive' , 'dotmatchesall' ]
```

### Returns

Return type: real

A real number 1, indicating one or more matches of the regular expression are found in the input string, or 0 indicating no matches of the regular expression are found in the input string.

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

Find if a string starts with a certain phrase:

```
RegExContains( 'Abc' , '^ab' )
```

returns 1 because 'Abc' starts with 'ab' without case sensitivity. Setting case sensitive matching, starting at the beginning of the input string:

```
RegExContains( 'Abc' , '^ab' , 0 , 'casesensitive' )
```

returns 0 because the case sensitive match fails.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexcontains) | | |
| [◄ RefName](func_refname.htm) |  | [RegExIsValid ▶](func_regexisvalid.htm) |
