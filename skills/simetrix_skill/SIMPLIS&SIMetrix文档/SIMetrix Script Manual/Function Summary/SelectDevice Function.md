# SelectDevice Function

Opens parts browser dialog.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Parts data |
| 2 | string | No | No device selected | Selected device |
| 3 | string array | No |  | User installed models |

#### Argument 1

Argument is array of strings containing parts database. This is usually read from the file 'OUT.CAT' in the script directory. The format for this file is described in  [User's Manual/Device Library and Parts Management/Advanced Topics/Catalog Files](../../user_manual/topics/devicelibraryandpartsmanagement_partsmanagement_advancedtopics.htm)  Chapter of the  *User's Manual* . Each line contains up to 8 semi-colon delimited fields. Only the first field (part number) and the fourth field (category) are displayed to the user but the values of any other field will be returned in the result.

#### Argument 2

If supplied and is the part number of a device included in arg 1, that device will be selected.

#### Argument 3

contains a list of model names that will appear in the '\* User Models \*' category. These will also appear in the '\* Recently Installed Models \*' category if the model was installed within the last 30 days or other duration defined by the NewModelLifetime option setting.

### Returns

Return type: string array

Return value is a string array of length 8 containing the value of each field of the selected device or an empty vector if cancelled.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_selectdevice) | | |
| [◄ SelectCount](func_selectcount.htm) |  | [SelectDialog ▶](func_selectdialog.htm) |
