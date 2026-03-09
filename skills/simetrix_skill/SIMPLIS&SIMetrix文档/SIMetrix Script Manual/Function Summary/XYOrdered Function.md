# XYOrdered Function

Creates an XY Vector from two separate vectors. An XY Vector is a vector that has a reference (see  [Vector References](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__vectorreferences)  ). The resulting vector will have y values defined by argument 1 and the x values (i.e. its reference) of argument 2.

The values will be arranged in order of their x-values. This function is used to rearrange data for performance plots that are created in non-sequential order. This occurs when using multiple cores to run multi-step analyses.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | y vector |
| 2 | real array | Yes |  | x vector |

### Returns

Return type: real XY array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_xyordered) | | |
| [◄ XY](func_xy.htm) |  | [YCursor ▶](func_ycursor.htm) |
