# CreateLockFile Function

Creates or removes a lock file for the filename specified. This can be used to synchronise operations between multiple instances of SIMetrix.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | filename |
| 2 | string | Yes |  | operation |

#### Argument 1

Filename to lock. The lock file created will have the same name with the suffix .lck. The lock file itself will be locked for write and other applications will not be able to delete or write to the file.

#### Argument 2

One or two element string array. First element is the operation to be performed. This is either 'lock' or 'unlock'. If 'lock' is specified, an attempt will be made to create a lock file. The operation will fail if the file has already been locked - perhaps by another instance of SIMetrix. If 'unlock' is specified the file will be removed provided that this instance of SIMetrix created the file in the first place.

A second element may be specified and set to 'autodelete'. In this case the file will automatically be unlocked when control is returned to the command line.

### Returns

Return type: string

May be one of the following values:

|  |  |
| --- | --- |
| success | Operation successful |
| failed | Lock failed because the file has already been locked |
| notexist | Attempt made to unlock a file that was not locked by this instance or has not been locked at all |
| locked | File has already been locked by this instance |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_createlockfile) | | |
| [◄ CreateGraphMeasurement](func_creategraphmeasurement.htm) |  | [CreateMutex ▶](func_createmutex.htm) |
