# SortIdx Function

This function is deprecated. Use  [SortIdx2](func_sortidx2.htm)  for new code.

Sorts the items in argument 1 but instead of returning the actual sorted data the function returns the indexes of the sorted values into the original array. The method of sorting depends on the data type as follows:

|  |  |
| --- | --- |
| string | Alphabetic |
| real | Numeric |
| complex | Numeric - uses magnitude |

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | any array | Yes |  | Items to sort |
| 2 | string | No | 'forward' | Sort direction |

#### Argument 2

Sort option, value either 'forward' or 'reverse'. For numeric data, 'forward' returns highest values first. This is the opposite of what might be expected.  [SortIdx2](func_sortidx2.htm)  behaves as expected and should be used in new code.

### Returns

Return type: real array

An array of indexes into the input array, sorted by the method specified in argument 2.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_sortidx) | | |
| [◄ Sort](func_sort.htm) |  | [SortIdx2 ▶](func_sortidx2.htm) |
