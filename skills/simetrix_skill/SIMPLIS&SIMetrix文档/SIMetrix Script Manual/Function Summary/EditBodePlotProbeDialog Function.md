# EditBodePlotProbeDialog Function

UI function for editing Bode plot fixed probes.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Initialisation |

#### Argument 1

Array values used to initialise dialog as shown in the table below.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Gain label |
| 1 | Phase label |
| 2 | Persistence |
| 3 | 'Multiplied by -1' . '0' for normal, '1' for invert |
| 4 | 'Use dB auto limits'. '1' on, '0' off |
| 5 | Minimum limit - dB |
| 6 | Maximum limit - dB |
| 7 | 'Use phase auto limits'. '1' on, '0' off |
| 8 | Minimum limit - phase |
| 9 | Maximum limit - phase |

### Returns

Return type: string array

Returns the values entered in the dialog controls as defined in the table above

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editbodeplotprobedialog) | | |
| [◄ EditAxisDialog](func_editaxisdialog.htm) |  | [EditBodePlotProbeDialog2 ▶](func_editbodeplotprobedialog2.htm) |
