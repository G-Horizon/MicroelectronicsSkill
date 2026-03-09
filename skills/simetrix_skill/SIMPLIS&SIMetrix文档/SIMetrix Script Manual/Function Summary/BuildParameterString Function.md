# BuildParameterString Function

Constructs a string of name=value pairs from two arrays containing the names and values separately.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Parameter names |
| 2 | string array | Yes |  | Parameter values |
| 3 | string | No | space and tab | Special characters |

#### Argument 1

Array of parameter names

#### Argument 2

Array of parameter values

#### Argument 3

Special characters. Any parameter value containing one or more of the characters specified here will be enclosed in double quotation marks.

### Returns

Return type: string

String in form 'name=value name=value ...'

### See Also

* [ParseParameterString](func_parseparameterstring.htm)
* [ParseParameterString2](func_parseparameterstring2.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_buildparameterstring) | | |
| [◄ BuildMclogHTML](func_buildmcloghtml.htm) |  | [BuildSensitivityCsv ▶](func_buildsensitivitycsv.htm) |
