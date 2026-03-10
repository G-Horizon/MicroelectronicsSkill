# HashAdd Function

Add items to a hash table. If the table is not defined as 'multiple', this function will edit the values of items that are already present. If the table is defined as 'multiple' new values for the item will be added.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Hash table id as return by |
| 2 | string | Yes |  | List of keys |
| 3 | string | Yes |  | List of values corresponding to the keys in argument 2 |

### Returns

Return type: real

1.0 if hash table exists otherwise 0.0

### See Also

* [HashCreate](func_hashcreate.htm)
* [HashDelete](func_hashdelete.htm)
* [HashKeys](func_hashkeys.htm)
* [HashRemove](func_hashremove.htm)
* [HashSearch](func_hashsearch.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_hashadd) | | |
| [◄ Hash](func_hash.htm) |  | [HashCreate ▶](func_hashcreate.htm) |
