# ParseLaplace Function

Parses a Laplace expression to return array of denominator and numerator coefficients

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Laplace expression |

#### Argument 1

Expression in s-variable defining a Laplace transfer function. Refer to the User's Manual -> Parts -> Generic Parts -> Laplace Transfer Function for a detailed explanation .

### Returns

Return type: real array

real array as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Status code - 0 means success. Use \mbox{  [GetLaplaceErrorMessage](func_getlaplaceerrormessage.htm)  } to convert this to an error messgae |
| 1 | denominator order |
| 2 | numerator order |
| 3 to (3+den order) | denominator coefficients - lowest order first |
| 3+den order+1 to \newline 3+den order+1+num order | numerator coefficients - lowest order first |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parselaplace) | | |
| [◄ ParseEscape](func_parseescape.htm) |  | [ParseParameterString ▶](func_parseparameterstring.htm) |
