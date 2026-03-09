# WAV\_ReadData Function

Read WAV data from file opened using  [WAV\_OpenFile](func_wav_openfile.htm)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real | Yes |  | Handle |
| 2 | Real | Yes |  | Options |

#### Argument 1

Handle obtained from  [WAV\_OpenFile](func_wav_openfile.htm)

#### Argument 2

Options as defined below

|  |  |
| --- | --- |
| 0 | Channel: 0 or 1 |
| 1 | Peak value. Default = 1.0 |

### Returns

Return type: Real array

Data

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wav_readdata) | | |
| [◄ WAV\_OpenFile](func_wav_openfile.htm) |  | [WAV\_WriteFile ▶](func_wav_writefile.htm) |
