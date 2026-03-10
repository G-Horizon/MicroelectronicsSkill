# RegExMatch Function

This function compiles a regular expression from the second argument and searches for a regular expression match in the string supplied as the first argument. The return value is a string array containing the matched strings. This first index is the string which the entire regular expression matched, each index after the first represents any captured text using the capturing groups syntax: (). If no match occurs, an empty vector is returned.

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

The input string to find the index where the regular expression match occurs.

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

Return type: string array

String array containing the matched strings.

### See Also

* [RegExIsValid](func_regexisvalid.htm)
* [RegExContains](func_regexcontains.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

A simple example without capturing groups:

```
RegExMatch('abcdef', 'de|bc' )
```

returns the matched string, in this case 'bc'. A more advanced example where substrings are found and captured:

```
RegExMatch( 'POWER_SUPPLY_LOAD_3_RES' , '(SIMPLIS_DVM_ADVANCED|POWER_SUPPLY)_LOAD_(\d)' )
```

returns a string array with three elements. The first element contains the entire matched text, the second element contains the string matched by the first captured group (SIMPLIS\_DVM\_ADVANCED|POWER\_SUPPLY), the third element contains the text from the second captured group (\d):

```
'POWER_SUPPLY_LOAD_3'
'POWER_SUPPLY'
'3'
```

A failing match:

```
RegExMatch( 'res_z' , '(SIMPLIS_DVM_ADVANCED|POWER_SUPPLY)_LOAD_(\d)' )
```

returns an empty vector. You can check the length of the return with the  [Length](func_length.htm)  function.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexmatch) | | |
| [◄ RegExIsValid](func_regexisvalid.htm) |  | [RegExp ▶](func_regexp.htm) |
