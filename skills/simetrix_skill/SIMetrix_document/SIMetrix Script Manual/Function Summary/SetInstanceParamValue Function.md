# SetInstanceParamValue Function

Script-based multi-step analyses use a script call to define each step. This function can be used in such a script to a set an instance parameter.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | yes |  | Instance name |
| 2 | string | Yes |  | Parameter name |
| 3 | string | Yes |  | New parameter value |
| 4 | real | No | 0 | Vector index for vector parameters |

### Returns

String indicating status of function call:

|  |  |
| --- | --- |
| **Return string** | **Description** |
| 'success' | Function successful |
| 'badparam' | Unknown parameter name |
| 'noinstance' | Unknown instance name |
| 'nocircuit' | No circuit loaded |

### See Also

* [GetCurrentStepValue](func_getcurrentstepvalue.htm)
* [SetModelParamValue](func_setmodelparamvalue.htm)
* [GetModelParameterValues](func_getmodelparametervalues.htm)
* [GetDotParamValue](func_getdotparamvalue.htm)

### Example

The following script code sets the area parameter of 'Q6' to values of 100, 200 and 400 for the first, second and third steps respectively.

```
Let values = [1, 2, 4]
Let step = GetCurrentStepValue()
Let value = values[step-1]

Let SetInstanceParamValue('q6', 'area', value)
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_setinstanceparamvalue) | | |
| [◄ SetDifference](func_setdifference.htm) |  | [SetIntersect ▶](func_setintersect.htm) |
