# GetSchematicVersion Function

Returns version information for the currently selected schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

Returns an array of length 4. Details are given below. The following table shows integer versions returned in element 0 and associated application version. Note these only apply to old binary schematics. A value of zero is returned for ASCII or XML schematics.

|  |  |
| --- | --- |
| 102 | Version 1.0 to 2.02 |
| 250 | Version 2.5 to 4.0 |
| 420 | Version 4.1 |
| 421 | Version 4.2 |
| 422 | Version 4.5 |
| 423 | Version 5.0 - 5.2 |
| 424 | Version 5.3 |
| 425 | Version 5.4 |
| 426 | Version 5.5 |
| 0 | ASCII or XML schematic |

The meaning of the 4 elements is described below:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Format version. This will be an integer defining the format of the schematic binary file. Possible values and the SIMetrix versions for which those formats were used are listed above. |
| 1 | User version. Each time the schematic is saved this value is incremented |
| 2 | Exact version of SIMetrix that was used to save the file. Only valid if saved with version 5.4 or later. Otherwise this field will be empty. Version includes the maintenance suffix letter. E.g. 5.4e |
| 3 | Name of application that created the schematic file |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getschematicversion) | | |
| [◄ GetSchematicTabs](func_getschematictabs.htm) |  | [GetSchemTitle ▶](func_getschemtitle.htm) |
