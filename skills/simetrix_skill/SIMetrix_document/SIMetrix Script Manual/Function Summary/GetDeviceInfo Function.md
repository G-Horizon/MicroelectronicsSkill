# GetDeviceInfo Function

Returns information about the specified simulator device.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Model name |
| 2 | string | No | none | Options |

#### Argument 1

Internal device name as returned by the GetModelType or GetInternalDeviceName function. This is not the same as the type name used in the .MODEL control but a name that is used internally by the simulator. For example, the internal device name for a LEVEL 1 MOSFET is 'MOS1'.

Optionally the device letter may be specified if arg2 = 'letter'. However, the function will not return such precise information if this option is used. For example, the LEVEL value will not be known and so -1 will be returned. Also the minimum and maximum number of terminals will reflect all devices that use that device letter and not just one specific device. E.g. the 'BJT' device defines the standard SPICE Gummel-Poon transistor which can have 3 or 4 terminals. But the 'q' letter can also specify VBIC\_Thermal devices which can have 5 terminals.

#### Argument 2

Options, currently only one. If this is set to 'letter', a single letter should be specified for argument 1. This is the device letter as used in the netlist, e.g. 'Q' for a BJT, 'R' for a resistor. See notes above concerning specifying using the device letter.

### Returns

Return type: string array

Result is a 7 element array about the specified simulator device.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Model type name for negative polarity device. E.g. 'npn', 'nmos' etc. |
| 1 | Model type name for positive polarity device E.g. 'pnp', 'pmos' etc. Empty if device has only a single polarity |
| 2 | Device letter. E.g. 'Q' for a BJT |
| 3 | Maximum number of terminals. |
| 4 | Minimum number of terminals. This is usually the same as the maximum number of terminals, except for BJTs whose substrate terminal is optional. |
| 5 | Value required for LEVEL parameter. 0 means that this is the default device when no LEVEL parameter is specified. -1 will be returned if the 'letter' option is specified. |
| 6 | Semi-colon delimited list of valid .MODEL control model name values. E.g. 'npn', 'pnp' and 'lpnp' are returned for the 'BJT' device. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdeviceinfo) | | |
| [◄ GetDeviceDefinition](func_getdevicedefinition.htm) |  | [GetDeviceParameterNames ▶](func_getdeviceparameternames.htm) |
