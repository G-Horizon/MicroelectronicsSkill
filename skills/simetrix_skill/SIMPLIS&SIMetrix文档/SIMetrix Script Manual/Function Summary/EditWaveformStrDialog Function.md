# EditWaveformStrDialog Function

Opens a dialog box designed for editing a time domain waveform. To see an example of this dialog box, place a Waveform Generator on a schematic, select it then press F7.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Time/frequency initial values |
| 2 | string array | No |  | Vertical initial values |
| 3 | string array | No |  | Options |

#### Argument 1

Initial values for the controls in the Time/Frequency group box. Values must be entered as strings and may be in the form of expressions enclosed with curly braces as well as literal constants. Up to 10 elements defined as follows:

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

Initial values for the controls in the Vertical group box. Values must be entered as strings and may be in the form of expressions enclosed with curly braces as well as literal constants. Up to 5 elements defined as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Initial |
| 1 | Pulse |
| 2 | Off until delay |
| 3 | Offset |
| 4 | Amplitude |

#### Argument 3

String array which may contain any combination of:

|  |  |
| --- | --- |
| **Name** | **Description** |
| simplis | Select SIMPLIS mode. This shows the "Source idle during POP and AC analyses" check box |
| initialpulse | If true, means read the values for initial and pulse and use these to derive values for offset and amplitude. If false, read the values for offset and amplitude and use these to derive values for initial and pulse. This is set unconditionally if arg1 is missing or has size < 5. Otherwise it is set by a flag in arg2 if present otherwise it is false. |

### Returns

Return type: string array

String array with 16 elements. Elements 0 - 9 as for argument 1, elements 10-14 as for argument 2. Element returns the state of the "Source idle during POP and AC analyses" check box.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editwaveformstrdialog) | | |
| [◄ EditWaveformDialog](func_editwaveformdialog.htm) |  | [ElementProps ▶](func_elementprops.htm) |
