# SetSnapGrid Command

Warning: only change the snap grid if there is no alternative. We strongly recommend against changing the snap grid simply to satisfy personal preferences as doing so may introduce compatibility problems, especially if applied to symbols.

Sets the snap grid for the currently selected schematic or symbol editor window. The snap grid is the grid on which wires and symbol pins lie. The default value is 120 but may be changed to 60, 40, 30 or 24. Note that this command will not allow the snap grid to be changed to something that would place existing wires or symbols off grid.

```
SetSnapGrid <snapgrid>
```

### Parameters

|  |  |
| --- | --- |
| snapgrid | Snap grid in sheet units. May be 120 (default), 60, 40, 30 or 24. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_setsnapgrid) | | |
| [◄ SetRef](com_setref.htm) |  | [SetStyleColour ▶](com_setstylecolour.htm) |
