# GetCompatiblePathName Function

Returns a "short" path name if the supplied path has white space or non-ascii characters. This function may not function as desired on all systems as not all file systems support short path names.

The function only replaces the parts of the path that have spaces or non-ASCII characters.

A short path is one that complies with the DOS 8.3 naming convention.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path |

#### Argument 1

Input path. Maybe full or partial and the function will return its argument in the same form (that it, it won't convert to a full path). If the input path does not exist, this function will simply return its argument unmodified.

### Returns

Return type: string

### See Also

* [GetLongPathName](func_getlongpathname.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getcompatiblepathname) | | |
| [◄ GetColourSpec](func_getcolourspec.htm) |  | [GetComponentValue ▶](func_getcomponentvalue.htm) |
