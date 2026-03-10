# ParseParameterString2 Function

Parses a string of name-value pairs and performs some specified action on them. The function can read specified values and return just the values. It can write to specific values and return a modified string. It can also delete specific values.

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

String to parse. This is a list of name-value pairs but may also contain any number of unlabelled values at the start of the string. The number of unlabelled values must be specified in argument 3 (see below). Examples:

Without any unlabelled value:

```
W=1u L=2u AD=3e-12 AS=3e-12
```

With 1 unlabelled value:

```
2.0 DTEMP=25.0
```

The above shows an equals sign separating names and values, but these may be omitted.

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

### Example

This will return the string array ['1u', '2u']:

```
Let str = 'W=1u L=2u AD=3e-12 AS=3e-12'
ParseParameterString(str, ['W', 'L'], 'read')
```

This returns '2.0'

```
Let str = '2.0 DTEMP=25.0'
ParseParameterString(str, '$unlabelled$1', ['read','1'])
```

This will return the modified string: `'W=90n L=120n AD=3e-12 AS=3e-12'`

```
Let str = 'W=1u L=2u AD=3e-12 AS=3e-12'
ParseParameterString(str, ['W','L'], 'write', ['90n', '120n'])
```

This will return the modified string: `'AD=3e-12 AS=3e-12'`

```
Let str = 'W=1u L=2u AD=3e-12 AS=3e-12'
ParseParameterString(str, ['W','L'], 'delete')
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parseparameterstring2) | | |
| [◄ ParseParameterString](func_parseparameterstring.htm) |  | [ParseProbeExpression ▶](func_parseprobeexpression.htm) |
