# HashCreate Function

Create a hash table.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No | empty | Options |

#### Argument 1

Array of strings - may be any combination of:

|  |  |
| --- | --- |
| 'temporary' | Hash table is temporary and will be automatically deleted when control returns to the command line |
| 'multiple' | Allows multiple entries with the same name to be added to the table |

### Returns

Return type: real

Id of hash table. May be used in any of the hash table function. See list below in 'See Also' section.

### Notes

Hash tables provide a fast method of searching for objects in a large list. Be aware that the number of items in the table needs to be in excess of about 10000 before the hash table offers an worthwhile improvement in performance over a linear search done using the  [Search](func_search.htm)  function. This is because of the function overhead in the script system.

### See Also

* [HashDelete](func_hashdelete.htm)
* [HashSearch](func_hashsearch.htm)
* [HashAdd](func_hashadd.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_hashcreate) | | |
| [◄ HashAdd](func_hashadd.htm) |  | [HashDelete ▶](func_hashdelete.htm) |
