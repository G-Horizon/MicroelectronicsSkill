# MkVec Function

Most simulation vectors are accessed using the name of the node that generated the data. For example if a node is called 'VOUT' the vector to access the data on that node is also called 'VOUT'.

However, some nodes are named in a manner that cannot directly be accessed as the name contains characters that can be confused with arithmetic and other operators. For example, it is legal to call a node +15V but this would be confused with the constant value +15.

To resolve this, a vector may be accessed using the  [Vec](func_vec.htm)  function. E.g. Vec('+15V'). The MkVec() function will return a string that can be used to access the vector data. If the vector name does not contain any conflicting characters, it will return the name unmodified. If it does contain conflisting characters, it will return a string using the Vec function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Node name |

### Returns

Return type: string

Expression to access node data

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_mkvec) | | |
| [◄ MinN](func_minn.htm) |  | [MLRidgeRegressionFit ▶](func_mlridgeregressionfit.htm) |
