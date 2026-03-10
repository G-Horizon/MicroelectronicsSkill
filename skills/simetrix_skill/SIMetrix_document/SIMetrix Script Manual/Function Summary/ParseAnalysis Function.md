# ParseAnalysis Function

Opens the choose analysis dialog initialised according to the analysis controls passed as the argument. Returns a new analysis spec that may be passed to a netlist.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Analysis spec |

#### Argument 1

Analysis spec as it would appear in a netlist or the F11 window. E.g. lines beginning with .TRAN, .AC, .DC etc.

### Returns

Return type: string array

String array of length 2. Element 0 contains the new analysis spec. Note individual simulator controls are separated by new line characters.

Element 1 identifies how the user closed the dialog box as defined below:

|  |  |
| --- | --- |
| Run button | '2' |
| Cancel button | '1' |
| OK button | '0' |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_parseanalysis) | | |
| [◄ Parse](func_parse.htm) |  | [ParseEscape ▶](func_parseescape.htm) |
