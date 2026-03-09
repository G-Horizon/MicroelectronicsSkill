# EditTimer Function

Edit a timer. The function can stop a timer or change its interval. To delete a timer, use the  [DeleteTimer](func_deletetimer.htm)  function.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Timer ID |
| 2 | string | Yes |  | action |
| 3 | real | No |  | Value |

#### Argument 1

Timer ID as returned by the  [CreateTimer](func_createtimer.htm)  function

#### Argument 2

Action. This can be either:

|  |  |
| --- | --- |
| 1. | 'interval' in which case this function will change the interval of the timer identified in argument 1 to the value specified in argument 3 |
| 2. | 'kill' in which case the timer will be stopped. The timer will not be deleted and can be restarted by calling this function with the 'interval' action |

#### Argument 3

Required if 'interval' is specified in argument 2

### Returns

Return type: real

Returns 1.0 if the function is successful. Otherwise returns 0.0. The function will fail if the specified timer does not exist, if the action is not recognised or if the action is 'interval' and argument 3 is not specified.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_edittimer) | | |
| [◄ EditSymbolBusDialog](func_editsymbolbusdialog.htm) |  | [EditWaveformDialog ▶](func_editwaveformdialog.htm) |
