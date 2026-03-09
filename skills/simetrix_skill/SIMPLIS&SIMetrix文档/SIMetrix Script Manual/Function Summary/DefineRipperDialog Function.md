# DefineRipperDialog Function

Opens a dialog box to define a schematic bus ripper.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | initial settings |
| 2 | string array | Yes |  | list of style box items |

#### Argument 1

This argument is a string array of length 4 and defines the initial settings for the box controls as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Bus name |
| 1 | Start index (entered as a string) |
| 2 | End index (entered as a string) |
| 3 | Style index. This is an index into the values in the style box which are defined in argument 2 |

#### Argument 2

String array containing list of items entered in style box

### Returns

Return type: string array

The function returns a string array of length 4 with the same format as argument 1 described above. If the user selects Cancel the function returns an empty vector.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_defineripperdialog) | | |
| [◄ DefineRegisterDialog](func_defineregisterdialog.htm) |  | [DefineSaturableTxDialog ▶](func_definesaturabletxdialog.htm) |
