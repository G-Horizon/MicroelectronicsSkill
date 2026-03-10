# DeleteTreeProgress Function

Delete an entire directory tree, while showing a progress box

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | directory to delete |

### Returns

Single string value providing status of operation as follows

|  |  |
| --- | --- |
| **Value** | **Description** |
| success | Operation successful |
| failed | Operation failed |
| incomplete | Operation partially completed: some files were not deleted |
| sourcenotexist | Source does not exist |
| aborted | Operation aborted byuser |
| unknown | Unknown error |

### See Also

* [DeleteTree](func_deletetree.htm)

### Example

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_deletetreeprogress) | | |
| [◄ DeleteTree](func_deletetree.htm) |  | [DelSchemProp ▶](func_delschemprop.htm) |
