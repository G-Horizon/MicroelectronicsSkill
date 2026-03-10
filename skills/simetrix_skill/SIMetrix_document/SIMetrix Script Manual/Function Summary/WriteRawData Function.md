# WriteRawData Function

Writes data to the specified file in a SPICE3 raw file compatible format. See the built in script write\_raw\_file for an application example. This can be found on the install CD.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real/complex array | Yes |  | data |
| 2 | string | Yes |  | File name |
| 3 | string | No |  | Options |
| 4 | string | No | '%d' | Format of index display |

### Returns

Return type: string

The function returns a single string according to the success or otherwise of the operation. Possible values are: 'success' , 'nodata' and 'fileopenfail'.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writerawdata) | | |
| [◄ WriteIniKey](func_writeinikey.htm) |  | [WriteRegSetting ▶](func_writeregsetting.htm) |
