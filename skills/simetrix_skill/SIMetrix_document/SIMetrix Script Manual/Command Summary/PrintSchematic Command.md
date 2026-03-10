# PrintSchematic Command

Prints the current schematic.

```
PrintSchematic [/caption <caption>] [/fixed <grid-size>] [/margin l t r b] [/mono on|off] [<dim-left> <dim-top> <dim-right> <dim-bottom>]
```

### Parameters

|  |  |
| --- | --- |
| /caption | Caption printed at the bottom of the page. |
| /fixed | If specified, fixed scaling will be used.  *grid-size*  is the size of a single grid square on the printed sheet in inches. Otherwise the schematic scale will be chosen to fill the print area. The scaling is  *isotropic* . That is the aspect ratio will be maintained. |
| /margin | Page margins in mm, stated in the form  *left, top, right, bottom* . |
| /mono | If specified, the graph will be printed in black and white. |
| dim-left, dim-top, dim-right, dim-bottom | Dimensions and position of printed image on page. Values are relative to page size less the specified margins in units equal to 1/1000 of the page width/height. The default is 0 0 1000 1000 which would place the image to fill the entire area within the margins. 0 500 1000 1000 would place the image at the bottom half of the page. 0 0 2000 1000 would place the left half of the image in the full page while -1000 0 1000 1000 would place the right half. This allows the printing on multiple sheets. Note that if values greater than 1000 or less than 0 are used, part of the printed image will lie in the margins. This provides a convenient overlap for multiple sheets. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_printschematic) | | |
| [◄ PrintGraph](com_printgraph.htm) |  | [Probe ▶](com_probe.htm) |
