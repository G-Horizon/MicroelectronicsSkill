# AddLegend Command

Adds a legend box to the currently selected graph. A "Legend Box" is a graph annotation object which consist of a rectangle containing a list of curve labels. See  [Graph Objects](applications_graphobjects.htm)  for more information.

```
AddLegend [/autowidth] [/rowcount <row-count>] [/font <font-name>] [/colour <colour-name>] [<label> [<x-pos> [<y-pos> [<width> [<height>]]]]] [/graphid id]
```

### Parameters

|  |  |
| --- | --- |
| /autoWidth | If specified, the size of the box will be adjusted automatically according to its contents. The layout is influenced by the rowcount value |
| /colour | Name of colour to be used for text. Name of option setting that will store the colour of the object in the form #rrggbb. Default is "GraphColourLegendBox" |
| /font | Name of font object to be used for text object. This must with the CreateFont command. See  [CreateFont](com_createfont.htm)  for details. Default is "Legend Box" |
| /graphid | Id of graph sheet. If omitted the current graph will be used |
| /rowcount | Specifies the number of rows that will be used to lay out the contents of the box. The default is 4. The contents will be laid out using rowcount or less if possible but more rows will be used if required |
| label | This is the text that will copied to each entry. To be meaningful this must contain a symbolic value enclosed by '%'. Symbolic values for graph objects are explained more fully on  [Symbolic Values](applications_graphobjects.htm#applications_graphobjects__symbolicvalues) . The default value for label if omitted if %DefaultLabel%. This will result in the curves name and measurements being displayed in the legend box. Some alternatives are:  |  |  | | --- | --- | | %Curve:Label% | displays just the label with no measurements | | %Curve:Measurements% | displays just the measurements | | %Curve% | displays the curve's ID only | | %Curve:Label%/%Curve:YUnit% | displays the curve name and y-axis units | |
| x-pos | X position of box in view units (See  [Graph Coordinate System](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ). If the value is 1.0 or greater, the box will be placed such that its left hand edge is to the right of the graph's grid area. Default = 0. |
| y-pos | Y position of box in view units (See  [Graph Coordinate System](applications_graphobjects.htm#applications_graphobjects__graphcoordinatesystems)  ). If the value is 1.0 or greater, the box will be placed such that its bottom edge is above the graph's grid area. Default = 1.02 |
| width | Physical width of box in mm. Note that this value will be ignored if /autowidth is specified. Default = 50. |
| height | Physical height of box in mm. ote that this value will be ignored if /autowidth is specified. Default = 50.Default = 15mm |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addlegend) | | |
| [◄ AddImageScript](com_addimagescript.htm) |  | [AddLegendProp ▶](com_addlegendprop.htm) |
