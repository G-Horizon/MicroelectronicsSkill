# GetLicenseInfo Function

Returns information about the current license.

### Arguments

No arguments

### Returns

Return type: string array

String array as defined in the following table:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | License type. One of 'Network', 'NamedUser', 'Nodelocked', 'Portable' or 'Unknown' |
| 1 | License serial number |
| 2 | Licensee |
| 3 | License location. Server name if network. |
| 4 | Additional information specific to license type. For portable licenses this is the type and serial number of the hardware key (dongle). |
| 5 | Expiry date. Returns 'permanent' if non-expiring. |
| 6 | License version - this number is related to the maintenance expiry date. |
| 7 | Enabled features |
| 8 | Encryption code |
| 9 | License server version |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlicenseinfo) | | |
| [◄ GetLibraryModels](func_getlibrarymodels.htm) |  | [GetLicenseStats ▶](func_getlicensestats.htm) |
