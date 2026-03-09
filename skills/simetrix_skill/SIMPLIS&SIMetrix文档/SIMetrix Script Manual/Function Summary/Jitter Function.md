# Jitter Function

Calculates clock jitter. Input signal should be a repetitive waveform. The threshold value defines the crossing point. Result will be a vector with length equal to the number of rising edge threshold crossings detected. Each value will be the deviation of the crossing time compared to ideal signal of the same frequency with zero phase jitter.

|  |
| --- |
|  |
| Typical output from Jitter function |

}

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | Real vector | Yes |  | Input data |
| 2 | Real | Yes |  | Threshold |

#### Argument 1

Input data

#### Argument 2

Threshold

### Returns

Return type: Real vector

Jitter values

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_jitter) | | |
| [◄ IsTextEditorModified](func_istexteditormodified.htm) |  | [Join ▶](func_join.htm) |
