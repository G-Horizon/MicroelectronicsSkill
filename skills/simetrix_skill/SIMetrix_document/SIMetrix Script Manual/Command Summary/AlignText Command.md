# AlignText Command

Aligns the text of a text annotation both within its boundary and externally. Options are left, right or centre aligned.

External alignment refers to the position of the whole object in the schematic and affects how the object will move if the object is resized by changing the text or changing the font size. If left-aligned the top left point of the object will remain fixed while any change in size will extend to the right and downwards. If right-aligned the right top point will be fixed and if centre-aligned the centre top point will be fixed. External alignment can only be applied to free text objects.

Internal alignment refers to the way multi-line text will be displayed within the boundary of the object. Single line text objects are not affected by the internal alignment. Internal alignment may be applied to free text objects and also shape annotations such as rectangles.

### Parameters

|  |  |
| --- | --- |
| /center | Internal centre align |
| /centre | Internal centre align |
| /extbottom | External centre horizontal align, vertical bottom align |
| /extcenter | External centre align |
| /extcentre | External centre align |
| /extleft | External left align |
| /extright | External right align. |
| /left | Internal left align |
| /right | Internal right align |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_aligntext) | | |
| [◄ AddTitleBlock](com_addtitleblock.htm) |  | [Anno ▶](com_anno.htm) |
