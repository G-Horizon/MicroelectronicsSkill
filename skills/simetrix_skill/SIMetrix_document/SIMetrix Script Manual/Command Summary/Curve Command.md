# Curve Command

Curve can be used to add a new curve to an existing graph created with Plot or to change the way it is displayed.

```
Curve 
        [/xl <xlimit_low> <xlimit_high>] [/yl <ylimit_low> <ylimit_high>] [/xdelta <xdelta>] [/ydelta <ydelta>]
        [/ylabel <ylabel>] [/xlabel <xlabel>] [/yunit <yunit>] [/xunit <xunit>] [/title] [/xauto] [/yauto]
        [/xlog] [/ylog] [/loglog] [/dig] [/select] [/newaxis] [/newgrid] [/axisid <id>] [/autoaxis] [/coll] [/name]
        [/bus <bus-spec>] [/icb <objid>] [/new] [/newsheet] [/autoxlog] [/autoylog] [/histo]\n
        <y-expression> [<x-expression>]
```

### Parameters

|  |  |
| --- | --- |
| /autoaxis | If specified, a suitable axis based on physical type will be selected or created. For example if a current vector is specified and all current curves are for voltages, a new y-axis will be created to separate the voltages from currents |
| /autoXlog | Automatically choose log or lin for x-axis according to data |
| /autoYlog | Automatically choose log or lin for y-axis according to data |
| /axisid | If specified, the new curve will be added to a y-axis with the id specified. Axis id is returned by the functions  [GetAllYAxes](func_getallyaxes.htm)  ,  [GetCurveAxis](func_getcurveaxis.htm)  and  [GetSelectedYAxis](func_getselectedyaxis.htm) . |
| /bus | If specified, the new curve will be plotted on a digital axis and will be plotted as a bus curve. type may be 'hex', 'dec' or 'bin' specifying hexadecimal, decimal or binary display respectively. |
| /cv | Get data from CurveData object. Used to ungroup curve history |
| /dig | If specified, new curve will be plotted on new digital axis. Digital axes are stacked on top of main axes and are sized and labelled appropriately for digital waveforms. |
| /graphuserid | Plots curve on same graph as existing curve created with .GRAPH with userid parameter |
| /gridid | If specified, the curve will be plotted on the specified grid. |
| /griduserid | Plots curve on same grid as existing curve created with .GRAPH with userid parameter |
| /group | Always group multi-division curves. Usually multi-division curves are grouped by default. The exception is if the curves are digital and the option to ungroup was set in the analysis definition |
| /guid | Adds the specified GUID to the ProbeGuid property of the curve |
| /histo | Plot histogram |
| /icb | Specifies the internal clipboard as the source of the curve data. clipboard-index is a value of 0 or more that indicates which curve in the internal clipboard is to be used. The function  [HaveInternalClipboardData](func_haveinternalclipboarddata.htm)  may be used to determine the number of curves available. The maximum acceptable value for clipboard-index is thus one less than the value returned by  [HaveInternalClipboardData](func_haveinternalclipboarddata.htm) . |
| /loglog | Only effective when graph sheet is empty. Forces both y and x axes to be logarithmic |
| /name | If specified, curve will be named curve-name. |
| /newAxis | If specified, the new curve will be plotted on a new y-axis. |
| /newGrid | If specified, the new curve will be plotted on a new grid. |
| /newGridDetached | As newGrid but with a detached x-axis. A detached x-axis has an independent zoom |
| /scatter | Plot scatter plot |
| /select | If specified, the new curve will be selected. |
| /title | Plot and NewPlot commands only: sets graph window title when new sheet created |
| /ungroup | Always ungroup multi-division curves |
| /xauto | Flag. Use automatic limits for x-axis. If this appears after a /xl specification /xauto will override it and vice-versa. |
| /xAxisid | If specified, the new curve will be added to a x-axis with the id specified. |
| /xdelta | Specify spacing between major grid lines on x-axis. Followed by  *x-grid-spacing*  , a real value. For default spacing use 0. |
| /xl | Use fixed limit for x-axis. Followed by  *x-low-limit*  and  *x-high-limit*  , which are real valued lower and upper limit of the x-axis. |
| /xlabel | Specify a label for the x-axis. If the label name argument contains any spaces, the whole string must be enclosed in double quotes. |
| /xlog | Only effective when graph sheet is empty. Forces logarithmic xaxis. |
| /xunit | Specify units for the x-axis (Volts, Watts etc.), followed by the unit name as a string. If the string contains spaces, the whole string must be enclosed in quotes (""). You should not include an engineering prefix (m, K etc.). This switch assigns the unit to the axis and also to the curve being plotted. |
| /yauto | Flag. Use automatic limits for y-axis. If this appears after a /yl specification /yauto will override it and vice-versa. |
| /ydelta | Specify spacing between major grid lines on y-axis. Followed by  *y-grid-spacing*  , a real value. For default spacing use 0. |
| /yl | Use fixed limit for y-axis. Followed by  *y-low-limit*  and  *y-high-limit*  , which are real valued lower and upper limit of the y-axis. |
| /ylabel | Specify a label for the y-axis. If the label name argument contains any spaces, the whole string must be enclosed in double quotes. |
| /ylog | Only effective when graph sheet is empty. Forces logarithmic yaxis. |
| /yunit | Specify units for the y-axis (Volts, Watts etc.), followed by the unit name as a string. If the string contains spaces, the whole string must be enclosed in quotes (""). You should not include an engineering prefix (m, K etc.). This switch assigns the unit to the axis and also to the curve being plotted. |

### Notes

**/autoxlog and /autoxylog log test**  The x-values are deemed to be logarithmically spaced if three values satisfy the following:  \[ 1.0000001 > \frac{x\_1^2}{x\_0\*x\_2} > 0.9999999 \]  Where:  \[ x\_0 = x[0] \]  i.e the first point in the data. If there are an even number of points:  \[ x\_1 = x[\frac{n}{2}-1] \]   \[ x\_2 = x[n-2] \]  where ???MATH???n???MATH??? is the number of points in the data. If there are an odd number of points:  \[ x\_1 = x[\frac{n-1}{2}] \]   \[ x\_2 = x[n-1] \]  where ???MATH???n???MATH??? is the number of points in the data. If there are fewer than three points or any of the values is less than or equal to zero, a linear axis will be selected.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_curve) | | |
| [◄ CursorMode](com_cursormode.htm) |  | [CurveEditCopy ▶](com_curveeditcopy.htm) |
