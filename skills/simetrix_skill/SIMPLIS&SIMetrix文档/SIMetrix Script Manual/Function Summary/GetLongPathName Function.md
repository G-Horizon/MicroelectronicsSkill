# GetLongPathName Function

Returns long path name for path specified either as a long or short path. Short path names are a feature of some file systems which represent the path in a form that would be accepted on legacy files systems especially DOS.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

#### Argument 1

Input path. Maybe full or partial and the function will return its argument in the same form. (That it, it won't convert to a full path). If the input path does not exist, this function will simply return its argument unmodified.

### Returns

Return type: string array

### See Also

* [GetShortPathName](func_getshortpathname.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getlongpathname) | | |
| [◄ GetListUnselected](func_getlistunselected.htm) |  | [GetMaxCores ▶](func_getmaxcores.htm) |
