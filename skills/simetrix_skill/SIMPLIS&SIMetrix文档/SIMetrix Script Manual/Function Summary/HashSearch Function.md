# HashSearch Function

Search hash table for an item

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Hash table id as return by |
| 2 | string array | Yes |  | Keys to search |
| 3 | string | No | Empty string | Empty tag |

#### Argument 2

This can be an array provided that the table was not defined as 'multiple' on creation.

### Returns

Return type: string array

For non-multiple tables, return value has the same length as argument 2. Each element maps to the corresponding element in argument 2.

For multiple tables, the return value is a lit of all items that were found matching the search value.

### See Also

* [HashAdd](func_hashadd.htm)
* [HashCreate](func_hashcreate.htm)
* [HashDelete](func_hashdelete.htm)
* [HashKeys](func_hashkeys.htm)
* [HashRemove](func_hashremove.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_hashsearch) | | |
| [◄ HashRemove](func_hashremove.htm) |  | [HasLogSpacing ▶](func_haslogspacing.htm) |
