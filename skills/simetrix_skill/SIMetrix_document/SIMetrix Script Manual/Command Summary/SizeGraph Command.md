# SizeGraph Command

General purpose command to zoom or scroll a graph. Can apply an offset or scale or both. If both are specified, the offset is applied first.

```
SizeGraph [/axisid id] <x-offset> <y-offset> <x-scale> <y-scale>
```

### Parameters

|  |  |
| --- | --- |
| /axisid | Specify which y-axis to resize. If omitted, all y-axes on selected graph will be affected. |
| /xfull | If specified, the x-axis is zoomed to fit whole graph. xscale and  *x-offset*  will be ignored. |
| /yfull | If specified, the y-axis is zoomed to fit whole graph. yscale and  *y-offset*  will be ignored. |
| x-offset | Extent of X-shift as proportion of full width of graph. E.g. 0.25 will shift by a quarter. 0 has no effect. |
| y-offset | As  *x-offset*  but for y-axis |
| x-scale | View width required as proportion to current width. E.g. 0.8 will zoom in by 20%. 1 has no effect. 0 is illegal. |
| y-scale | As  *x-scale*  but for y-axis. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_sizegraph) | | |
| [◄ ShowSimulatorWindow](com_showsimulatorwindow.htm) |  | [SwitchModelSection ▶](com_switchmodelsection.htm) |
