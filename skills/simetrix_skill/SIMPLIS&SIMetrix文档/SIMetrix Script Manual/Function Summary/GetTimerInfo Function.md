# GetTimerInfo Function

Returns information about a timer object created using  [CreateTimer](func_createtimer.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | Yes |  | Timer id |

#### Argument 1

Timer id returned by  [CreateTimer](func_createtimer.htm)

### Returns

### Notes

If a timer is defined using the 'oneshot' option, the return value for the timer interval will change after the timer has triggered. Before the timer triggers the specified interval will be returned. After the timer has triggered, it will return 0.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_gettimerinfo) | | |
| [◄ GetThreadTimes](func_getthreadtimes.htm) |  | [GetTitleBlockInfo ▶](func_gettitleblockinfo.htm) |
