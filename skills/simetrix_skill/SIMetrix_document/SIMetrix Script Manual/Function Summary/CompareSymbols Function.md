# CompareSymbols Function

Returns 1 if the definitions of the schematic symbols specified are identical. Otherwise returns 0. Two symbol definitions are identical if:

|  |  |
| --- | --- |
| 1. | Their graphics are identical. I.e. all segments, arcs and pin locations are the same |
| 2. | All pin names are the same |
| 3. | All protected properties are identical |

Unprotected properties are not compared.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | symbol name 1 |
| 2 | string | Yes |  | symbol name 2 |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_comparesymbols) | | |
| [◄ CommandStatus](func_commandstatus.htm) |  | [ComposeDigital ▶](func_composedigital.htm) |
