# GetSchematicFileVersion Function

Returns the file version for the requested schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Schematic file path |

### Returns

Return type: string array

Version information about the file type.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Binary, ASCII or XML file format. Will return unknown if format not recognised or failed if file could not be opened |
| 1 | Binary: version in form N.NN. ASCII/XML: Major version |
| 2 | Binary: empty. ASCII/XML integer value 1 or higher representing minor version number |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getschematicfileversion) | | |
| [◄ GetRegistryClassesRootKeys](func_getregistryclassesrootkeys.htm) |  | [GetSchematicTabs ▶](func_getschematictabs.htm) |
