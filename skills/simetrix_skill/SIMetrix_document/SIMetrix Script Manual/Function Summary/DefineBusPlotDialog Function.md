# DefineBusPlotDialog Function

Opens a dialog box to allow the user to plot a bus.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Initial values |
| 2 | string | No |  | options |

#### Argument 1

String array of length up to 9. Elements defined in the following table:

|  |  |  |
| --- | --- | --- |
| **Index** | **Description** | **Default** |
| 0 | Bus name | " |
| 1 | Bus start index | 0 |
| 2 | Bus end index | 0 |
| 3 | Display type: |  |  | | --- | --- | | '0' | Decimal | | '1' | Hexadecimal | | '2' | Analog waveform | | '3' | Binary | | '0' |
| 4 | Hold invalid: |  |  | | --- | --- | | 'TRUE' | Hold invalid ON | | 'FALSE' | Hold invalid off | | 'FALSE' |
| 5 | Scale factor | '1.0' |
| 6 | Offset '0.0' |  |
| 7 | Units |  |
| 8 | Items used to load 'Units' combo box separated by '|' |  |
| 9 | Analog threshold lower |  |
| 10 | Analog threshold upper |  |
| 11 | Axis type: |  |  | | --- | --- | | '0' | Auto select | | '1' | Use separate Y-axis | | '2' | Use separate grid | | '3' | Digital | |  |
| 12 | Axis name |  |
| 13 | Use separate graph? |  |  | | --- | --- | | 0 | yes | | 1 | no | |  |
| 14 | Graph name |  |

#### Argument 2

Options. Currently just one. If set to 'noProbeOptions', the Probe Options sheet will be hidden.

### Returns

Return type: string array

String array with the same length as the input. Each field holds the value selected by the user. Note that field index 8 does not currently output a meaningful value and should be ignored.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_definebusplotdialog) | | |
| [◄ DefineArbSourceDialog](func_definearbsourcedialog.htm) |  | [DefineCounterDialog ▶](func_definecounterdialog.htm) |
