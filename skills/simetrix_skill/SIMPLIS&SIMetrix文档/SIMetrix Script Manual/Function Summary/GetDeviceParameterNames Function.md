# GetDeviceParameterNames Function

Returns string array containing all device parameter names for the specified simulator model type.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Device type |
| 2 | real | No | -1 | Level |
| 3 | string array | No |  | Options |

#### Argument 1

Device type specified using its SPICE letter e.g. 'Q' for a BJT, 'M' for a MOSFET etc.

#### Argument 2

Model level if relevant. If omitted or set to -1, the default level for that type of device will be used.

#### Argument 3

String array of length up to 2. May contain one or both of 'useInternalName' and 'readback'. If 'useInternalName', then argument 1 must specify the device's internal name. This is returned by  [GetInternalDeviceName](func_getinternaldevicename.htm) . Argument 2 is ignored in this case.

If 'readback' is specified, the function returns names of 'read back' parameters. Read back parameters aren't writeable but return information about a device's operating characteristics. For example, most MOS devices have 'vdsat' read back parameter that returns the saturation voltage. This function only returns the names of read back parameters. To find their values, use  [GetInstanceParamValues](func_getinstanceparamvalues.htm) .

### Returns

Return type: string array

String array of length determined by the number of parameters the device has. Each element contains the name of a single parameter. To find the values for the parameters use  [GetInstanceParamValues](func_getinstanceparamvalues.htm) .

### Example

The following:

```
Show GetDeviceParameterNames('M')
```

returns:

```
0    'L'
1    'W'
2    'M'
3    'AD'
4    'AS'
5    'PD'
6    'PS'
7    'NRD'
8    'NRS'
9    'IC-VDS'
10   'IC-VGS'
11   'IC-VBS'
12   'TEMP'
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdeviceparameternames) | | |
| [◄ GetDeviceInfo](func_getdeviceinfo.htm) |  | [GetDevicePins ▶](func_getdevicepins.htm) |
