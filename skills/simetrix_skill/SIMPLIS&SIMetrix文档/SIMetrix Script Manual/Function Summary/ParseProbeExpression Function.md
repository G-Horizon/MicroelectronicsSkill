# ParseProbeExpression Function

Parses an expression used arbitrary fixed probes. The expression uses the access functions V() and I() to denote node voltages and source currents respectively. The function provides a list of the access nodes and sources used in the expression. These are used to create an abritrary probe symbol.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Expression |

#### Argument 1

Expression to be parsed using V(node) and I(source) access functions

### Returns

Return type: string array

|  |  |
| --- | --- |
| **Index** | **Description** |
| } |  |
| 0 | Expression converted to a form useable by a fixed probe |
| 1 | Number of distinct nodes = nn |
| 2 | Number of distinct sources = ns |
| 3 to 3+nn-1 | Node names used |
| 3+nn to 3+nn+ns-1 | Source names used |

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 |  |

### See Also

* [SubstProbeExpression](func_substprobeexpression.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parseprobeexpression) | | |
| [◄ ParseParameterString2](func_parseparameterstring2.htm) |  | [ParseSIMPLISInit ▶](func_parsesimplisinit.htm) |
