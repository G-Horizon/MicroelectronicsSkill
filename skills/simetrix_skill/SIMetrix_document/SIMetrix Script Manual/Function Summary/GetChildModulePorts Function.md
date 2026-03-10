# GetChildModulePorts Function

Finds information about module ports in the underlying schematic of a hierarchical block. This function was developed as part of the system to allow buses to pass through hierarchies as it can find whether the underlying module port for a hierarchical block is defined for bus connections.

Property name and value must uniquely define an instance.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | Yes |  | Property value |
| 3 | real | No | -1 (use currently selected schematic) | Schematic ID |

#### Argument 1

Usually arg 1 the property name is 'handle'. If arg 1 is an empty string, a single selected instance will be used.

#### Argument 2

The property value

#### Argument 3

Schematic ID as returned by the  [OpenSchematic](func_openschematic.htm)  function. This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

String array of size = 2 times the number of module ports in the underlying schematic. Values arranged in pairs. The first in each pair in the name of the module port and the second value is the bus size. The latter will always be 1 for a non bus module port.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getchildmoduleports) | | |
| [◄ GetAxisUnits](func_getaxisunits.htm) |  | [GetCodecNames ▶](func_getcodecnames.htm) |
