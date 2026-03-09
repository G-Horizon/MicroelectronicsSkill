# Range Function

Returns a vector which is a range of the input vector in argument 1. The range extends from the indexes specified by arguments 2 and 3. If argument 3 is not supplied the range extends to the end of the input vector. If neither arguments 2 or 3 are supplied, the input vector is returned unmodified.

See also the function  [Truncate](func_truncate.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real/complex or string array | Yes |  | Vector |
| 2 | real | No |  | Start index |
| 3 | real | No | Vector length -1 | End index |

### Returns

Return type: matches argument 1. If argument 1 is an XY vector, the return value will be an XY vector

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_range) | | |
| [◄ RadioSelect](func_radioselect.htm) |  | [re ▶](func_re.htm) |
