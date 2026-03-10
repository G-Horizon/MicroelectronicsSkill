# AddCurveData Command

Curves can contain multiple data items used to store history. This command adds new data to a curve putting any previous data in its history. The old data will usually be plotted using broken lines.

```
AddCurveData /curve <curve-id> [/icb <objid>] [<y-expression> [<x-expression>]]
```

### Parameters

|  |  |
| --- | --- |
| /curve | Curve id. Compulsory |
| /icb | Specifies the internal clipboard as the source of the curve data. clipboard-index is a value of 0 or more that indicates which curve in the internal clipboard is to be used. The function  [HaveInternalClipboardData](func_haveinternalclipboarddata.htm)  may be used to determine the number of curves available. The maximum acceptable value for clipboard-index is thus one less than the value returned by  [HaveInternalClipboardData](func_haveinternalclipboarddata.htm) . |
| y-expression | Expression to be evaluated to create curve data. Compulsory unless /icb specified |
| x-expression | Optional expression to define x-values for curve data |

### Notes

For more information about curve history, see  [Users Manual/Graphs, Probes and Data Analysis/Fixed Probes/Curve History](../../user_manual/topics/graphs_probesanddataanalysis_fixedprobes.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addcurvedata) | | |
| [◄ AddCirc](com_addcirc.htm) |  | [AddCurveMarker ▶](com_addcurvemarker.htm) |
