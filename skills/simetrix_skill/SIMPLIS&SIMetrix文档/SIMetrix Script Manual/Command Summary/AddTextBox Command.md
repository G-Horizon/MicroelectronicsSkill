# AddTextBox Command

Adds a Text Box to the currently selected graph. A text box is an item of text enclosed by a border.

```
AddTextBox [/font <font-name>] [/colour <colour-name>] <text> [ <x-position> [<y-position>]]
```

### Parameters

|  |  |
| --- | --- |
| /colour | Name of colour to be used for text. Name of option setting that will store the colour of the object in the form #rrggbb. Default is GraphColourTextBoxText |
| /font | Name of font to be used for text. This must either be a built in font or one created using CreateFont. Default is "Graph Text Box" |
| /graphid | Id of graph sheet. If omitted the current graph will be used |
| text | Text to be displayed in the box. This may use symbolic value enclosed by '%'. The following are meaningful for Text Box objects:  |  |  | | --- | --- | | %Date% | The date when the object was created | | %Time% | The time when the object was created | | %Version% | The name and current version of the program |  See  [Symbolic Values](applications_graphobjects.htm#applications_graphobjects__symbolicvalues)  for more information on symbolic values. |
| x-position | The x position of the box in view units (See  [Graph Coordinate Systems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ) |
| y-position | The y position of the box in view units (See  [Graph Coordinate Systems](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ) |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addtextbox) | | |
| [◄ AddSymbolProperty](com_addsymbolproperty.htm) |  | [AddTitleBlock ▶](com_addtitleblock.htm) |
