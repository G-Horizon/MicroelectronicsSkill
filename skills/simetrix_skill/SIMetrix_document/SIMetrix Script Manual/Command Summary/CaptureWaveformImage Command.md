# CaptureWaveformImage Command

Copies a graphical picture of the graph to a file.

### Parameters

|  |  |
| --- | --- |
| /dpi | Defines the assumed DPI setting for creating the graph. Graph objects such as text and lines are sized in physical units (inches, millimeters) not in pixels. By default the image created by this command assumes the DPI (dots-per-inch) setting of the current display. With high resolution displays this can lead to heavy lines and large text if the image size is small. By specifying a fixed DPI a consistent image will be created independent of the system that generated it. A suitable value is 96 for an image of around 512 x 512. For larger images a higher value can be used. |
| /file | Specifies the filename to output to. If omitted, the image will be written to the clipboard |
| /graphid | Write image of specified graph |
| /size | Specifies the size of the image to capture. Values are width and height. |

### Notes

This command writes a graph in PNG format to a file. To write in scalable formats, use the more general  [CopyClipGraph](com_copyclipgraph.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_capturewaveformimage) | | |
| [◄ Cancel](com_cancel.htm) |  | [Cd ▶](com_cd.htm) |
