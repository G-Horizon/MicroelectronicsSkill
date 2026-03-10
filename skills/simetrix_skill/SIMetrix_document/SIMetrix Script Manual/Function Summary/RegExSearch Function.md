# RegExSearch Function

This function compiles a regular expression from the second argument and searches for a regular expression match in each element of the string array supplied as the first argument. The return value is the index into the input string array where the first match occurs, or -1 if no matches are found. This function is a regular expression version of the  [Search](func_search.htm)  function.

The third argument is the offset into the input string to start the regular expression search.

In common with the other Regular Expression functions, this function is case  *insensitive*  by default. Also by default, the dot metacharacter character '.' does not match new line characters. You can change these behaviors using two options passed as the fourth argument.

The regular expression functions in SIMetrix/SIMPLIS support Perl-compatible regular expressions. Forward references, back references, alternation, capturing up to 99 groups, negative and positive look behind and ahead assertions are all supported. Regular expressions can be tested for validity with the  [RegExIsValid](func_regexisvalid.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | String array to search |
| 2 | string | Yes |  | Regular expression |
| 3 | real | No | 0 | Character offset |
| 4 | string | No |  | Options |

#### Argument 1

The input string array to search for the regular expression match.

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

The index into the input string array where the first match occurs, or -1 indicating no matches of the regular expression are found in the input string array.

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExContains](func_regexcontains.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

A simple example where a string array is searched for a certain phrase:

```
RegExSearch( [ '.tran 1m 0' , '.pop TRIG_COND=1_TO_0 MAX_PERIOD=2.2u' , '.options POP_USE_TRAN_SNAPSHOT' , '.options POP_ITRMAX=20' ] , '\.options' )
```

returns 2 because the first occurrence of the literal '.options' occurs at index=2. Note that the '.' metacharacter character is escaped with the '\' character in the regular expression string. A failing example:

```
RegExSearch( [ '.tran 1m 0' , '.pop TRIG_COND=1_TO_0 MAX_PERIOD=2.2u' , '.options POP_USE_TRAN_SNAPSHOT' , '.options POP_ITRMAX=20' ] , '\.ac' )
```

returns -1 because '.ac' is not found in any of the input string array elements.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexsearch) | | |
| [◄ RegExReplace](func_regexreplace.htm) |  | [RegExSearchAll ▶](func_regexsearchall.htm) |
