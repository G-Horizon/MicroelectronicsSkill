# GetConnectedPins Function

Function returns instance and pin name for all pins connected to net at specified point. Results are sorted according to the number of pins on owner instance.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | real array | Yes |  | schematic location |
| 2 | string | No | 'ref' | identifying property |
| 3 | string | No | 'pinname' | pin number of pin name |

#### Argument 1

Specifies a point on the schematic that identifies a net. This could be returned by the  [WirePoints](func_wirepoints.htm)  function for example.

#### Argument 2

Property whose value will be used to identify instance in returned values.

#### Argument 3

Specify whether pins to be identified by their name or number. If set to 'pinnumber', the number will be used otherwise the name will be used.

### Returns

Return type: string array

An array of strings of length equal to 2 times the number of pins on the net. The even indexes hold the property value identifying the instance and the odd indexes hold either the pin's name or number according to the value of argument 3.

Note that this function does not return pins on implicit connections. An implicit connection is one that is made by virtue of having the same netname as defined by a terminal symbol or similar but has no physical connection using wires.

### Example

The following sequence will display the output of this function for a single selected wire on the schematic:

```
** Get selected wires
Let wires = SelectedWires()

** Get locations for first wire in selected list
Let points = WirePoints(wires[0])

** Show connected pins
Show GetConnectedPins([points[0], points[1]])
```

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getconnectedpins) | | |
| [◄ GetConfigLoc](func_getconfigloc.htm) |  | [GetConvergenceDevNames ▶](func_getconvergencedevnames.htm) |
