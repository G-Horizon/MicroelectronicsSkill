# GetKeyDefs Function

Returns details of all key definitions. Note that only keys defined using  [DefKey](com_defkey.htm)  are listed. Keys assigned as accelerators to menu definitions are not included.

### Arguments

No arguments

### Returns

Return type: string array

Returns an array of strings with each element in the array detailing a single key definition. Each definition is a semi-colon delimited string with three fields:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Name of key as entered in  [DefKey](com_defkey.htm) |
| 1 | Command executed by key press |
| 2 | Flag value. This is usually 4, but will be 5 for 'immediate' keys. |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getkeydefs) | | |
| [◄ GetInternalDeviceName](func_getinternaldevicename.htm) |  | [GetKnownFolderPath ▶](func_getknownfolderpath.htm) |
