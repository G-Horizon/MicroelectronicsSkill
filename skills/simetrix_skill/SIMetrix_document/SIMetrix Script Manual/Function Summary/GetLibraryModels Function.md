# GetLibraryModels Function

Returns a string array containing information about each model in the specified model library.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Library spec |
| 2 | string | No |  | Options |

#### Argument 1

Library specification for installed library. This could be a single file or a folder containing a wildcard specification. All installed libraries are returned by  [GetModelFiles](func_getmodelfiles.htm) .

#### Argument 2

If set to 'usermodelsonly' only models installed by the user will be returned.

### Returns

Return type: string array

String array with each element describing a single library model. Information is supplied as a semi-colon delimited string with the following fields:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Model name |
| 1 | File where model found. (Filename only, not full path) |
| 2 | Line number |
| 3 | SPICE letter. E.g. 'x' for subcircuits |
| 4 | Is alias: 'false' not an alias, 'true' is an alias |
| 5 | User install time. 0 if system installed. Time is number of seconds since January 1, 1970 |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlibrarymodels) | | |
| [◄ GetLegendProperties](func_getlegendproperties.htm) |  | [GetLicenseInfo ▶](func_getlicenseinfo.htm) |
