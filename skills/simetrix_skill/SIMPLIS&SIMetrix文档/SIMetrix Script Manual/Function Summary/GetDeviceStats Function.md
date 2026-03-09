# GetDeviceStats Function

Get simulation statistics for each device type

### Arguments

No arguments

### Returns

Return type: string array

Array of strings with each element containing a list of name=value pairs providing information on each device type used in the simulator. Information provided is as follows:

|  |  |
| --- | --- |
| **Name** | **Value** |
| (unlabelled) | Device type |
| Tload | Time in seconds used to evaluate the device's equations. This entry will be zero unless '.OPTIONS devacct' is specified in the simulation netlist |
| Count | Number of instances of this device type |
| ByteCount | Number of bytes used to store the data for instances of this device |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdevicestats) | | |
| [◄ GetDevicePins](func_getdevicepins.htm) |  | [GetDisabledInstances ▶](func_getdisabledinstances.htm) |
