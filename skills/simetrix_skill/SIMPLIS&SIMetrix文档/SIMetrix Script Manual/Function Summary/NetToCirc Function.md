# NetToCirc Function

Converts a netlist or subcircuit model to a schematic and returns information about the conversion

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Input model name or netlist path |
| 2 | String array | No |  | Symbol pin names (model mode) |
| 3 | String array | No | ['model', 'default'] | Options |
| 4 | String | Yes |  | Model-symbol association table |

#### Argument 1

In netlist mode, the path to the netlist. In model mode, the name of the model

#### Argument 2

Used in model mode only. Sets the names of the module ports in the top level in order to match the pin names of the schematic symbol. If empty or not provided, the module port names will follow the subcircuit definition

#### Argument 3

Configures the conversion. A string array with one element from each row in the following table

|  |  |
| --- | --- |
| Conversion mode | 'netlist' or 'model' |
| Output format | 'xml', 'ascii' or 'default' |

### Returns

Return type: String array

An array with three elements as defined in the following table

|  |  |
| --- | --- |
| Status of conversion: 'Ok', 'Warning' or 'Error' |  |
| Path to top level schematic |  |
| Conversion report in HTML format |  |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_nettocirc) | | |
| [◄ NetNames](func_netnames.htm) |  | [NetWires ▶](func_netwires.htm) |
