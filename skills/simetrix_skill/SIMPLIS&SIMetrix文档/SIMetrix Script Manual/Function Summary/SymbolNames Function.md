# SymbolNames Function

Returns symbol names of schematic instances.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |
| 2 | string | No | Use selected | Property name |
| 3 | string | No | Use all with property name in arg 2 | Property value |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

#### Argument 2

Along with argument 3, if present these arguments identify the instances to be examined. If only argument 2 is specified then all instances on the specified schematic that possess that property will be used. If argument 3 is also present then the instance name and value must match argument 2 and 3 respectively. If neither are present the selected instances will be used.

### Returns

Return type: string array

String array containing the symbol names for the instances identified by this functions arguments.

Note that this function complements  [PropValues2](func_propvalues2.htm)  and  [PropFlags2](func_propflags2.htm)  , and will return the same number of values and in the same order as those function given the same arguments.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_symbolnames) | | |
| [◄ SymbolName](func_symbolname.htm) |  | [SymbolPinOrder ▶](func_symbolpinorder.htm) |
