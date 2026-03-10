# GetPlatformFeatures Function

Returns information on availability of certain features that are platform dependent.

### Arguments

No arguments

### Returns

Return type: string array

Currently a string of length 4 defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Is the function  [ShellExecute](func_shellexecute.htm)  implemented? 'true' or 'false' |
| 1 | Obsolete |
| 2 | Is 'VersionStamp' function implemented. 'true' or 'false' |
| 3 | Is context sensitive help implemented. 'true' or 'false' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getplatformfeatures) | | |
| [◄ GetPath](func_getpath.htm) |  | [GetPrinterInfo ▶](func_getprinterinfo.htm) |
