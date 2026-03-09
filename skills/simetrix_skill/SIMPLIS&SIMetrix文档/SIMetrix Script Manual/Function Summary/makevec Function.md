# makevec Function

Returns a vector consisting of all 0's. Scalar argument specifies length of vector. If argument is itself a vector, the return value is a multi-division vector whose division lengths are defined by the value sin each field

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real scalar or array | Yes |  | Number of elements in result or each division in reault |

#### Argument 1

Number of elements in result if argument is a scalar. If the argument is a vector, the return value will be a multi-division vector with a number of divisions equal to the length of this argument. The length of each division will be equal to the corresponding entry in this argument

### Returns

Return type: real array

Vector or multi-division vector with all values set to zero

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_makevec) | | |
| [◄ MakeString](func_makestring.htm) |  | [ManageDataGroupsDialog ▶](func_managedatagroupsdialog.htm) |
