# OpenSchem Function

Opens a schematic similar to the command  [OpenSchem](com_openschem.htm)  but returns a code indicating success or otherwise.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File path |
| 2 | string array | No |  | Options |

#### Argument 1

Schematic file path.

#### Argument 2

Options. String array may contain any of the following:

|  |  |
| --- | --- |
| **Option** | **Description** |
| 'cd' | Change current working directory to the location of the specified schematic file |
| 'readonly' | Open in read only mode |
| 'selectiveReadOnly' | Open in read only mode if the schematic file cannot be opened for writing |

### Returns

Return type: string array

The return value is a string array. The first element may be one of the following:

|  |  |
| --- | --- |
| **Code** | **Description** |
| NOERR | Schematic opened successfully |
| OPEN\_WITH\_ERRORS | Opened with some errors reported in later array elements |
| OPEN\_WITH\_WARNINGS | Opened with some warnings reported in later array elements |
| SC\_READONLY | Schematic file is read only. If 'readonly' or 'selectiveReadOnly' was specified as an option, then the schematic would have been successfully opened but it will not be possible to save it to the same file. |
| SC\_LOCKED | Schematic file is in use by another SIMetrix user. If 'readonly' or 'selectiveReadOnly' was specified as an option, then the schematic would have been successfully opened but it will not be possible to save it to the same file. |
| FILE\_NONAME | No file name was given. (Arg1 an empty string) |
| FILE\_CANTOPENFORREAD | Can't open specified file because it doesn't exist or the path is bad |

Subsequent elements may provide additional information about errors or warnings

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_openschem) | | |
| [◄ OpenPrinter](func_openprinter.htm) |  | [OpenSchematic ▶](func_openschematic.htm) |
