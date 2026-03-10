# Wires Function

Returns array of strings holding handles for all wires in the specified schematic. Wire handles are used by the function  [WirePoints](func_wirepoints.htm)  and the commands  [Select](com_select.htm)  and  [SetHighlight](com_sethighlight.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real | No | -1 | Schematic ID |

#### Argument 1

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

### See Also

* [NetWires](func_netwires.htm)
* [SelectedWires](func_selectedwires.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wires) | | |
| [◄ WirePoints](func_wirepoints.htm) |  | [WM\_CanRevertToSaved ▶](func_wm_canreverttosaved.htm) |
