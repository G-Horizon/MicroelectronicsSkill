# GetSimetrixFile Function

Function opens a dialog box to allow the user to select a file. Returns the full path name to the selected file or an empty string if cancelled.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File type |
| 2 | string array | No | <<empty>> | Options |
| 3 | string | No | <<empty>> | Initial file |

#### Argument 1

String to define one of the standard SIMetrix file types. This determines the files that will be displayed. Possible values are:

|  |  |
| --- | --- |
| 'Schematic' | Schematic files |
| 'Data' | Data files |
| 'Text' | Text files |
| 'LogicDef' | Logic definition files as used by the arbitrary logic block |
| 'Script' | Script files |
| 'Model' | Model files |
| 'Catalog' | Catalog files |
| 'Graph' | Graph files |
| 'Component' | Schematic component files |
| 'Symbol' | Symbol library files |
| 'Snapshot' | Snapshot files |
| 'Netlist' | Netlist files |
| 'VerilogA' | Verilog-A files |
| 'VerilogHDL' | Verilog-HDL files |
| 'AsciiFileEditor' | Schematic ASCII files |
| 'AnalysisData' | Monte Carlo, Sensitivity and Worst-case analysis files |
| 'Optimiser' | Optimiser files |

The type selected determines the files to be displayed controlled by their extension. The extension associated with each file type can be set with the options dialog box opened by menu **File** > **Options** > **General...**

You can combine multiple file types delimited by '&'. For example "Netlist & Model" will select both netlist and model file types.

#### Argument 2

String array that specifies a number of options. Any or all of the following may be included:

|  |  |
| --- | --- |
| 'ChangeDir' | If present, the current working directory will change to that containing the file selected by the user |
| 'Open' | If present a "File Open" box will be displayed other wise a "Save As" box will be displayed. |
| 'NotExist' | If used with 'Open', the file is not required to already exist to be accepted |
| 'All' | If present an "All files" entry will be added to the "Files of type" list |

#### Argument 3

Initial file selection.

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getsimetrixfile) | | |
| [◄ GetSimConfigLoc](func_getsimconfigloc.htm) |  | [GetSIMPLISExitCode ▶](func_getsimplisexitcode.htm) |
