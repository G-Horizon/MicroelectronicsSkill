# Field Function

Function provides bit access to integers. Returns the decimal value of a binary number composed from the binary representation of argument 1 between the bit numbers defined in arguments 2 and 3. E.g.:

```
Field(100, 1, 3) = 2

100 (decimal) = 1100100 (binary)
bits 1 to 3 (from right i.e. least significant) = 010 (binary) = 2
```

Field is useful for cracking the individual bits used for symbol attribute flags. See  [Attribute Flags in the Prop command](com_prop.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | value |
| 2 | real | Yes |  | first bit |
| 3 | real | Yes |  | second bit |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_field) | | |
| [◄ fft](func_fft.htm) |  | [FileToString ▶](func_filetostring.htm) |
