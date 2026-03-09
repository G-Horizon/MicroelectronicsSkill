# Show Command

Displays the value of an expression.

```
Show 
        [/file <filename>] [/append <filename>] [/noindex] [/plain] [/noHeader] [/clipboard] [/names <names>]
        [/force] [/width <width>] [/lock] [/detail] [/unix] expression [expression ...]
```

### Parameters

|  |  |
| --- | --- |
| /append | As `/file` except that file is appended if it already exists. |
| /clipboard | If specified, the result is copied to the windows clipboard. |
| /csv | If specified, outputs result to  *filename*  in CSV format. |
| /detail |  |
| /detailxml |  |
| /file | If specified, outputs result to  *filename* . The values are output in a format compatible with  [OpenGroup](com_opengroup.htm)  and the `/text` switch. |
| /force | File specified by `/file` will be unconditionally overwritten if it exists. |
| /interactive |  |
| /list |  |
| /lock | If specified with  */file*  , a lock file will be created while the write operation is being performed. The file will have the extension.lck. This can be used to synchronise data transfers with other applications. The file will be locked for write operations. |
| /names | Semicolon delimited list of column labels. If specified, each vector column will be labelled by the corresponding name given in  *names* . Otherwise, vector name is used as label. |
| /noHeader |  |
| /noindex | If the vector has no reference, the index value for each element is output if this switch is  *not*  specified. |
| /plain | If specified, no index (as `/noindex` ), and no header (as `/noHeader` ) will be output. In addition, string values will be output less the quotation marks. |
| /unix |  |
| /width | Page width in columns. |
| expression | Expression to be displayed. If expression is an array, all values will be displayed. |

### Notes

To enter multiple expressions, separate each with a comma. The display of arrays with a very large number of elements (>500) can take a long time. For large arrays it is recommended that the /file or /clipboard switch is used to output the results to a file or the windows clipboard respectively. The data can then be examined with a text editor or spreadsheet program. The results will be tabulated if all vectors are compatible that is have the same xvalues. If the any vectors listed are not compatible, each vector's data will be listed separately. The precision of numeric values can be controlled using the "Precision" option setting. Use the command: `Set precision = value`. This sets the precision in terms of the column width.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_show) | | |
| [◄ ShellOld](com_shellold.htm) |  | [ShowCurve ▶](com_showcurve.htm) |
