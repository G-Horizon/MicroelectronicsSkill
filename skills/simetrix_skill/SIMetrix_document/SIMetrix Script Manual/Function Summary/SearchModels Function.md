# SearchModels Function

This is a special purpose function designed for use with the model installation system. It returns an array of strings holding pathnames with wildcards of directories containing files with SPICE compatible models. The argument specifies a directory tree to search. The function will recurse through all sub directories of the supplied path.

Note that if the root directory of a large disk is specified, this function can take a considerable time to return. It can however be aborted by pressing the escape key.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Path to search |

### Returns

Return type: string array

List of library specs containing model files

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_searchmodels) | | |
| [◄ SearchDialog](func_searchdialog.htm) |  | [Seconds ▶](func_seconds.htm) |
