# ConvertSchematicFormat Function

Converts a schematic file or symbol library from one format to another. Supports these formats for both input and output

|  |  |
| --- | --- |
| binary25 | Binary format used from version 2.5 |
| binary | Binary format used from version 4.1 |
| ascii | Default format since version 8.0 but readable and writeable with all versions from version 5 |
| XML | Optional XML format introduced with version 9.1 |

In addition, LTspice schematic and symbol files are also accepted as input.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Path of input file |
| 2 | String | Yes |  | Path of output file |
| 3 | String | Yes |  | Output format |

#### Argument 1

Path of input file

#### Argument 2

Path of output file

#### Argument 3

Output format. Can be one of the following:

|  |  |
| --- | --- |
| binary25 | Binary format used from version 2.5 |
| binary | Binary format used from version 4.1 |
| ascii | Default format since version 8.0 but readable and writeable with all versions from version 5 |
| XML | Optional XML format introduced with version 9.1 |
| default | Uses the current default output format. For versions up to and including version 9.1 this is usually ASCII but may be overridden using the \mbox{SchematicSaveFormat} option setting |

### Returns

Return type: String or String array

Status value indicating the success or otherwise of the operation. Maybe one of these values

|  |  |
| --- | --- |
| success | Conversion succeeded |
| file-corrupted | Input file corrupt |
| obsolete-format | Input file uses an obsolete format |
| open-read-fail | Could not open input file |
| unknown-input-format | Input file uses an unknown format |
| unknown-version | Input file uses an unknown version |
| open-write-fail | Output file could not be opened |
| unknown-output-format | Output format not recognised |
| file-write-fail | Failure writing output file |
| unexpected | unexpected error |
| unknown | unknown error |

In the case of error, there may be additional fields giving further information about the error

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_convertschematicformat) | | |
| [◄ ConvertRGBcolourToHTML](func_convertrgbcolourtohtml.htm) |  | [ConvertToBase64 ▶](func_converttobase64.htm) |
