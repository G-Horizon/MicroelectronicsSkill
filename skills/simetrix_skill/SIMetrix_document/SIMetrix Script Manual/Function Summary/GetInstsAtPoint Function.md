# GetInstsAtPoint Function

Functions finds the instances with pins at a specified point and returns a string array to identify them. The return value is a string array of length 2 times the number of pins at the specified point. The first value in each pair is the value of the property identified in argument 2. The second value is the pin number (also referred to as the  *netlist order*  ).

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Instance pin location |
| 2 | string | Yes |  | Property name |

#### Argument 1

specifies the pin location and is the value returned from the  [GetInstancePinLocs](func_getinstancepinlocs.htm)  with the 'absolute' option specified.

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinstsatpoint) | | |
| [◄ GetInstancePinLocs](func_getinstancepinlocs.htm) |  | [GetInternalDeviceName ▶](func_getinternaldevicename.htm) |
