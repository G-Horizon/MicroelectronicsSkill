# InstPoints Function

Returns an array of length 3 providing XY co-ordinates and orientation of an instance.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No |  | Property name |
| 2 | string | No |  | Property value |
| 3 | real | No | -1 | Schematic ID |

#### Argument 1

Property name to identify instance. Along with parameter 2, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

#### Argument 2

Property value to identify instance. Along with parameter 1, if these arguments are not provided, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

Using the 'HANDLE' property and its value will guarantee uniqueness.

#### Argument 3

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: real array

Returns real array of size 3 as defined by the table. If no instance is identified by arguments 1 and 2 an empty value will be returned.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | X co-ordinate |
| 1 | Y co-ordinate |
| 2 | Orientation: 0 to 7 |

### Notes

The co-ordinates are those of the point defined to be at 0,0 in the symbol definition. The scaling used is 120 points to one grid square. (Grid refers to snap grid. This is the same as the visible grid for magnifications of 0.83 and higher.). Co-ordinates are relative. For a new schematic the zero point is at the top left corner of the window but this can change. The orientation values are as follows:

|  |  |
| --- | --- |
| **Orientation value** | **Description** |
| 0 | Normal (as symbol def) |
| 1 | 90 deg. clockwise |
| 2 | 180 deg. |
| 3 | 270 deg clockwise |
| 4 | Mirrored through y-axis |
| 5 | Mirrored through y-axis + 90 deg clock. |
| 6 | Mirrored through y-axis + 180 deg. |
| 7 | Mirrored through y-axis + 270 deg clock. |

Note: Mirror through x-axis is equivalent to mirror through y with 180 rotation. The values returned by this function can be used with the command  [Inst](com_inst.htm)  using the `/loc` switch.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_instpoints) | | |
| [◄ InstPins](func_instpins.htm) |  | [InstProps ▶](func_instprops.htm) |
