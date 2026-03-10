# SetModelParamValue Function

Script-based multi-step analyses use a script call to define each step. This function can be used in such a script to a set a model parameter.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | yes |  | Model name |
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
| 'nomodel' | Unknown model name |
| 'nocircuit' | No circuit loaded |

### See Also

* [GetCurrentStepValue](func_getcurrentstepvalue.htm)
* [SetInstanceParamValue](func_setinstanceparamvalue.htm)
* [GetModelParameterValues](func_getmodelparametervalues.htm)
* [GetDotParamValue](func_getdotparamvalue.htm)

### Example

The following script code sets the BF parameter to values of 100, 200 and 400 for the first, second and third steps respectively.

```
Let values = [100, 200, 400]
Let step = GetCurrentStepValue()
Let value = values[step-1]

Let SetModelParamValue('BC546B', 'BF', value)
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_setmodelparamvalue) | | |
| [◄ SetIntersect](func_setintersect.htm) |  | [SetPropertyStyles ▶](func_setpropertystyles.htm) |
