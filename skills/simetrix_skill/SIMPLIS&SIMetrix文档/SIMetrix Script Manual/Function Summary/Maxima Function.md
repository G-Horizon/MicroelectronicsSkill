# Maxima Function

Returns array of values holding every maximum point in the supplied vector whose value complies with limits specified in argument 2.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real XY array | Yes |  | Vector |
| 2 | real array | No | [???MATH???-\infty, +\infty???MATH???] | [min limit, max limit] |
| 3 | string | No | <<empty>> | Options |
| 4 | real | No | 0.0 | Tolerance |

#### Argument 1

Input vector

#### Argument 2

Real array of max length 2. Specifies limits within which the input values must lie to be included in the result. Values are:

|  |  |
| --- | --- |
| 0 | Minimum limit i.e. maxima must be above this to be accepted |
| 1 | Maximum limit i.e. maxima must be below this to be accepted. |

#### Argument 3

String array of max length 2. Specifies two possible options:

|  |  |
| --- | --- |
| 'xsort' | If specified the output is sorted in order of their x-values (reference). Otherwise the values are sorted in descending order of y magnitude. |
| 'nointerp' | If not specified the values returned are obtained by fitting a parabola to the maximum and each point either side then calculating the x, y location of the point with zero slope. Otherwise no interpolation is carried out and the literal maximum values are returned. |
| 'noendpts' | If specified, the first and last points in the data will not be returned as maximum points. |

#### Argument 4

Minimum spacing between x values. Any pair of points that are closer than this value will be treated as a single point

### Returns

Return type: real XY array

The function returns the XY values for each maximum point. The X-values are returned as the vector's reference (see  [Vector References](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__vectorreferences)  ).

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_maxima) | | |
| [◄ maxidx](func_maxidx.htm) |  | [Maximum ▶](func_maximum.htm) |
