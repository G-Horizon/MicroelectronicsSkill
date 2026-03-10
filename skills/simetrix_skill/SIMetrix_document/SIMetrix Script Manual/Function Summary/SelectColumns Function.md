# SelectColumns Function

Accepts an array of character delimited strings and returns an array containing only the specified field. This function was developed for the parts browser mechanism but is general purpose in nature.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Input data |
| 2 | real | Yes |  | Field number |
| 3 | string | No | ';' | Delimiter |

### Returns

Return type: string array

### Example

Data input (arg 1):

```
BUF600X1;Buf;;Buffers;;2,1,4,3
BUF600X2;Buf;;Buffers;;2,1,4,3
BUF601X1;Buf;;Buffers;;2,1,4,3
BUF601X2;Buf;;Buffers;;2,1,4,3
```

Field number (arg2)

```
0
```

Returns:

```
BUF600X1
BUF600X2
BUF601X1
BUF601X2
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectcolumns) | | |
| [◄ SelectColourDialog](func_selectcolourdialog.htm) |  | [SelectCount ▶](func_selectcount.htm) |
