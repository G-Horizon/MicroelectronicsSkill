# avg Function

Calculates the average of the argument with respect to its reference as defined by:

\[ y = \int\_{0}^{t}\frac{x}{t}dt \]

where ???MATH???x???MATH??? is the argument and ???MATH???t???MATH??? is the reference of ???MATH???x???MATH???. See  [Vector References](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__vectorreferences)  for details.

The function uses simple trapezoidal integration.

An error will occur if the argument supplied has no reference.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | vector |

### Returns

Return type: real array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_avg) | | |
| [◄ atanh](func_atanh.htm) |  | [BoolSelect ▶](func_boolselect.htm) |
