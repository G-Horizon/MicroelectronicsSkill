# Locate Function

Function performs a binary search on the input vector (argument 1) for the value specified in argument 2. The input vector  *must be monotonic*  i.e. either always increasing or always reducing. This is always the case for the reference vector (see  [Vector References](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__vectorreferences)  ) of a simulation result. If the input vector is increasing (positive slope) the return value is the index of the value immediately below the search value. If the input vector is decreasing (negative slope) the return value is the index of the value immediately above the search value.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Vector |
| 2 | real | Yes |  | Search value |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_locate) | | |
| [◄ LoadTouchstone](func_loadtouchstone.htm) |  | [log ▶](func_log.htm) |
