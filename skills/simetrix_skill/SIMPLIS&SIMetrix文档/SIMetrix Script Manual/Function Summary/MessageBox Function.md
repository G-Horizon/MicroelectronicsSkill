# MessageBox Function

Opens a message dialog box with a choice of styles.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | Message |
| 2 | string array | No |  | Options |

#### Argument 1

1 or 2 element string array. First element is the text of the message to be displayed in the box. The second element is the box title. If the second element is not supplied the box title will be the name of the application - e.g. 'SIMetrix Classic'

#### Argument 2

1, 2 or 3 element string array. First element is box style. This may be one of the following:

|  |  |
| --- | --- |
| 'AbortRetryIgnore' | Three buttons supplied for user response - Abort, Retry and Ignore |
| 'Ok' | Ok button only |
| 'OkCancel' | Ok and Cancel button |
| 'YesNo' | Yes and No buttons |
| 'YesNoCancel' | Yes, No and Cancel buttons. |

Default = 'OkCancel'

Second element is icon style. A small icon is displayed in the box to indicate the nature of the message. Possible values: 'Warn', 'Info', 'Question', 'Stop'.

Default = 'Info'

Third element may be 'dontaskagain' or 'dontshowmessageagain' in which case a 'Do not ask again' or 'Do not show this message again' check box will also be displayed

### Returns

Return type: string

A single string indicating the user's response. One of:

* 'Abort'
* 'Cancel'
* 'Ignore'
* 'No'
* 'Ok'
* 'Retry'
* 'Yes'

If 'dontaskagain' or 'dontshowmessageagain' was specified and the user checked the 'Do not ask again'/'Do not show this message again' check box, the return value will be appended with '|DontAskAgain'

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_messagebox) | | |
| [◄ MeasureDialog](func_measuredialog.htm) |  | [Mid ▶](func_mid.htm) |
