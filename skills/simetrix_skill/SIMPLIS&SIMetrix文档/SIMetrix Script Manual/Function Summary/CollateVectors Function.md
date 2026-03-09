# CollateVectors Function

Returns the data for the specified vectors in an interleaved manner suitable for writing out in common simulation data formats such as SPICE3 raw format.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Vector names |
| 2 | string | Yes |  | Group name |
| 3 | real array | No |  | Start index, length, division index |

#### Argument 1

List of vector names. Note that they must be valid vector names in the group specified by argument 2. Expressions of vectors are not permitted.

#### Argument 2

Group name holding vectors specified in argument 1.

#### Argument 3

Three element array. Element 1 is the start index for the return values, element 2 is the number of values to be returned for each vector and element 3 is the division index. The default values for the three elements are 0, the length of the first vector and 0 respectively.

### Returns

Return type: real or complex array

If the vectors supplied in arg 1 are real the return value will be a real array. If they are complex the return value will be a complex array. The length of the result will be 3+(number of vectors)\*(vector length)

The first three elements of the array are:

|  |  |
| --- | --- |
| 0: | number of vectors |
| 1: | start index |
| 2: | length of each vector |

The remaining elements hold the vector data. This is in the following order:

```
vec1[0]
vec2[0]
vec3[0]....
vecn[0]
vec1[1]
vec2[1]
vec3[1]...
vecn[1]
vec1[2]
vec2[2]
vec3[2]....
vecn[2]
etc.
```

Where vec1 is the first vector specified in arg 1, vec2 the second and so on.

This function is used by the write\_raw\_file script to create SPICE3 raw file data. The source for this script is provided on the install CD.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_collatevectors) | | |
| [◄ CollateNested](func_collatenested.htm) |  | [CommandStatus ▶](func_commandstatus.htm) |
