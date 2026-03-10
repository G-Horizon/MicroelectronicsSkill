# GetLicenseStats Function

Returns information about the license checkout process. This function is typically used to provide diagnostic information when a license checkout fails.

### Arguments

No arguments

### Returns

Return type: string array

Returns an array of strings. Each entry provides details of each license location. The first entry is always the license path for license files. Subsequent entries refer to network license servers and there could be more than one of these.

Each entry is a semi-colon delimited list of values in the form:  *location;type;checkout successful;checkout time;error code* .  *type*  may be 'path' or 'server'.  *error code*  will be 0 if successful otherwise it will be a negative number according to the cause of failure. A list of error codes is provided in the FLEXlm end user documentation provided on the install CD.  *checkout time*  is the time taken to check out the license.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlicensestats) | | |
| [◄ GetLicenseInfo](func_getlicenseinfo.htm) |  | [GetLine ▶](func_getline.htm) |
