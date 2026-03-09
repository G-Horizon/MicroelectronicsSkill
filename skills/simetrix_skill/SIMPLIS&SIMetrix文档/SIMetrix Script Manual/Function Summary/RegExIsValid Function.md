# RegExIsValid Function

This function checks if the regular expression provided as the first argument is a valid regular expression. There are several reasons why a regular expression could be invalid. These include unbalanced capturing parentheses, referencing a captured group which is not actually captured etc. This function returns a real 1 if the regular expression is valid or a string with an error message. You can test the type of the return value with the  [IsStr](func_isstr.htm)  function.

Note that you will only need to use this function for development or in a script where the regular expression is created during script execution. Any regular expression entered as a string literal can be checked before the script is executed using this function, and the actual script will not need to call this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Regular expression |

#### Argument 1

The regular expression string.

### Returns

Return type: real or string

If the expression is valid, the return is a real 1. If invalid, a string error message describing why the regular expression is not valid.

### See Also

* [RegExContains](func_regexcontains.htm)
* [RegExMatch](func_regexmatch.htm)
* [RegExReplace](func_regexreplace.htm)
* [RegExSearch](func_regexsearch.htm)
* [RegExSearchAll](func_regexsearchall.htm)
* [RegExStrStr](func_regexstrstr.htm)
* [RegExSplit](func_regexsplit.htm)

### Example

An example of a missing opening parentheses:

```
RegExisValid('asdfghjkl)')
```

returns 'Invalid regular expression (unmatched closing parenthesis) index into regular expression string where error occurs : 9' An example of a missing closing parentheses:

```
RegExisValid('(asdfghjkl')
```

returns 'Invalid regular expression (missing closing parenthesis) index into regular expression string where error occurs : 10' Once the opening and closing parentheses are correctly matched:

```
RegExisValid('(asdfghjkl)')
```

returns 1.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_regexisvalid) | | |
| [◄ RegExContains](func_regexcontains.htm) |  | [RegExMatch ▶](func_regexmatch.htm) |
