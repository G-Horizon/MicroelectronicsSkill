# MakeString Function

Creates an array of strings. Length of array is given as argument to function. The strings may be initialised by supplying argument 2.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Number of elements in result |
| 2 | string array | No |  | Initial values |

#### Argument 1

Number of elements to create in string array.

#### Argument 2

Initialises values of string. Can be used to extend an existing string. e.g:

```
Let str = ['john', 'fred', 'bill']
Let str = MakeString(6, str)
```

In the above the string `str` will be extended from length 3 to length 6 by the call to `MakeString`.

### Returns

Return type: string array

Returns new string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_makestring) | | |
| [◄ MakeLogicalPath](func_makelogicalpath.htm) |  | [makevec ▶](func_makevec.htm) |
