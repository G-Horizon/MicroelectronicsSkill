# Truncate Function

Returns a portion of the input vector with defined start and end points. Interpolation will be used to create the first and last points of the result if the start and end values do not coincide with actual points in the input vector.

Arguments 2 and 3 define the beginning and end of the vector.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | Vector |
| 2 | real | No | start of vector | Start x value |
| 3 | real | No | end of vector | end x value |

### Returns

Return type: real XY array

### Example

Suppose we have a vector called VOUT which was the result of a simulation running from 0 to 1mS. We want to perform some analysis on a portion of it from ???MATH???250\mu???MATH???S to ???MATH???750\mu???MATH???S. The following call to Truncate would do this:

```
Truncate(VOUT, 250u, 750u)
```

If VOUT did not actually have points at ???MATH???250\mu???MATH???S and ???MATH???750\mu???MATH???S then the function would create them by interpolation. Note that the function will not extrapolate points before the start or after the end of the input vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_truncate) | | |
| [◄ True](func_true.htm) |  | [TwoFileSelectionDialog ▶](func_twofileselectiondialog.htm) |
