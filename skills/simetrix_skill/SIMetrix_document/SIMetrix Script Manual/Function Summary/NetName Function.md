# NetName Function

Returns the net name of the nearest wire or instance pin.

This function is used for voltage cross-probing. The node vectors produced by the simulator always have the same name as the net so the string returned by this function is the name of the variable holding the voltage at that node.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty>> | Option |

#### Argument 1

The argument determines the behaviour of the function for child schematics in a hierarchy. If the argument is omitted or empty, the full net name is returned including the parents name(s). (E.g. U2.U6.R3\_P). If the argument is the string 'flat' the value returned is just the local netname (E.g. R3\_P).

### Returns

Return type: string

Returns the net name of the nearest wire or instance pin.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_netname) | | |
| [◄ NearestInst](func_nearestinst.htm) |  | [NetNames ▶](func_netnames.htm) |
