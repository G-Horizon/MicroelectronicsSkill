# VectorsInGroup Function

Returns the names or optionally the physical type of all vectors in the specified group. Argument 2 is a string array that may contain values of 'PhysType' and/or 'RealOnly'. If 'PhysType' is present the physical type (e.g. 'voltage', 'current', 'time' etc.) of the vectors will be returned otherwise the function will return their names. If 'RealOnly' is present, only values of type 'Real' will be returned. Complex values, string values and aliases values will be excluded.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | Current group | group name |
| 2 | string array | No |  | Options |

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_vectorsingroup) | | |
| [◄ vector](func_vector.htm) |  | [VersionInfo ▶](func_versioninfo.htm) |
