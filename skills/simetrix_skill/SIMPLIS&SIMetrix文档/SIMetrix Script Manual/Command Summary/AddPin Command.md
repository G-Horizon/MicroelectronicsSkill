# AddPin Command

AddPin is a Symbol Definition Command. A pin is a point on a symbol where wires can be connected. Refer to  [Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm)  for more details.

```
AddPin <pin-name> <pin-number> <x> <y> [<label-x> <label-y> <label-flags>] [<qualifier-list>]
```

### Parameters

|  |  |
| --- | --- |
| pin-name | Text string. Any pin name can be used as long as it does not contain spaces. However, in order to allow the plotting of currents from the schematic, certain pin names must be used for primitive components. |
| pin-number | Integer. Determines the order in which the pins appear on the device's netlist entry. Must be in a certain order for primitive components. |
| x,y | Integer. Symbol co-ordinates of pin. As wires always snap to grid points pins must lie on grid points if is to be possible to connect to them. This means that the x and y co-ordinates must be a multiple of 100. |
| label-x, label-y | X and Y position relative to pin of pin label. Text of label will be pin name. Scaling is 100 points per grid square. Justification is determined by label\_flags - see below. |
| label-flags | Justification of pin label text. Values as follows:  |  |  | | --- | --- | | 0: | left top | | 1: | centre top | | 2: | right top | | 8: | left baseline | | 9: | centre baseline | | 10: | right baseline |  Baseline means the base for upper case characters. The tails of some lower case characters go below the baseline. |
| qualifier-list | One or more qualifiers used for XSPICE devices. For more information refer to  [Simulator Reference Manual/Simulator Devices/Using XSPICE Devices](../../../simetrix/simulator_reference/topics/simulatordevices_usingxspicedevices.htm) . Qualifiers may be one of:  |  |  | | --- | --- | | vecclose | Pin closes a vector connection. This causes a ']' to be placed after the pin's connection in the netlist | | vecopen | Pin opens a vector connection. This causes a '[' to be placed before the pin's connection in the netlist | | vecopenl | As vecopen except that it forces the '[' to always be placed before any other qualifiers. | | invert | Inverts a digital pin. Places a '~' before it in the netlist | | %d | Forces pin to be of digital type. | | %g | Forces pin to be of type "grounded conductance". | | %gd | Forces pin and the one following to be of type "differential conductance" | | %h | Forces pin to be of type "grounded resistance". | | %hd | Forces pin and the one following to be of type "differential resistance" | | %i | Forces pin to be of type "single ended current". | | %id | Forces pin and the one following to be of type "differential current" | | %v | Forces pin to be of type "single ended voltage". | | %vd | Forces pin and the one following to be of type "differential voltage" | |

### See Also

* [Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addpin) | | |
| [◄ AddLegendProp](com_addlegendprop.htm) |  | [AddProp ▶](com_addprop.htm) |
