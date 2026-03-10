# CopyClipGraph Command

Copies a graphical picture of the graph to the clipboard or to a specified file.

### Parameters

|  |  |
| --- | --- |
| /dpi | Defines the assumed DPI setting for creating the graph. Graph objects such as text and lines are sized in physical units (inches, millimeters) not in pixels. By default the image created by this command assumes the DPI (dots-per-inch) setting of the current display. With high resolution displays this can lead to heavy lines and large text if the image size is small. By specifying a fixed DPI a consistent image will be created independent of the system that generated it. A suitable value is 96 for an image of around 512 x 512. For larger images a higher value can be used. |
| /file | If specified, the graph is written out to the specified file in the format specified by the format switch. If not specified the graph picture is written to the clipboard. Note that the SVG format does not support output to the clipboard |
| /format | Picture format used. Choices are:  |  |  | | --- | --- | | wmf | Enhanced metafile format. | | svg | "Scalable Vector Graphics" format. A scalable format compatible across platforms. Not supported in clipboard mode | | jpeg | JPEG format | | png | PNG format | | bmp | Windows bitmap format |  In clipboard mode jpeg, png and bmp do the same thing - that is write an uncompressed bitmapped image of the graph.  If /format is omitted, wmf will be used. |
| /graphid | Write image of specified graph |
| /mark | If specified, markers are displayed on each curve as a means of identification. This is enabled automatically if /mono is specified. |
| /mono | Copy graph in monochromatic form. |
| /transparent | Image is transparent |
| /vp | Two arguments x and y. Specifies viewport dimensions in pixels. This is used to specify the size of the image if a bitmapped format (png, jpeg, bmp) is specified. x is the width, y is the height. |

### Notes

This command makes it possible to export graphs into other windows applications such as word processors. The clipboard is a central store within operating system which is accessible by all applications. Refer to system documentation for more information.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_copyclipgraph) | | |
| [◄ Copy](com_copy.htm) |  | [CopyClipSchem ▶](com_copyclipschem.htm) |
