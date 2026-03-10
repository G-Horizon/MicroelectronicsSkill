# GetSoaResults Function

Returns the SOA results for the most recent simulation.

### Arguments

No arguments

### Returns

Return type: string

Returns an array of strings, each one describing a single SOA failure. Each string is a semi-colon delimited list with fields defined below.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | SOA Label |
| 1 | Start of failure |
| 2 | End of failure |
| 3 | 'under' or 'over'. Defines whether the test fell below a minimum limit or exceeded a maximum limit. |
| 4 | Value of limit that was violated |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsoaresults) | | |
| [◄ GetSoaOverloadResults](func_getsoaoverloadresults.htm) |  | [GetSymbolArcInfo ▶](func_getsymbolarcinfo.htm) |
