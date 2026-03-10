# EditWaveformDialog Function

Opens a dialog designed for editing a time domain waveform. This function has been superceeded by  [EditWaveformStrDialog](func_editwaveformstrdialog.htm)  but is retained to support old designs.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Time/frequency initial values |
| 2 | real | No |  | Vertical initial values |
| 3 | string array | Yes |  | options |

#### Argument 1

Initial values for the controls in the Time/Frequency group box. Up to 10 elements defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Integer from 0 to 8, specifies wave shape as follows: |  |  | | --- | --- | | 0 | Square | | 1 | Triangle | | 2 | Sawtooth | | 3 | Sine | | 4 | Cosine | | 5 | Pulse | | 6 | One pulse | | 7 | One pulse (exp) | | 8 | Step | |
| 1 | Delay |
| 2 | Rise time |
| 3 | Fall time |
| 4 | Width |
| 5 | Period |
| 6 | Damping |
| 7 | 0: Use Delay, 1: Use Phase |
| 8 | Frequency |
| 9 | Duty cycle |

#### Argument 2

Initial values for the controls in the Vertical group box. Up to 5 elements defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Initial |
| 1 | Pulse |
| 2 | Off until delay |
| 3 | Offset |
| 4 | Amplitude |

#### Argument 3

String array up to length 2 which may specify either of these options

* Simulator mode - either 'SIMetrix' or 'SIMPLIS'
* Initial pulse mode - set to 'initialpulse'

### Returns

Return type: string array

String array with 15 elements. Elements 0 - 9 as for argument 1, elements 10-14 as for argument 2.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editwaveformdialog) | | |
| [◄ EditTimer](func_edittimer.htm) |  | [EditWaveformStrDialog ▶](func_editwaveformstrdialog.htm) |
