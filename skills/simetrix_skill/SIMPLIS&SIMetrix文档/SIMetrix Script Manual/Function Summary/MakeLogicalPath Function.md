# MakeLogicalPath Function

Converts a file system path to a symbolic path using the automatic path matching mechanism. This process is described in  [User's Manual/Sundry Topics/Symbolic Path Names](../../user_manual/topics/sundrytopics_symbolicpathnames.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |
| 2 | string | Yes |  | Options |

#### Argument 2

May be set to either one of:

|  |  |
| --- | --- |
| **Name** | **Description** |
| 'systemonly' | Will only match system symbols to the path. These are: %STARTPATH% %DOCSPATH% %EXEPATH% %APPDATAPATH% %TEMPPATH% %SXAPPDATAPATH% %SHAREPATH% %LIBPATH% %SXDOCSPATH% %COMMON\_APPDATAPATH% |
| 'projectonly' | Will only match symbols listed in the [Locations] section of the configuration file |

Refer to  [User's Manual/Sundry Topics/Symbolic Path Names/Definition](../../user_manual/topics/sundrytopics_symbolicpathnames.htm)  for details of system path

### Returns

Return type: string

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_makelogicalpath) | | |
| [◄ MakeDir](func_makedir.htm) |  | [MakeString ▶](func_makestring.htm) |
