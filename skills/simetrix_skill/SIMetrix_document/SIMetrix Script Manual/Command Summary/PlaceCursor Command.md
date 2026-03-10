# PlaceCursor Command

Positions graph cursors if they are enabled.

```
PlaceCursor [/main x-main y-main] [/datum x-datum y-datum]
```

### Parameters

|  |  |
| --- | --- |
| /datum | Location of reference cursor. Position is determined by  *x-datum* .  *y\_datum*  is only used for non-monotonic curves (e.g. nyquist plots) where there is more than one y value for a given x value. |
| /main | Location of main measurement cursor. Position is determined by  *x-main* .  *y-main*  is only used for non-monotonic curves (e.g. Nyquist plots) where there is more than one y value for a given x value. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_placecursor) | | |
| [◄ Pause](com_pause.htm) |  | [Plot ▶](com_plot.htm) |
