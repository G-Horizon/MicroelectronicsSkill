# GetAllSymbolPropertyNames Function

Returns a string array containing the names of all the properties on the symbol currently open in the symbol editor.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Options |

#### Argument 1

Options. Currently, there is only one which is 'nopins'. If  *not*  present, the function will return all properties including the internally generated properties used to display pin names. These are of the form $Pin$  *pinname* . If 'nopins' is specified, these properties will not be returned by the function.

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getallsymbolpropertynames) | | |
| [◄ GetAllSimulatorDevices](func_getallsimulatordevices.htm) |  | [GetAllXAxes ▶](func_getallxaxes.htm) |
