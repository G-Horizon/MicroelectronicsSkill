# CreateTimer Function

Creates a timer to run a script at regular intervals or at some specified time in the future.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Command |
| 2 | real | Yes |  | Interval |
| 3 | string array | No | 2 | options |

#### Argument 1

Command to run. This can be a primitive command or the name of a script and may include arguments to the command or script.

#### Argument 2

Interval in milliseconds. The first event will occur after the interval time has elapsed.

#### Argument 3

Options. String array containing any combination of 'oneshot' and 'echo'. 'oneshot' defines a timer that will trigger only once. 'echo' enables message output in the command shell.

### Returns

Return type: real

The function returns an integer id. This can be used as an argument to functions  [DeleteTimer](func_deletetimer.htm)  ,  [EditTimer](func_edittimer.htm)  and  [GetTimerInfo](func_gettimerinfo.htm) .

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_createtimer) | | |
| [◄ CreateShortcut](func_createshortcut.htm) |  | [CurveEditDialog ▶](func_curveeditdialog.htm) |
