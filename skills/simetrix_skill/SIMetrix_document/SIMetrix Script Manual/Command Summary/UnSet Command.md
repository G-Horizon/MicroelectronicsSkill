# UnSet Command

Deletes specified option.

```
UnSet name [ name ...]
```

### Parameters

|  |  |
| --- | --- |
| /temp | Deletes only temporarily. Will revert to original value once control returns to the command line. |

### Notes

Some Option values are  *internal* . This means that they always have a value. If such an option is UnSet, it will be restored to its default value and not deleted.

### See Also

* [Set](com_set.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_unset) | | |
| [◄ Unselect](com_unselect.htm) |  | [Unzip ▶](com_unzip.htm) |
