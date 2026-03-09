# PrintGraph Command

Prints the current graph sheet.

```
PrintGraph [/caption <caption>] [/margin l t r b] [/major on|off] [/minor on|off] [/mono] [dim-left, dim-top, dim-right, dim-bottom]
```

### Parameters

|  |  |
| --- | --- |
| /caption | Caption printed at the bottom of the page. |
| /interactive |  |
| /major | Specify whether major grid lines should be printed. options are 'on' or 'off'. Default is 'on'. |
| /margin | Page margins in mm, stated in the form  *left, top, right, bottom* . |
| /minor | Specify whether minor grid lines should be printed. options are 'on' or 'off'. Default is 'on'. |
| /mono | If specified, the graph will be printed in black and white. |
| /nointeractive |  |
| dim-left, dim-top, dim-right, dim-bottom | Dimensions and position of printed image on page. Values are relative to page size less the specified margins in units equal to 1/1000 of the page width/height. The default is 0 0 1000 1000 which would place the image to fill the entire area within the margins. 0 500 1000 1000 would place the image at the bottom half of the page. 0 0 2000 1000 would place the left half of the image in the full page while -1000 0 1000 1000 would place the right half. This allows the printing on multiple sheets. Note that if values greater than 1000 or less than 0 are used, part of the printed image will lie in the margins. This provides a convenient overlap for multiple sheets. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_printgraph) | | |
| [◄ PreProcessNetlist](com_preprocessnetlist.htm) |  | [PrintSchematic ▶](com_printschematic.htm) |
