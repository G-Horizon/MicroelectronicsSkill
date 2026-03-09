# DeleteTree Function

Delete an entire directory tree

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
| unknown | Unknown error |

### See Also

* [DeleteTreeProgress](func_deletetreeprogress.htm)

### Example

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_deletetree) | | |
| [◄ DeleteTouchstone](func_deletetouchstone.htm) |  | [DeleteTreeProgress ▶](func_deletetreeprogress.htm) |
