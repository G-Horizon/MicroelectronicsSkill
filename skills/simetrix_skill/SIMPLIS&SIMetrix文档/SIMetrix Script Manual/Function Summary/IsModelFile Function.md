# IsModelFile Function

Returns 1 if the specified file contains .MODEL, .SUBCKT, .PARAM or .ALIAS definitions. Otherwise returns 0. The function will unconditionally return 0 if the file has any of the following extensions:

.EXE, .COM, .BAT, .CMD, .SXSCH, .SXDAT, .SXGPH, .SXSLB, .SXCMP

This will be overridden if the second argument is set to 'AllExt'.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path of file |
| 2 | string | No |  | Options |

### Returns

Return type: real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_ismodelfile) | | |
| [◄ IsImageFile](func_isimagefile.htm) |  | [IsNum ▶](func_isnum.htm) |
