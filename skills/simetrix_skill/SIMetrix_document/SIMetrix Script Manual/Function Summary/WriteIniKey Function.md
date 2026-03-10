# WriteIniKey Function

Writes a value to an 'INI' file. See the function  [ReadIniKey](func_readinikey.htm)  for more information on INI files.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File |
| 2 | string | Yes |  | Section |
| 3 | string | Yes |  | Key |
| 4 | string | No | Empty string | Value |

#### Argument 1

File name. You should always supply a full path for this argument. If you supply just a file name, the system will assume that the file is in the WINDOWS directory. This behaviour may be changed in future versions. For maximum future compatibility, always use a full path.

#### Argument 2

Section name.

#### Argument 3

Key name.

#### Argument 4

Key value

### Returns

Return type: real

Returns 1 if function successful. Otherwise returns 0.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_writeinikey) | | |
| [◄ WriteF11Options](func_writef11options.htm) |  | [WriteRawData ▶](func_writerawdata.htm) |
