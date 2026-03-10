# GetDeviceDefinition Function

Searches for the specified device model in the global library and returns the text of the model definition. If the device is defined using a .MODEL control, the result will have a single element containing the whole definition. If the device is defined using a subcircuit then the result will be a string array with a single element for each line in the subcircuit definition.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Device name |
| 2 | string | Yes |  | Device type |
| 3 | string | No | 'SIMetrix' | Simulator type |
| 4 | string | No |  | Options |

#### Argument 1

The model/subcircuit name. E.g. 'Q2N2222' or 'TL072'

#### Argument 2

The type of the device. This may be either the device letter e.g. 'Q' for a BJT, or the model type name e.g. 'npn'. A list of device letters is given in the Simulator Reference manual in the "Running the Simulator" chapter.

If the device is a subcircuit, use the letter 'X'.

#### Argument 3

This must be either 'SIMetrix' or 'SIMPLIS'. If set to SIMPLIS, only subcircuits declared for use with SIMPLIS will be returned. This is done using the .SIMULATOR control in the library file. Note that only SIMPLIS subcircuits are supported. Currently SIMPLIS devices defined using .MODEL are not supported by the SIMetrix model library manager.

#### Argument 4

Options. Currently there is only one: set this argument to 'header' to instruct the function to output preceding comment text. If this is set, up to 20 comment lines (starting with '\*') before the start of the model will also be output.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdevicedefinition) | | |
| [◄ GetDatumCurve](func_getdatumcurve.htm) |  | [GetDeviceInfo ▶](func_getdeviceinfo.htm) |
