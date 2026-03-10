# SelectRows Function

Accepts an array of character delimited strings and returns an array containing a selection containing the test string at specified field. This function was developed for the parts browser mechanism but is general purpose in nature.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Input data |
| 2 | string | Yes |  | Test string |
| 3 | string | No | 0 | Field number |
| 4 | string | No | ';' | Delimiter |

### Returns

Return type: string array

### Example

Data input (arg 1):

```
HA-5002/HA;buf;;Buffers;;
HA-5033/HA;buf;;Buffers;;
HA5002;buf;;Buffers;;
HA5033;buf;;Buffers;;
LM6121/NS;buf;;Buffers;;1,2,4,3
MAX4178;buf_5;;Buffers;;
MAX4278;buf_5;;Buffers;;
MAX496;buf_5;;Buffers;;
```

Test string (arg 2)

```
'buf'
```

Field number (arg 3)

```
1
```

Returns:

```
HA-5002/HA;buf;;Buffers;;
HA-5033/HA;buf;;Buffers;;
HA5002;buf;;Buffers;;
HA5033;buf;;Buffers;;
LM6121/NS;buf;;Buffers;;1,2,4,3
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectrows) | | |
| [◄ SelectFontDialog](func_selectfontdialog.htm) |  | [SelectSIMPLISAnalysis ▶](func_selectsimplisanalysis.htm) |
