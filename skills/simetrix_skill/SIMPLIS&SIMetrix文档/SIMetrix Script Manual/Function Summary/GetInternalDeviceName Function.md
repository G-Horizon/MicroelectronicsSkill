# GetInternalDeviceName Function

Finds the simulator's internal device name for a model defined using its model type name and optionally, level and version.

The internal device name is a unique name used to define a primitive simulator device. For example, npn and pnp transistors have the internal device name of 'BJT'. Level 1 MOSFETs have the internal device name of 'MOS1' while nmos level 8 devices are called 'BSIM3'. Some functions - e.g.  [GetDeviceInfo](func_getdeviceinfo.htm)  - require the internal device name as an argument.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Model details |

### Returns

Return type: string array

1 - 3 element string array which describes device.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Model type name as used in the .MODEL control. E.g. 'nmos', 'npn' etc. |
| 1 | Optional. Value of LEVEL parameter. If omitted, default level is assumed. |
| 2 | Optional. Value of VERSION parameter. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinternaldevicename) | | |
| [◄ GetInstsAtPoint](func_getinstsatpoint.htm) |  | [GetKeyDefs ▶](func_getkeydefs.htm) |
