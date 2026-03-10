# ReadIniKey Function

Reads an INI file. An INI file usually has the extension .INI and is used for storing configuration information. INI files are used by many applications and follow a standard format as follows:

```
[section_name1]
key1=value1
key2=value2...
[section_name2]
key1=value1
key2=value2...

etc.
```

There may be any number of sections and any number of keys within each section.

The ReadIniKey function can return the value of a single key and it can also return the names of the all the keys in a section as well as the names of all the sections.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Inifile name |
| 2 | string | Yes |  | Section name |
| 3 | string | Yes |  | Key name |

#### Argument 1

File name. You should always supply a full path for this argument. If you supply just a file name, the system will assume that the file is in the WINDOWS directory. This behaviour may be changed in future versions. For maximum compatibility, always use a full path.

#### Argument 2

Section name. If this argument is an empty string, the function will return the names of the sections in the file.

#### Argument 3

Key name. If this argument is an empty string and argument 2 is  *not*  an empty string, the function will return the names of all the keys in the named section.

### Returns

Return type: string array

string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readinikey) | | |
| [◄ ReadFile](func_readfile.htm) |  | [ReadRegSetting ▶](func_readregsetting.htm) |
