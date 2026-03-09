# Display Command

Displays list of all vectors in specified groups or current group by default. Lists the name, physical type (e.g. voltage, current etc.) data type (real, complex, string, alias) and size of each vector.

```
Display [/file <filename>] [/append <filename>] [/notype] [/notitle] [/type <type>]
```

### Parameters

|  |  |
| --- | --- |
| /append | Append result to  *filename* |
| /file | Output result to  *filename* |
| /list |  |
| /noTitle | Do not display te header showing the group name |
| /notype | Do not list the data type |
| /type | Filter result according to type. type is a list of typenames separated by '|'. Possible values are:   * real * complex * string * alias |

### See Also

* [Expressions](scriptlanguage_expressions.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_display) | | |
| [◄ Discard](com_discard.htm) |  | [DrawArc ▶](com_drawarc.htm) |
