# GetDevicePins Function

Returns information about the electrical connections on a specified simulator device

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | device identifier |
| 2 | string array | No |  | options |

#### Argument 1

Device identifier. If 'instname' is specified in argument 2, this will be the instance reference of the device. Otherwise the device name must be specified.

#### Argument 2

Can be a combination of 'instname' and 'getterms'. 'instname' means use the instance name to define the device. 'getterms' is functional for Verilog-HDL devices and will instruct the function to return information on vectored terminals.

### Returns

Return type: string array

Array of semi-colon delimited strings providing the following information about the electrical connections to the specified simulator device.

|  |  |
| --- | --- |
| **Field index** | **Description** |
| 1 | Pin name |
| 2 | Direction - in, out or inout. Currently only Verilog-HDL devices will return anything other than in or out for this field |
| 3 | Discipline - Verilog-A devices will return the defined discipline for the connection. This field will be empty for other devices |
| 4 | Connection size for vector connections - Currently only Verilog-HDL devices will return anything other than 1 for this field |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdevicepins) | | |
| [◄ GetDeviceParameterNames](func_getdeviceparameternames.htm) |  | [GetDeviceStats ▶](func_getdevicestats.htm) |
