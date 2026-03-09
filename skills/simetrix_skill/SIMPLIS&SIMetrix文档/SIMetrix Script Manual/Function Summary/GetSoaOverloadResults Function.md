# GetSoaOverloadResults Function

Returns the overload factor for each SOA definition.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Options |

#### Argument 1

String array consisting of one or both of the values: 'ignorewindow' or 'derated'. If 'ignorewindow' is specified, then the function will not return data for SOA specifications that include a window. If 'derated' is included, the values returned allow for any derating factor. For example, if the limit is 40V with 80% derating and the maximum value reached was 38V, the overload factor with 'derated' specificed will be ???MATH???\frac{38}{40\times0.8} = 1.1875???MATH???. Without 'derated' specified, the overload factor would be ???MATH???\frac{38}{40} = 0.95???MATH???.

### Returns

Return type: real array

Returns an array of reals defining the overload factor for each SOA definition. Each element in the array corresponds to the elements returned by the function  [GetSoaDefinitions](func_getsoadefinitions.htm) .

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsoaoverloadresults) | | |
| [◄ GetSoaMaxMinResults](func_getsoamaxminresults.htm) |  | [GetSoaResults ▶](func_getsoaresults.htm) |
