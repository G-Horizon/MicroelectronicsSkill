# SplitPath Function

Splits file system pathname into its component path.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

### Returns

Return type: string array

Return value is string array of length 4.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Drive including ':'. E.g. 'C:' |
| 1 | Directory including prefix and postfix '\'. E.g. "Program Files\ SIMetrix\' |
| 2 | Filename without extension. E.g. 'SIMetrix' |
| 3 | Extension including period. E.g. '.EXE' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_splitpath) | | |
| [◄ SpectrumUniv](func_spectrumuniv.htm) |  | [SplitString ▶](func_splitstring.htm) |
