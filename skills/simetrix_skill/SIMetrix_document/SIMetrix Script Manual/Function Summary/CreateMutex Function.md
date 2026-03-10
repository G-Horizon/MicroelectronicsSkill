# CreateMutex Function

Creates a system named mutex. This can be used to synchronise with other applications

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Name of mutex |

#### Argument 1

Name of mutex. This must have fewer than 260 characters which may use international character sets. The name is global and can be opened using the Windows API function CreateMutex in other processes. The mutex can be released with a call to  [DestroyMutex](func_destroymutex.htm)  and will also be automatically released when the application closes.

If CreateMutex is called for a mutex that has already been created by a former call to CreateMutex, the id of the existing mutex will be returned.

Note that mutex names are  **case sensitive**  unlike most other function in SIMetrix.

### Returns

Return type: Real

Integer id > 0 identifying the mutex which can be used in a call to  [DestroyMutex](func_destroymutex.htm) . Note this is unrelated to the system handle. The function will return empty if the mutex cannot be created

### See Also

* [DestroyMutex](func_destroymutex.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_createmutex) | | |
| [◄ CreateLockFile](func_createlockfile.htm) |  | [CreateNewTitleBlockDialog ▶](func_createnewtitleblockdialog.htm) |
