# MoveProperty Command

This is an interactive command. It switches the schematic editor into 'move property' mode. In this mode the user can move the specified property for all selected instances. The mode is completed by pressing the left or right mouse key. The left key will fix the new property position and the right key will cancel the mode and leave the properties unmodified.

```
MoveProperty [<property-name>]
```

### Notes

In SIMetrix, property positions can be defined in one of two ways namely 'Auto' and 'Absolute'. Most of the standard symbols have their properties defined as 'Auto'. This means that SIMetrix chooses the location of the property on a specified edge of the symbol and ensures that it doesn't clash with other properties on the same edge. 'Auto' properties are always horizontal and therefore easily readable. The position of 'Absolute' properties is fixed relative to the symbol body regardless of the orientation of the symbol and location of other properties. When the symbol is rotated through 90 degrees, absolute text will also rotate. When a visible property on a symbol is moved using the MoveProperty command, it and all other visible properties on that symbol are converted to 'Absolute' locations. This is the only way that the positions of all properties can be preserved.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_moveproperty) | | |
| [◄ MoveMenu](com_movemenu.htm) |  | [Netlist ▶](com_netlist.htm) |
