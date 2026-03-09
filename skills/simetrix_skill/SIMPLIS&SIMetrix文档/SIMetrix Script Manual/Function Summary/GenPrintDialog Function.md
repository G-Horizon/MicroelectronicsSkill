# GenPrintDialog Function

Opens a dialog box used to define print settings

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial settings |
| 2 | string | No |  | Enabled modes |

#### Argument 1

The argument is a string array of length 13 and defines the initial settings of the dialog box as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | |  |  | | --- | --- | | 'area' | "Fit Area" | | 'grid' | "Fixed Grid" | |
| 1 | Schematic scale (entered as a string) |
| 2 | Schematic caption |
| 3 | Graph magnification (entered as a string) |
| 4 | Graph caption |
| 5 | Orientation 'landscape' or 'portrait' |
| 6 | Layout: |  |  | | --- | --- | | '0' | Schematic only | | '1' | Graph only | | '2' | Schematic/Graph | | '3' | Graph/Schematic | |
| 7 | Left margin. The value is entered and returned in units of 0.1mm but will be displayed according to system regional settings. Must be entered as a string. |
| 8 | Top margin. Comments as for left margin. |
| 9 | Right margin. Comments as for left margin. |
| 10 | Bottom margin. Comments as for left margin. |
| 11 | Major grid checked: |  |  | | --- | --- | | 'on' | Checked | | 'off' | Not checked | |
| 12 | Minor grid checked: |  |  | | --- | --- | | 'on' | Checked | | 'off' | Not checked | |

#### Argument 2

Specifies whether schematic mode, graph mode or both are enabled. If omitted the mode is determined by the schematic and graph windows that are open.

To enable schematic mode only, set this argument to 'Schem', to set to graph mode set to 'Graph' and to set to both, set to 'Schem|Graph'.

### Returns

Return type: string array

The function returns a string array with the same format as argument 1 and assigned with the user's settings. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_genprintdialog) | | |
| [◄ GaussTrunc](func_gausstrunc.htm) |  | [GetActualPath ▶](func_getactualpath.htm) |
