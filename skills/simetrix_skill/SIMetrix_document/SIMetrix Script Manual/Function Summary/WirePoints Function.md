# WirePoints Function

Returns location of specified wire.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Wire handle |
| 2 | real | No | -1 | Schematic ID |

#### Argument 1

Handle of schematic wire segment. Wire handles are returned by the functions  [Wires](func_wires.htm)  ,  [NetWires](func_netwires.htm)  and  [SelectedWires](func_selectedwires.htm) .

#### Argument 2

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: real array

Returns a numeric vector of length 4 providing the sheet locations of the each termination of the specified wire.

The four values in the vector are defined in the table. The functions returns an empty vector if the wire handle supplied is invalid.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | X-co-ordinate for termination 1 |
| 1 | Y-co-ordinate for termination 1 |
| 2 | X-co-ordinate for termination 2 |
| 3 | Y-co-ordinate for termination 2 |

### See Also

* [InstPoints](func_instpoints.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wirepoints) | | |
| [◄ WC2](func_wc2.htm) |  | [Wires ▶](func_wires.htm) |
