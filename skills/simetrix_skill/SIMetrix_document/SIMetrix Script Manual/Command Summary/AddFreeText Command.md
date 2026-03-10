# AddFreeText Command

Adds a free text item to the currently selected graph sheet. Free Text is a graph annotation object. See  [Graph Objects](applications_graphobjects.htm)  for full details.

```
AddFreeText [/font <font-name>] [/colour <colour-name>]  [/align <align>] <text> [<x-pos> [<y-pos>]]
```

### Parameters

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| /align | Integer that specifies alignment of text. Possible values:  |  |  | | --- | --- | | 0 | Left bottom | | 1 | Centre bottom | | 2 | Right bottom | | 8 | Left top | | 9 | Centre top | | 10 | Right top | | 12 | Left middle | | 13 | Centre middle | | 14 | Right middle | |
| /colour | Name of colour to be used for text. Name of option setting that will store the colour of the object in the form #rrggbb. Default is "GraphColourFreeText" |
| /font | Name of font object to be used for text object. This must with the CreateFont command. See  [CreateFont](com_createfont.htm)  for details. Default is "Graph Free Text" |
| /grid | If specified, defines the grid where the text object will be placed. If omitted, text will beplaced on the selected grid |
| /localpos | If set, position is stored relative to a grid. Otherwise it is relative to the whole plotting area. Typically captions are global whereas free text objects are local |
| text | The text to be displayed |
| x-pos | x-co-ordinate of the text in view units (See  [Graph Co-ordinate Systems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ). Default = 0.5. |
| y-pos | y-co-ordinate of the text in view units (See  [Graph Co-ordinate Systems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ). Default = 0.5. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addfreetext) | | |
| [◄ AddFloodFill](com_addfloodfill.htm) |  | [AddGlobalStyle ▶](com_addglobalstyle.htm) |
