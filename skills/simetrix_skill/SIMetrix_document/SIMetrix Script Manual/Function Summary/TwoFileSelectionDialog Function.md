# TwoFileSelectionDialog Function

Opens a dialog to define two file names. While originally intended for file parsing applications, this dialog function has been made general purpose for any application where the user needs to be prompted to select two file names. The dialog has file selection buttons which open a typical File Selection Dialog. The first file is the Input file and must exist on disk when the dialog is closed. The second file is the Output file and doesn't need to exist when the dialog is closed.

|  |
| --- |
|  |
| TwoFileSelectionDialog Configured as the Encryption Dialog |

The first argument defines the two file names and the description combo box text.

The second argument configures the displayed text on the dialog including the caption, title, group box titles and so on.

The third argument configures how the program remembers the input and output file names, description text and checkbox state. Each of these strings is a key in the user's configuration file, allowing the dialog to be used for many different applications with different memories. These remembered values will be displayed in the file and descriptive text combo boxes the next time the dialog is opened. The program remembers the last 10 file and description entries.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No | <<empty>> | Initial files and description combo box text |
| 2 | string array | No | <<empty>> | Dialog Configuration |
| 3 | string array | No | <<empty>> | File history an other configuration |

#### Argument 1

The argument is a string array of length 3 which defines the input file, output file and description text. Additional arguments add GUI elements to the dialog. If the 4th element is passed, the dialog is configured with a set of checkboxes inside the  **Options**  group at the bottom of the dialog. Each additional argument up to the 7th element represents a checkbox. The  **Options**  group of checkboxes was added to SIMetrix/SIMPLIS Version 8.10c.

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Input file name | populates the input file name combo box. | <<empty>> |
| 1 | Output file name | populates the output file name combo box. | <<empty>> |
| 2 | Description text | populates the description combo box. | <<empty>> |
| 3 | Checkbox state | If '1' is passed, checks the checkbox under the Output file name. If not passed or an empty string is passed, the checkbox state is determined by the memory feature. | <<empty>> |
| 4 | First  **Options**  checkbox state | If '1' is passed, checks the first checkbox in the Options Box | <<empty>> |
| 5 | Second  **Options**  checkbox state | If '1' is passed, checks the second checkbox in the Options Box | <<empty>> |
| 6 | Third  **Options**  checkbox state | If '1' is passed, checks the third checkbox in the Options Box | <<empty>> |
| 7 | Fourth  **Options**  checkbox state | If '1' is passed, checks the fourth checkbox in the Options Box | <<empty>> |

#### Argument 2

The argument is a string array of length 13 which defines the dialog text.

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Dialog Box Caption |  | <<empty>> |
| 1 | Box Title |  | <<empty>> |
| 2 | Upper group box title |  | Description |
| 3 | Upper group box text |  | <<empty>> |
| 4 | Input file group box title |  | Input file |
| 5 | Input group box text |  | <<empty>> |
| 6 | Output file group box title |  | Output file |
| 7 | Output group box text |  | <<empty>> |
| 8 | Checkbox text |  | Open output file when complete? |
| 9 | Description group box title |  | File description (optional) |
| 10 | Description group box text |  | <<empty>> |
| 11 | Flag to hide the description groupbox | If set to '1' the description groupbox will be hidden. | '1' |
| 12 | Help context id | For internal use only | <<empty>> |
| 13 | First  **Options**  checkbox text | Create symbol? | <<empty>> |
| 14 | Second  **Options**  checkbox text | Output debug statements to model file? | <<empty>> |
| 15 | Third  **Options**  checkbox text | Create SIMetrix compatible model? | <<empty>> |
| 16 | Fourth  **Options**  checkbox text | Add resistance tolerance to all resistors? | <<empty>> |

#### Argument 3

The argument is a string array of length 8 which defines the memory and file selection dialog filters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Index** | **Purpose** | **Notes** | **Default** |
| 0 | Input file history key name | Any text without spaces, if omitted or empty string, no files will be remembered. | <<empty>> |
| 1 | Output file history key name | Any text without spaces, if omitted or empty string, no files will be remembered. | <<empty>> |
| 2 | Description history key name | Any text without spaces, if omitted or empty string, no description text will be remembered. | <<empty>> |
| 3 | Checkbox history key name | Any text without spaces, if omitted or empty string, no checkbox state will be remembered. Unlike the other memories, this only remembers the last checkbox state. | <<empty>> |
| 4 | Input file type | SIMetrix/SIMPLIS has several internally defined (and user customizable) input file types. |  |  | | --- | --- | | 'Schematic' | Schematic files | | 'Model' | Model files | | 'Netlist' | Netlist files | | 'Graph' | Graph binary files | | 'Script' | Script files | | 'VerilogA' | Verilog-A files | | 'VerilogHDL' | Verilog-HDL files | | 'Data' | Data files | | 'Text' | Text files | | 'AsciiFileEditor' | Schematic ASCII Files | | 'LogicDef' | Logic definition files used with arbitrary logic block | | 'Init' | SIMPLIS Initializaition files. |  An empty string will open the file browser with all files displayed. | <<empty>> |
| 5 | Output file type | Same as the Input file type but for the output file extension | <<empty>> |
| 6 | Output file replacement mode | |  |  | | --- | --- | | 'none' | no replacement is performed on the output file string. | | 'file' | the replacement text supplied in index 7 is applied to the end of the file name before the extension. This occurs when the user selects a file using the file browser selection button. | | 'ext' | the replacement text supplied in index 7 is applied to the end of the file extension. This occurs when the user selects a file using the file browser selection button. | |  |
| 7 | replacement text for index 6. |  |  |
| 8 | First  **Options**  checkbox history key name | Any text without spaces, if omitted or empty string, no checkbox state will be remembered. | <<empty>> |
| 9 | Second  **Options**  checkbox history key name | Any text without spaces, if omitted or empty string, no checkbox state will be remembered. | <<empty>> |
| 10 | Third  **Options**  checkbox history key name | Any text without spaces, if omitted or empty string, no checkbox state will be remembered. | <<empty>> |
| 11 | Fourth  **Options**  checkbox history key name | Any text without spaces, if omitted or empty string, no checkbox state will be remembered. | <<empty>> |

### Returns

Return type: string array

The function returns a string array with a minimum of 4 elements. If the additional  **Options**  checkbox elements are passed on the first argument, the return will be of the same length as the first argument. The return is in this order:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Input file name |
| 1 | Output file name |
| 2 | Description text |
| 3 | Checkbox state |
| 4 | First  **Options**  checkbox state |
| 5 | Second  **Options**  checkbox state |
| 6 | Third  **Options**  checkbox state |
| 7 | Fourth  **Options**  checkbox state |

If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_twofileselectiondialog) | | |
| [◄ Truncate](func_truncate.htm) |  | [UD ▶](func_ud.htm) |
