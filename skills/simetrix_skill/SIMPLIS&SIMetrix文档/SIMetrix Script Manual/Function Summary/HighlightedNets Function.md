# HighlightedNets Function

Returns names for any wholly highlighted net names on the specified schematic.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

Returns the highlighted netnames as an array of strings.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_highlightednets) | | |
| [◄ HierarchyHighlighting](func_hierarchyhighlighting.htm) |  | [Histogram ▶](func_histogram.htm) |
