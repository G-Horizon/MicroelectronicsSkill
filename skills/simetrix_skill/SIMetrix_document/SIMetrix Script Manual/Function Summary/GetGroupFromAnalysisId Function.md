# GetGroupFromAnalysisId Function

Get group name given its analysis ID. The analysis ID can be added to some simulation commands using the ANALYSIS\_ID parameter name. E.g.

.tran 1u 1m ANALYSIS\_ID=tran\_23

This function can be used to retrieve the name of the data group where the results were written. The ANALYSIS\_ID may be used with both SIMPLIS and SIMetrix analysis lines. ANALYSIS\_ID can be used with SIMetrix .TRAN, .DC, .AC, .NOISE and .TF analysis lines and.POP, .AC and .TRAN SIMPLIS analysis lines.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Analysis ID value |
| 2 | Real | No | Main group | Main or DCOP group. (SIMetrix only) |

#### Argument 1

Analysis ID value

#### Argument 2

Boolean: 0: return name of main group, 1: return name of associated DC operating point group

### Returns

Return type: String

Name of data group that carries data for analysis

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgroupfromanalysisid) | | |
| [◄ GetGroupAnalysisInfo](func_getgroupanalysisinfo.htm) |  | [GetGroupInfo ▶](func_getgroupinfo.htm) |
