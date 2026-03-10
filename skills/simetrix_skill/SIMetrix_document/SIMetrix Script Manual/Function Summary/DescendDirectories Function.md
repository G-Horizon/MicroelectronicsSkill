# DescendDirectories Function

Returns all directories under the specified directory. DescendDirectories recurses through all sub-directories including those pointed to by symbolic links. DescendDirectories only returns directory names. It does not return files. Use the  [ListDirectory](func_listdirectory.htm)  function to return the files in a directory.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Directory |
| 2 | string | No | None | Options |

#### Argument 2

Set to 'includehidden' to include hidden files in putput

### Returns

Return type: string array

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_descenddirectories) | | |
| [◄ DelSchemProp](func_delschemprop.htm) |  | [DescendHierarchy ▶](func_descendhierarchy.htm) |
