# CopyTree Function

Copy a directory tree. Requires target to be empty

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Source directory |
| 2 | string | Yes |  | Target directory |

### Returns

Return type: string

Single string value providing status of operation as follows

|  |  |
| --- | --- |
| **Value** | **Description** |
| success | Operation successful |
| failed | Operation failed |
| incomplete | Operation partially completed: some files were not copied |
| notempty | Target already exists and was not empty |
| sourcenotexist | Source does not exist |
| unknown | Unknown error |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_copytree) | | |
| [◄ CopyDivisionData](func_copydivisiondata.htm) |  | [CopyURL ▶](func_copyurl.htm) |
