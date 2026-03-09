# Histogram Function

Creates a histogram of argument 1 with the number of bins specified by argument 2. The bins are divided evenly between the maximum and minimum values in the argument.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | Vector |
| 2 | real | Yes |  | Number of bins |
| 3 | string | No |  | Options |

#### Argument 1

Vector to be processed.

#### Argument 2

Number of bins.

#### Argument 3

Set to 'step' to force output in a stepped style similar to a bar-graph.

### Returns

Return type: real XY array

### Notes

Histograms are useful for finding information about waveforms that are difficult to determine by other means. They are particularly useful for finding "flat" areas such as the flat tops of pulses as these appear as well defined peaks. The Histogram() function is used in the rise and fall time scripts for this purpose. Users should note that using this function applied to raw transient analysis data will produce misleading results as the values are unevenly spaced. If you apply this function to simulation data, you must either specify that the simulator outputs at fixed intervals (select the Output at .PRINT step option in the **Simulator** > **Choose Analysis...** dialog box) or you must interpolate the results using the function  [Interp](func_interp.htm) .

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_histogram) | | |
| [◄ HighlightedNets](func_highlightednets.htm) |  | [HistoryDepthDialog ▶](func_historydepthdialog.htm) |
