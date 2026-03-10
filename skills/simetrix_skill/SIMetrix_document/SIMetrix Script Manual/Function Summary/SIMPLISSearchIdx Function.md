# SIMPLISSearchIdx Function

Searches the input string array at argument 1 for the test string passed as argument 2. Returns a real array of indices into input array where the test string matches. If no matches are found, the function returns -1. The syntax for this function is similar to the  [Search](func_search.htm)  function, except the test string must be a single string, not an array, and the function returns all indices where the test string matches. The  [Search](func_search.htm)  function returns only the first index where the test string matches.

The case sensitivity of the search is defined by the 3rd argument. By default the search is case insensitive. If the 3rd argument is "casesensitive", the search will only return matches using the exact case. If the third argument is omitted or any string but "casesensitive", the matches are returned for case insensitive matches against the test string. The 3rd argument itself is not case sensitive.

This function is useful for searching netlists or other tabular data for indexes where certain strings, such as control statements, are located. Typically the netlist is parsed into columns using the  [SelectColumns](func_selectcolumns.htm)  function. This selects the column where the test data is located. After the finding the indices where the data of interest is located, the original file can be be edited by looping through the indices found by this function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String Array | Yes |  | List to Search |
| 2 | String | Yes |  | Test string |
| 3 | String | No | Empty string | Option |

#### Argument 1

List to Search

#### Argument 2

The string to search the first argument for.

#### Argument 3

If "casesensitive" is passed, the search will be case sensitive.

### Returns

Return type: real array

Array of indexes into argument 1 for the test string found in argument 2. If no matches are found the return value will be -1.

### Example

A call to:

```
SIMPLISSearchIdx( [ '.INCLUDE' , 'X1' , '.Include' , 'C1' ] , '.INCLUDE' )
```

will return a vector [ 0 , 2 ]. Note the matches are by default case insensitive. Passing the third argument as 'caseSensitive' results in a case sensitive search:

```
SIMPLISSearchIdx( [ '.INCLUDE' , 'X1' , '.Include' , 'C1' ] , '.INCLUDE' , 'caseSensitive' )
```

and will return a vector [ 0 ], indicating only the first index matches the test string.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_simplissearchidx) | | |
| [◄ SIMPLISRunStatus](func_simplisrunstatus.htm) |  | [SimulationHasErrors ▶](func_simulationhaserrors.htm) |
