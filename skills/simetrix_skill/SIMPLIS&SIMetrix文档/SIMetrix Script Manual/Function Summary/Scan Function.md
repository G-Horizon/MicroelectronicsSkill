# Scan Function

Splits a character delimited string into its components (known as tokens). Returns result as string array.

Character used as delimiter may be passed as argument 2. If argument 2 omitted delimiter defaults to a semi-colon.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | String to scan |
| 2 | string | No |  | Delimiter |
| 3 | real | No |  | Min number of return values |

#### Argument 1

String to scan.

#### Argument 2

Delimiter. Semi-colon if omitted. Only a single character is permitted. To scan with multiple delimiters, see the function  [Parse](func_parse.htm) .

#### Argument 3

If present, forces the result to be a minimum size. For example, if the input string had two tokens but this argument was set to three, the result would be a string array of length 3 with the third element an empty string. In many applications, this can save testing the length of the return value to determine if an optional token was provided.

### Returns

Return type: string array

Returns tokens as an array of strings. Empty fields are treated as a separate token. E.g. in `'BUF04;buf;;Buffers;;'` the double semi-colon after 'buf' would return an empty entry in the returned array. So:

```
Scan('BUF04;buf;;Buffers;;')
```

would return:

```
[ 'BUF04', 'buf', ", 'Buffers', "]
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_scan) | | |
| [◄ SaveSpecialDialog](func_savespecialdialog.htm) |  | [ScanEscape ▶](func_scanescape.htm) |
