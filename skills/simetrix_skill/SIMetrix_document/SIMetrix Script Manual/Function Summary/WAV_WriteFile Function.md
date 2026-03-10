# WAV\_WriteFile Function

Write data to a file in WAV format

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path to file |
| 2 | Real array | Yes |  | Configuration |
| 3 | Real | Yes |  | Data for channel 0 (left) |
| 4 | Real | No | None - data saved in single channel format | Data for channel 1 (right) |

#### Argument 1

Path to file

#### Argument 2

Array of up to size 3 providing the configuration of the data as described in the table below

|  |  |
| --- | --- |
| 0 | Bits per sample. Must be 8, 16, 24 or 32 |
| 1 | Peak value. Defaults to 1.0. Input data with this value will be encoded to the maximum integer value. |
| 2 | Sample rate. Defaults to 44100 |

#### Argument 3

Data for channel 0 (left)

#### Argument 4

Data for channel 1 (right)

### Returns

Return type: real

Status code:

|  |  |
| --- | --- |
| 0 | Completed, no errors |
| 1 | Overload, data exceeded peak value |
| 2 | Format not supported |
| 3 | File write failed |
| 4 | File open failed |
| 5 | Exception |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wav_writefile) | | |
| [◄ WAV\_ReadData](func_wav_readdata.htm) |  | [WC ▶](func_wc.htm) |
