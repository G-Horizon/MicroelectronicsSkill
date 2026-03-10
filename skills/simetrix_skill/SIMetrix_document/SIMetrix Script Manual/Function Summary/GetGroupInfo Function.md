# GetGroupInfo Function

Returns information about a group.

For more information on groups, see  [Groups](scriptlanguage_accessingsimulationdata.htm#scriptlanguage_accessingsimulationdata__groups) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Group name |

#### Argument 1

Group name for which information is required. Enter " to obtain information on the current group.

### Returns

Return type: string array

String array of length 3 as described in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Source file. This is the path name for the file that contains the data for the group. If the groups data is stored in RAM, this element will hold an empty string |
| 1 | Group title. For groups created by a simulation (which is to say virtually all groups) this is obtained from the netlist title |
| 2 | Empty - reserved for future use |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getgroupinfo) | | |
| [◄ GetGroupFromAnalysisId](func_getgroupfromanalysisid.htm) |  | [GetGroupStepParameter ▶](func_getgroupstepparameter.htm) |
