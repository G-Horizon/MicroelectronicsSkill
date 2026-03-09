# SortIdx2 Function

Sorts the items in argument 1 but instead of returning the actual sorted data the function returns the indexes of the sorted values into the original array. The method of sorting depends on the data type as follows:

|  |  |
| --- | --- |
| string | Alphabetic |
| real | Numeric |
| complex | Numeric - uses magnitude |

Use this function instead of SortIdx in new code. The original function sorted numeric values from high value to low value which is the opposite to what might usually be expected.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | any array | Yes |  | Items to sort |
| 2 | string | No | 'forward' | Sort direction |

#### Argument 2

Sort option, value either 'forward' or 'reverse'. 'forward' for numeric data means lowest values first.

### Returns

Return type: real array

An array of indexes into the input array, sorted by the method specified in argument 2.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_sortidx2) | | |
| [◄ SortIdx](func_sortidx.htm) |  | [SourceDialog ▶](func_sourcedialog.htm) |
