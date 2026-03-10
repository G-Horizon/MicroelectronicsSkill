# HaveInternalClipboardData Function

Returns the number of items in the specified internal clipboard. The internal clipboard is currently only used for graph curve data.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Data type |

#### Argument 1

The name of the internal clipboard to be queried. Currently there is only one internal clipboard so this argument must always be 'GraphCurve'.

### Returns

Return type: real scalar

### Notes

Use the command  [CurveEditCopy](com_curveeditcopy.htm)  to copy graph curve data to the internal clipboard. Use the `Curve /icb curve_index` to plot a curve that resides in the internal clipboard.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_haveinternalclipboarddata) | | |
| [◄ HaveFeature](func_havefeature.htm) |  | [HierarchyHighlighting ▶](func_hierarchyhighlighting.htm) |
