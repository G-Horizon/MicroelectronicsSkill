# GetSystemInfo Function

Returns information about the user's system.

### Arguments

No arguments

### Returns

Return type: string array

String array of length 14 as defined by the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Computer name |
| 1 | User log in name |
| 2 | Returns 'Admin' if logged in with administrator privilege otherwise returns 'User'. |
| 3 | Available system RAM in bytes |
| 4 | Operating system class, returns 'WINNT'. |
| 5 | Operating System descriptive name. |
| 6 | Unused |
| 7 | Processor architecture |
| 8 | Operating system version (major and minor) |
| 9 | Operating service pack number |
| 10 | Number processor cores |
| 11 | Number physical processors |
| 12 | Number logical cores |
| 13 | HW capability |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsysteminfo) | | |
| [◄ GetSymbols](func_getsymbols.htm) |  | [GetTempFile ▶](func_gettempfile.htm) |
