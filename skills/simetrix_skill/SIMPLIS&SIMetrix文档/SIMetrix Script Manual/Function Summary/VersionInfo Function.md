# VersionInfo Function

Returns version information about running copy of SIMetrix

### Arguments

No arguments

### Returns

Return type: string array

Returns a string array of length 7 defined as follows:

|  |  |
| --- | --- |
| 0 | Product name. E.g. "SIMetrix/SIMPLIS Elite with DVM" |
| 1 | Major Version number (3.1, 4.0 etc.) |
| 2 | Maintenance version. (empty or a single letter) |
| 3 | Internal product name. (E.g. "SIMPLIS-Elite") |
| 4 | Feature string allowing script to determine available functionality. This will be a combination of the following separated by the '|' character: |  |  | | --- | --- | | Basic | Always present | | AD | Digital simulator enabled | | Micron | CMOS device models enabled | | Schematic | Schematic enabled | | Advanced | Advanced analysis modes enabled | | Scripts | Scripting enabled | | Rtn | Real time noise enabled | | Simplis\_If | SIMPLIS simulator interface present | |
| 5 | Full version string - usually element 1 and 2 concatenated |
| 6 | Base product name |
| 7 | Architecture : either x86 (32 bit) or x64 (64 bit). This is the architecture of the program not the operating system on which it is running |
| 8 | Development cycle : either Release or Beta |
| 9 | Build type : This will always return FinalRelease for non development versions |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_versioninfo) | | |
| [◄ VectorsInGroup](func_vectorsingroup.htm) |  | [ViewFormattedFile ▶](func_viewformattedfile.htm) |
