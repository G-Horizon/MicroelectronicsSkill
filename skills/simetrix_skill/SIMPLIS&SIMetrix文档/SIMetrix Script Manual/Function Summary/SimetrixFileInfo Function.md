# SimetrixFileInfo Function

Returns information about a SIMetrix file. Currently this function will only return information about version 4.1 or later schematic files.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  |  |

#### Argument 1

File name

### Returns

Return type: string array

Return value will be an array of length 3. The first element will currently be one of the values, 'Schematic', 'Unknown' or 'CantOpen'. The second element reports the file format version. The third element will be one of:

|  |  |
| --- | --- |
| **Value** | **Description** |
| 'Schematic' | File is SIMetrix component or schematic file and contains just a schematic. (4.1 or later) |
| 'Symbol' | File is a SIMetrix component file and contains only the symbol part of the component |
| 'Symbol|Schematic' | File is a SIMetrix component file and contains both the symbol part and the schematic part of the component |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_simetrixfileinfo) | | |
| [◄ sign](func_sign.htm) |  | [SIMPLISRunStatus ▶](func_simplisrunstatus.htm) |
