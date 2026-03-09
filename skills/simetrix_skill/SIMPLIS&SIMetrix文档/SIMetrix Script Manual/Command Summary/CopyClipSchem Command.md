# CopyClipSchem Command

### Parameters

|  |  |
| --- | --- |
| /file | If specified, the schematic is written output in the format specified by the format switch. If not specified the schematic picture is written to the clipboard. |
| /format | Picture format used. Choices are:  |  |  | | --- | --- | | wmf | Enhanced metafile format. (Windows only) | | svg | "Scalable Vector Graphics" format. A scalable format compatible across platforms. Not supported in clipboard mode | | jpeg | JPEG format | | png | PNG format | | bmp | Windows bitmap format |  In clipboard mode jpeg, png and bmp do the same thing - that is write an uncompressed bitmapped image of the graph.  If /format is omitted, wmf will be used. |
| /mono | Copy schematic in monochromatic form. |
| /vp | Viewport dimensions in pixels. This is used to specify the size of the image if a bitmapped format (png, jpeg, bmp) is specified. x is the width, y is the height. |

### Notes

This command makes it possible to export schematics into other windows applications such as word processors. The clipboard is a central store within operating system which is accessible by all applications. Refer to system documentation for more information.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_copyclipschem) | | |
| [◄ CopyClipGraph](com_copyclipgraph.htm) |  | [CopyFile ▶](com_copyfile.htm) |
