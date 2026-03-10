# RenameLibs Command

Runs the rename model utility. This renames models inside installed model files if they are found to have duplicates. This command is called by the rename\_libs script which is documented in the User's Manual.

```
RenameLibs [/report] [/check] [/log logfile] <filename> <suffix> [catalog-file] [user-catalog-file]
```

### Parameters

|  |  |
| --- | --- |
| /check | If specified a dummy renaming process will be performed. All reports, logs and messages will be output but no actual renaming will take place. |
| /log | If specified, all renamed models will be listed in  *logfile* . |
| /report | If specified a report of progress will be displayed in the command shell. |
| filename | Name of model library file or file spec to be processed. This may include '\*' or '?' wild card characters. Any models within this file that have duplicates already installed in the global model library will be renamed using the suffix supplied. |
| suffix | Suffix applied to duplicate model name. |
| catalog-file | Usually called OUT.CAT. If specified alongside  *user-catalogfile*  , any user association of renamed models will be appropriately modified. |
| user-catalog-file | If specified a report of progress will be displayed in the command shell. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_renamelibs) | | |
| [◄ RegisterUserFunction](com_registeruserfunction.htm) |  | [RenameMenu ▶](com_renamemenu.htm) |
