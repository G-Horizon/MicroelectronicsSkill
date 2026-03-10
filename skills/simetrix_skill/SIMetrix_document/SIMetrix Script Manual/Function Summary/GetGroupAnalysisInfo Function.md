# GetGroupAnalysisInfo Function

Retrieves analysis info stored in data groups.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Current group | group name |

#### Argument 1

group name

### Returns

Return type: string array

Returns a string array with 7 elements:

* Analysis step mode
* Analysis type (e.g. tran, ac etc)
* Step type, None, Stepped or Statistical
* Appended group "true" or "false"
* Log sweep mode "true" or "false"
* Start value (e.g. start time)
* End value (e.g. end time)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgroupanalysisinfo) | | |
| [◄ GetGridCurves](func_getgridcurves.htm) |  | [GetGroupFromAnalysisId ▶](func_getgroupfromanalysisid.htm) |
