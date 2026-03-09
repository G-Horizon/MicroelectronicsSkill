# GetCurrentStepValue Function

Returns the current step value in a script-based multi-step analysis. Script-based multi-step analyses use a script call to define each step. For this analysis type, a counter is maintained which increments on each step. This function returns the value of that counter. Note that the counter is initialised to 1.

### Arguments

No arguments

### Returns

### See Also

* [SetModelParamValue](func_setmodelparamvalue.htm)
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
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcurrentstepvalue) | | |
| [◄ GetCurrentGraph](func_getcurrentgraph.htm) |  | [GetCursorCurve ▶](func_getcursorcurve.htm) |
