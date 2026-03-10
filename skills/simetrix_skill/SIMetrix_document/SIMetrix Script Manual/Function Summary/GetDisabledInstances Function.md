# GetDisabledInstances Function

Returns a list of all disabled instances on the current schematic. Instances may be disabled using the  [SetDisable](com_setdisable.htm)  command. A disabled instance is inactive as if it were not present in the schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Property used to report instances |
| 2 | String | Yes |  | Options |
| 3 | real | No | -1 | Schematic ID |

#### Argument 1

Property used to report instances

#### Argument 2

If set to 'type', the function will return 'short' if the instances is short-circuited or 'open' if it is open circuit. Otherwise, the function will return the property value of the disabled instance.

#### Argument 3

Schematic ID as returned by  [OpenSchematic](func_openschematic.htm) . This makes it possible to apply this function to any schematic and not just the one that is currently displayed. See  [OpenSchematic](func_openschematic.htm)  for more details.

### Returns

Return type: String array

List of property values (defined by argument 1) identifying the disabled instances. If arg2 is set to type, will return 'short' or 'open'

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getdisabledinstances) | | |
| [◄ GetDeviceStats](func_getdevicestats.htm) |  | [GetDivisionLabels ▶](func_getdivisionlabels.htm) |
