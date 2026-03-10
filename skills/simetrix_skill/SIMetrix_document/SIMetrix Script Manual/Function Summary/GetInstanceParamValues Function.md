# GetInstanceParamValues Function

Returns simulation instance parameter values for the device specified. This function returns the values used in the most recent simulation. If simulation has been run, or it was aborted or reset (using Reset command), then this function will return an empty vector.

If argument 3 is set to 'readback', this function will return the values for readback parameters.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Instance name |
| 2 | string | No | Get all parameters | Parameter name |
| 3 | string | No |  | Options |

#### Argument 1

Instance name, e.g. Q23, R3 etc. This is the name used in the netlist stripped of its dollar prefix if applicable.

#### Argument 2

Name of parameter whose value is required. If this argument is missing or empty, then all parameters will be returned. The number and order of the parameters in this case will match the return value of parameter names from the function  [GetDeviceParameterNames](func_getdeviceparameternames.htm) .

#### Argument 3

If set to 'readback' and argument 2 is empty, this function will return the values of all read back values for the devices. 'read back' values are values calculated during a run and give useful information about a device's operating conditions. Note that the value returned will reflect the state of the device at the last simulation point. For example, if a transient run has just been performed, the values at the final time point will be given. If a small-signal analysis has been performed, the results will usually reflect the DC operating point conditions.

### Returns

Return type: string or string array

If argument 2 is provided and valid, will return a single string expressing the value of the parameter. If arg 2 is missing or empty, a string array will be returned with all parameter values.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinstanceparamvalues) | | |
| [◄ GetInstanceConvergenceInfo](func_getinstanceconvergenceinfo.htm) |  | [GetInstancePinLocs ▶](func_getinstancepinlocs.htm) |
