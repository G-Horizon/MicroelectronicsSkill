# GetUserFile Function

Function opens a dialog box to allow the user to select a file.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File filter |
| 2 | string | No |  | Default extension |
| 3 | string | No | <<empty>> | Options |
| 4 | string | No | <<empty>> | Initial file |

#### Argument 1

Defines file filters. The 'save as type' list box may contain any number of entries that defines the type of file to be displayed. This argument defines the entries in this list box.

Each entry consists of a description followed by a pipe symbol ('|') then a list of file extensions separated by semi-colons (';'). Entries are also separated by the pipe ('|') symbol. For example, to list just schematic files enter:

```
"'Schematic files|*.sxsch;*.sch'"
```

Note that the text is enclosed in both single and double quotes. Strings in expressions are denoted by single quotes as usual but the semi-colon is normally used to separate commands on a single line. This is inhibited by enclosing the whole string in double quotes.

If you wanted to provide entries for selecting - say - both schematics and netlists, you could use the following:

```
"'Schematic files|*.sxsch;*.sch|Netlist files|*.net;*.cir'"
```

#### Argument 2

The default extension specified without the dot. This is the extension that will automatically be added to the file name if it does not already have one of the extensions specified in the filter.

#### Argument 3

String array that specifies a number of options. Any or all of the following may be included:

|  |  |
| --- | --- |
| 'ChangeDir' | If present, the current working directory will change to that containing the file selected by the user |
| 'Open' | If present a File Open box will be displayed otherwise a Save As box will be displayed. |
| 'NotExist' | If used with 'Open', the file is not required to already exist to be accepted |
| 'ShowReadOnly' | If present and 'Open' is also specified, an Open as readonly check box will be displayed. The user selection of this check box will be returned in either the second or third field of the return value. |
| 'FilterIndex' | If specified, the type of file selected by the user will be returned as an index into the list of file filters specified in argument 1. So, 0 for the first, 1 for the second etc. |

#### Argument 4

Initial file selection.

### Returns

Return type: string

String array of length between 1 and 3 as described in the following table:

|  |  |  |
| --- | --- | --- |
| **Option 'ShowReadOnly'** | **Option 'FilterIndex'** | **Return value** |
| No | No | Path name only |
| Yes | No | Two element array: |  |  | | --- | --- | | index=0 | path name | | index=1 | Read only checked - 'TRUE' or 'FALSE' | |
| No | Yes | Two element array: |  |  | | --- | --- | | index=0 | path name | | index=1 | Filter index selected | |
| Yes | Yes | Three element array: |  |  | | --- | --- | | index=0 | path name | | index=1 | Filter index selected | | index=2 | Read only checked - 'TRUE' or 'FALSE' | |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getuserfile) | | |
| [◄ GetUsedStyles](func_getusedstyles.htm) |  | [GetVecStepParameter ▶](func_getvecstepparameter.htm) |
