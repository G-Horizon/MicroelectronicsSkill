# EditFileDefinedPWLDialog Function

Opens the dialog box shown below allowing the entry of X-Y pairs intended for the definition of file defined piece-wise linear sources. ![](../../assets/fdpwl-dialog-four-pulses.png)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | file content |
| 2 | string | No |  | Source options |
| 3 | string | No |  | Options |

#### Argument 1

File content used to initialise table represented as a string array. The above example would be displayed after a call to:

```
Show EditFileDefinedPWLDialog(['***' , '*** default_file.txt' , '***' , 'START_DATA' , '0 0' ,  '10u 0' ,  '20u 1' ] , [ '0' , '0' , '0' , " , 'Disk' ] )
```

#### Argument 2

Up to seven element string array to define source parameters:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Source delay parameter |
| 1 | Checkbox state for Periodic source checkbox. |
| 2 | Checkbox state for Active only during transient after POP? checkbox. |
| 3 | Filename. |
| 4 | File location used to initialize the radio selection. 'Disk' or 'F11'. |
| 5 | v9.20+ Backward compatibility flag. 1 - removes ability to use parameterization |
| 6 | Reference designator for souce, used in error messages. |
| 7 | Pipe (|) delimited list of F11 filenames used to populate the F11 window combobox. |

#### Argument 3

Up to six element string array to define box labels:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Box caption. Default: 'Edit File Defined PWL Source' |
| 1 | Label for X-Values column. Default: 'Time' |
| 2 | Label for Y-Values column. Default: 'Value' |
| 3 | Help context id. Default: '-1' (no help button shown) |
| 4 | Minimum number of segments. Default = '2' |
| 5 | Maximum number of segments. Default = '100001' |

### Returns

Return type: string array

The function returns the edited file as a string array. The first element of the return contains the source parameters, concatenated in a semi-colon delimited list of 5 elements:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Source delay parameter |
| 1 | Checkbox state for Periodic source checkbox. |
| 2 | Checkbox state for Active only during transient after POP? checkbox. |
| 3 | Filename. |
| 4 | File location radio button state. 'Disk' or 'F11'. |
| 5 | Checkbox stat for Backward compatible checkbox. |

The file contents start at the second element (index=1). You can slice the file contents out of the return array with the  [Range](func_range.htm)  function:

```
Let fileContents = Range( return , 1 )
```

String arrays can be written to file with the  [Show](com_show.htm)  command.

```
Show /plain /file points.txt fileContents
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editfiledefinedpwldialog) | | |
| [◄ EditDigInitDialog](func_editdiginitdialog.htm) |  | [EditFreeTextDialog ▶](func_editfreetextdialog.htm) |
