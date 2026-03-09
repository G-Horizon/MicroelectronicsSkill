# NewLabel Command

Adds a new unplaced text label to a schematic. This is an interactive command, with the label being initially attached to the cursor, unless the `loc` flag is set.

If a style is given, that style is applied. If bold, italics, size, or font are given, a new style is created using those. If style is given as well as a font, size, bold or italics option, the given options will override the existing style and a new style will be created for this element.

```
NewLabel <label-text> [/italics] [/bold] [/font <font-family>] [/size <point-size>] [/style <style-name>] [/repeating] [/loc <x> <y>]
```

### Parameters

|  |  |
| --- | --- |
| /bold | Uses bold. |
| /font | Sets the font family, argument is the name of the font family to use. |
| /italics | Uses italics. |
| /loc | If set, places the label at the given position. |
| /repeating | Causes repeated placement of the label until a cancel request is made (right click or escape press). |
| /size | Sets the font size, argument is point size of the font to use. |
| /style | Sets the name of the style to apply to the label. |
| label-text | The text of the label. Use backslash n to set line breaks within the text. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_newlabel) | | |
| [◄ NewGrid](com_newgrid.htm) |  | [NewLogicDefinitionEditor ▶](com_newlogicdefinitioneditor.htm) |
