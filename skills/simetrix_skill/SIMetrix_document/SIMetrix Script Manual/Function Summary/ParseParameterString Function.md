# ParseParameterString Function

Legacy function. Use  [ParseParameterString2](func_parseparameterstring2.htm)  for new code. Parses a string of name-value pairs and performs some specified action on them. The function can read specified values and return just the values. It can write to specific values and return a modified string. It can also delete specific values.

ParseParameterString detects parameter names by searching for known names (as supplied in argument 2) in the supplied string in argument 1. This means that a parameter value that matches a known parameter name may be incorrectly identified as a name. The  [ParseParameterString2](func_parseparameterstring2.htm)  function identifies parameter names by their position in the input string and does not suffer from this problem. However  [ParseParameterString2](func_parseparameterstring2.htm)  is not compatible in all cases and so ParseParameterString is retained to keep old code working correctly.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to parse |
| 2 | string | Yes |  | Parameter names to process |
| 3 | string | Yes |  | action |
| 4 | string | No |  | Write value |
| 5 | string | No |  | Options |

#### Argument 1

String to parse. This is a list of name-value pairs but may also contain any number of unlabelled values at the start of the string. The number of unlabelled values must be specified in argument 3 (see below).

#### Argument 2

String array listing the names to be processed. If reading (see below) only the values of the names supplied here will be returned. If writing, the names listed in this argument will be edited with new values supplied in argument 4. If deleting, these names will be removed.

Unlabelled parameters may be referenced using the special name '$unlabelled$' followed by the position. I.e. the first unlabelled parameter is position 1, the second 2 and so on. So '$unlabelled$1' refers to the first unlabelled parameter.

#### Argument 3

1 or 2 element string array. The first element is the action to be performed. The second element is the number of unlabelled parameters that are expected in the input string. This is zero if omitted.

#### Argument 4

Values to write. These have a 1:1 correspondence with the parameter names in argument 2.

#### Argument 5

If set to 'allowquoted', the function will treat any items enclosed in single or double quotation marks as a single token even if there are spaces within.

### Returns

Return type: string array or scalar

If reading, the return value is an array of strings holding the values of the specified parameters. Otherwise it the input string appropriately modified according to the defined action.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parseparameterstring) | | |
| [◄ ParseLaplace](func_parselaplace.htm) |  | [ParseParameterString2 ▶](func_parseparameterstring2.htm) |
