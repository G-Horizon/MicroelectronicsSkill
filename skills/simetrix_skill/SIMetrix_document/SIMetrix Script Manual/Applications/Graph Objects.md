# Graph Objects

In this topic:

## Overview

Graph objects are the items displayed in a graph window. These include curves, axes, cursors and the various objects used for annotation. All graph objects possess a number of named properties all of which may be read and some may also be written. Each graph object also has a unique id which is used to identify it.

A knowledge of the inner workings of graph objects will be useful if you wish to customise some of the annotation features provided by the waveform viewer. However, the interface is at a low level with much work carried out by internal scripts. Consequently there is quite a steep learning curve to climb in order to make good use of the features available.

## Object Types

The following table lists all the available object types:

|  |  |
| --- | --- |
| **Object Name** | **Description** |
| Axis | Axes and grids |
| Crosshair | Crosshair part of cursor |
| CrosshairDimension | Object used to dimension cursors. Forms part of cursor. Cannot be displayed on its own |
| Curve | Curve |
| CurveData | Curve data object. Each curve has one or more associated curve data objects. These store the curve data. Curve history is stored in curve data objects |
| CurveMarker | Marker used to annotate curves |
| FreeText | Free Text annotation object. Displays unboxed text on graph |
| Graph | Graph sheet |
| Grid | Grid object |
| Histogram | Histogram plot |
| LegendBox | Box enclosing LegendText objects |
| LegendText | Text objects used in legend boxes and linked to a displayed curve. |
| Measurement | Measurement object used to display curve measurements in the measurement window |
| SharedAxis | X-Axis connector object. X-Axes that are linked, that is have common limits, are linked using a SHaredAxis object |
| ScaterPlot | Scatter plot |
| SmallCursor | The small cursor that permanently follows the mouse cursor and tracks the nearest curve. There is only ever one of these on each Graph sheet |
| TextBox | Box enclosing FreeText object |

## Properties

Properties are the most important aspect of graph objects. Each type of graph object possesses a number of properties which determine characteristics of the object. Some properties are read only and are either never altered or can only be altered indirectly. Other properties can be changed directly using the command [SetGraphAnnoProperty](com_setgraphannoproperty.htm). The labels for curves, axes and the various annotation objects are examples of properties that may be edited.

A full list of all object types and their properties is given in  [Objects and Their Properties](applications_graphobjects.htm#applications_graphobjects__objectsandtheirproperties) .

## Graph Object Identifiers - the "ID"

Each instance of a graph object is uniquely identified by an integer value known as its "ID". Valid IDs always have a value of 1 or greater. IDs are returned by a number of functions (see below) and also a number of the objects possess properties whose value is the ID of a related object.

Once the ID of an object has been obtained, its property names can be read and it property values may be read and/or modified.

The following functions return graph object IDs. Note that all functions return object IDs belonging to the currently selected graph only except for [GetGraphObjects](func_getgraphobjects.htm) which can optionally return IDs for objects on a specified graph.

|  |  |
| --- | --- |
| [AddGraphCrossHair](func_addgraphcrosshair.htm) | Add a new cursor to the currently selected graph and return its and its dimension's Ids |
| [GetAllCurves](func_getallcurves.htm) | Returns the IDs for all curves in the current graph |
| [GetAllAxes](func_getallaxes.htm) | Returns the IDs for all axes (X and Y) in current graph |
| [GetAllXAxes](func_getallxaxes.htm) | Returns the IDs for all X-axes in current graph |
| [GetAllYAxes](func_getallyaxes.htm) | Returns the IDs for all Y-axes in current graph |
| [GetAxisCurves](func_getaxiscurves.htm) | Returns IDs for all curves attached to specified axis (X or Y) in the current graph |
| [GetCurrentGraph](func_getcurrentgraph.htm) | Returns the ID for the currently selected graph sheet |
| [GetCursorCurve](func_getcursorcurve.htm) | Returns information about curve attached to the main cursor including its ID |
| [GetCurveAxis](func_getcurveaxis.htm) | Returns ID of y-axis associated with a curve in the current graph. |
| [GetCurveAxes](func_getcurveaxes.htm) | Returns IDs for x and y axes associated with a curve in the current graph |
| [GetDatumCurve](func_getdatumcurve.htm) | Returns information about curve attached to the reference cursor including its ID |
| [GetGraphObjects](func_getgraphobjects.htm) | Returns all objects on a graph, or objects of a specified type |
| [GetGraphTabs](func_getgraphtabs.htm) | Returns ids for all graph sheets |
| [GetGridAxes](func_getgridaxes.htm) | Returns ids for all axes belonging to the specified Grid |
| [GetSelectedCurves](func_getselectedcurves.htm) | Returns IDs of all selected curves in the current graph |
| [GetSelectedGraphAnnotations](func_getselectedgraphannotations.htm) | Returns the ID for all selected graph annotation objects |
| [GetSelectedGrid](func_getselectedgrid.htm) | Returns ID of the currently selected Grid object in the current graph |
| [GetSelectedXAxis](func_getselectedxaxis.htm) | Returns the ID of the selected X-axis in the current graph |
| [GetSelectedYAxis](func_getselectedyaxis.htm) | Returns the ID of the selected Y-axis in the current graph |
| [SelGraph](func_selgraph.htm) | Returns the id of the selected graph |
| [GetGridCurves](func_getgridcurves.htm) | Returns ids of all curves in the specified Grid |
| [CreateGraphMeasurement](func_creategraphmeasurement.htm) | Creates a graph measurement object and returns its ID |
| [FindGraphMeasurement](func_findgraphmeasurement.htm) | Returns the id of a graph measurement object defined by its associated curve and its label |
| [GetGraphObjPropValue](func_getgraphobjpropvalue.htm) | function |
| [CreateSharedAxisConnector](func_createsharedaxisconnector.htm) | Creates a SharedAxis object and returns its ID |

Some of the functions in the above list are technically redundant. For example the value obtained by [GetCurveAxis](func_getcurveaxis.htm)() can also be obtained by reading the value of the 'Y-axis' property of the curve.

## Symbolic Values

Some properties used for labels may be given symbolic values. Symbolic values consist of a property name enclosed with the '%' character. When the label is actually displayed the property name is replaced with its value.

Symbolic values may also be indirect. Some properties return the id of some other associated object and the value of a property for that object may be referenced with a symbolic value. The ':' character is used to denote indirect symbolic values. For example, this method is used with curve markers. The default value for a curve marker's label is:

```
%curve:label%
```

`curve` is a property of a curve marker that returns the id of the curve that it points to. `label` is a property of a curve that returns the label assigned to it. So `curve:label` returns the label of the curve that the curve marker points to.

Other curve properties can be used for this label. For example, curve measurements (as displayed below the legend in the legend panel) can also be accessed via property named "measurements". So the curve marker label:

```
%curve:label% %curve:measurements%
```

would display the curve's name followed by its measurements.

Finally the character sequence `<n>` can be used to denote a new line.

## Objects and Their Properties

The following lists all the properties available for all objects. Note that all objects have a 'Type' property that resolves to the object's type name. Also all objects except Graph have a 'Graph' property that returns the ID of the object's parent graph sheet.

### Axis

Axis objects represent both x and y graph axes.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| AutoLimit | 'On' or 'Off' determines whether axis limits are adjusted automatically according to attached curves | No |
| AxisType | 'X', 'Y' or 'Dig' | Yes |
| Curves | String array property returns all curve IDs attached to this axis | Yes |
| DefaultLabel | Label property is given default value of %DefaultLabel% which resolves to the value of this property. | Yes |
| DefaultUnit | Unit property is given default value of %DefaultUnit% which resolves to the value of this property. | Yes |
| Delta | Value that determines the minor grid line spacing | No |
| ExpandToFitLabel | Boolean, default = 'true'. If 'true' axis size will expand to fit its label | No |
| Grad | Grading of axis: "Log" or "Lin". | No |
| Graph | ID of parent graph | Yes |
| Grid | ID of parent grid | Yes |
| GUID |  | Yes |
| ID | ID of this object | Yes |
| Label | Label used to annotate axis. (Actual displayed text is \textlangle label\textrangle / \textlangle unit\textrangle). Default = %DefaultLabel% | No |
| Max | Maximum limit of axis | No |
| Min | Minimum limit of axis | No |
| Name | Axis name. ('Y1', 'Y2' etc.). Empty for X and Dig axes | Yes |
| ProbeId | Value used by fixed probes to identify axes | No |
| SharedId | ID of SharedAxis object. Only meaningful for x-axes and used to connect x-axes | No |
| Type | Type of object - always 'Axis' | Yes |
| VertOrder | Vertical order. Arbitrary string used to specify vertical display order | Yes |
| Unit | Physical units of axis. (E.g. 'V', 'A' etc.). Default = %DefaultUnit% | No |

### Crosshair

Object used to display cursor. Each graph cursor consists of a Crosshair and two CrosshairDimensions.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| COM1 | Common reference value. Only meaningful with X-Y plots such as Nyquist plots. Shows the value of the common reference to X and Y. This is frequency in a Nyquist plot | Yes |
| Dimensions | Comma delimited string providing the dimension objects attached to this cursor | Yes |
| Graph | ID of parent graph | Yes |
| ID | ID of this object | Yes |
| Point | 1 = Reference cursor. 2 = Main cursor | Yes |
| Type | Type of object - always 'Crosshair' | Yes |
| XDimension | The ID for the CrosshairDimension object that displays the X dimension and positions | Yes |
| YDimension | The ID for the CrosshairDimension object that displays the Y dimension and positions | Yes |
| Colour | RGB colour value, or option setting that holds an RGB value. Default=GraphColourCrossHair (option value) | No |
| Curve | ID of attached curve | No |
| Division | Division index of attached curve. See page for details on multi-division vectors | No |
| Frozen | 'On' or 'Off'. If 'On' the user will not be able to move the cursor with the mouse | No |
| Hidden | Boolean. Set to 'true' to hide cursor | No |
| Label | Cursor label displayed at base | No |
| LineStyle | Style of line used for crosshair. Comma delimited string of numbers representing mark-space values. E.g. '1,1' defines short evenly spaced dots, '3,1,1,1' defines a dotdash style | No |
| Style | Style of crosshair. Possible values: 'Crosshair' or 'Cursor'. 'Crosshair' means the object is displayed as a crosshair with a width and height that extends to cover the whole grid. 'Cursor' means that the object is a small bitmap representing a cross. | No |
| X1 | X data value of crosshair position | No |
| Y1 | Y data value of crosshair position. The value can be written but this can only affects nonmonotonic curves where there are multiple y crossings at a given x value. | No |

### CrosshairDimension

Object used to display the dimensions and positions of cursors. There are two types, namely horizontal and vertical.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curve1 | ID of curve attached to crosshair 1 | Yes |
| Curve2 | ID of curve attached to crosshair 2 | Yes |
| Graph | ID of parent graph | Yes |
| GUID |  | Yes |
| ID | ID of this object | Yes |
| Type | Type of object - always 'CrosshairDimension' | Yes |
| Vertical | 0 = Horizontal dimension, 1 = Vertical dimension | Yes |
| X1 | Horizontal type only. Holds the value of the x data position of the first crosshair. | Yes |
| X2 | Horizontal type only. Holds the value of the x data position of the second crosshair | Yes |
| Y1 | Vertical types only. Holds the value of the y data position of the first crosshair | Yes |
| Y2 | Vertical types only. Holds the value of the y data position of the second crosshair and is readonly | Yes |
| XDiff | = X2-X1 | Yes |
| YDiff | = Y2-Y1 | Yes |
| Crosshair1 | ID of crosshair 1 | No |
| Crosshair2 | ID of crosshair 2 | No |
| Font | Font used to display labels. Can either be the name of a font object or a font spec as returned by [GetFontSpec](func_getfontspec.htm). | No |
| Hidden | Boolean. If 'true', dimension object will be hidden | No |
| Label1 | Label positioned to depict value of first crosshair. Default = %x1% for horizontal types, %y1% for vertical. | No |
| Label2 | Label positioned to depict value of second crosshair. Default = %x2% for horizontal types, %y2% for vertical. | No |
| Label3 | Label positioned to depict the separation between crosshairs. Default = %XDiff% for horizontal types, %YDiff% for vertical. | No |
| Style | Controls display of dimension labels. Possible values: |  |  | | --- | --- | | Internal | Show difference only (label3) - internal position | | External | Show difference only (label3) - external position | | Auto | Show difference only (label3), position chosen automatically | | P2P1 | Show absolute labels (label1 and label2) | | P2P1Auto | Show all labels. Difference position chosen automatically | | None | No controls selected | | No |

### Curve, Histograms and Scatter Plots

The following properties are common to Curves, Histograms and Scatter Plots. In the following properties table, the object is referred to as a Curve but definitions apply equally to Histograms and Scatter Plots.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Analysis | Analysis type used to create curve's data | Yes |
| DefaultLabel | This is composed from Name, Suffix and GroupName to form a text string that is the default label for the curve | Yes |
| Expression | Expression that created this curve | Yes |
| Graph | ID of parent graph | Yes |
| Grid | ID of parent Grid | Yes |
| GroupName | The data group that was current when the curve was created | Yes |
| ID | ID of this object | Yes |
| Limits | The X an Y limits of the curve in the form `[xmin, xmax, ymin, ymax]` | Yes |
| MeasurementIds | String array. List of Measurement object IDs associated with this curve object | Yes |
| Measurements | Measurements added to a curve | Yes |
| MeasureSpec | String defining measurements for the curve. This is set for curves created by fixed probes. (.GRAPH statements) | Yes |
| NumDivisions | Number of divisions in curves data. I.e. the number of separate traces in a group of curves. Groups of curves are usually produced by Monte Carlo analyses | Yes |
| ShortLabel | A label composed from Name and Suffix but without group name | Yes |
| SweepType | For grouped curves, defines the type of sweep that created the group. Values are 'Statistical' for Monte Carlo analyses, 'Stepped' for stepped analyses or 'None' for non-grouped curves. F | Yes |
| Type | Type of object - 'Curve', 'Histogram' or 'ScatterPlot' | Yes |
| UserProbeID | Used by measurements for fixed probes (.GRAPH statements) | Yes |
| XPhysType | Physical type of curves x-values | Yes |
| XAxis | ID of x-axis attached to curve | Yes |
| XExpression | Expression that defines X-values | Yes |
| XUnit | Physical type of curve's x-data | Yes |
| XY | Boolean value. 'true' if curve created from X-Y data | Yes |
| YAxis | ID of y-axis attached to curve | Yes |
| YPhysType | Physical type of curves y-values | Yes |
| YUnit | Physical type of curve's y-data | Yes |
| Hidden | Boolean. If 'true' curve will not be visible. (Inverse of Visible property) | No |
| Highlight | Boolean. Curve is highlighted if 'true'. | No |
| HighlightedDivisions | Controls selective highlighting of grouped curves. Stores a list of divisions that are highlighted in form [div1, div2, ...]. E.g. [1,5,7] would highlight divisions 1 5 and 7 | No |
| Label | The curve's label. This is the text that appears in the legend panel. This can use a symbolic constant and in fact defaults to %DefaultLabel%. Note that when reading back a symbolic value assigned to this property, the resolved value will be returned | No |
| Name | The curve's base name. This is the value passed to the `/name` switch of the Curve/Plot command or the name of the vector plotted if no `/name` switch is supplied. | No |
| ProbeGUID | GUID originating from probe that created curve. If the curve is created from a .GRAPH statement in the netlist, this will be the value of the GUID parameter. If created using a Curve or Plot script command this can be set using the /guid switch. This feature is currently used to implement auto probe colouring | Yes |
| ProbeInst | Used by fixed probes (.GRAPH statement) to manage curve history | No |
| RGBColour | Colour of curve. Can be entered as value returned from [GetColourSpec](func_getcolourspec.htm) or using format #rrggbb where rr, gg and bb are two digit hex values representing the red, green and blue colour content respectively | No |
| Selected | Boolean - holds selected state of curve | No |
| Sequence | Integer value that is used to define default colour. The actual colour used may be set globally using options dialog box | No |
| Suffix | This is assigned when the result of a multistep analysis is plotted to give information about the step. E.g. if you stepped a resistor value the suffix would hold the name and value of the resistor at the step. | No |
| UseSequenceColour |  |  |
| Visible | If 'false', curve will be hidden, but its legend display will remain | No |

### Curve Only

The following properties apply to Curves only, i.e they do not apply to Histograms or Scatter Plots.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Alpha | Alpha blend ratio as a percentage. 0=invisible, 100=fully opaque | No |
| CurveDatas | String array. List of curve data objects associated with this Curve. Note that this returns all CurveData objects available, not just the ones that are visible | Yes |
| DisplayType | May be: |  |  | | --- | --- | | 'analog' | curve is regular analog trace | | 'decimal' | bus display showing decimal values | | 'hex' | bus display showing hexadecimal values | | 'binary' | bus display showing binary values | | No |
| ForceFastRender | Boolean. If set, unconditionally inhibits use of anti-alias with pixel width greater than 1. This combination renders slowly and is automatically disabled for large curves | No |
| LineStyle | Controls line style. May have values as defined below |  |  | | --- | --- | | 'auto' | Solid for main curve. History curves are set to broken lines in order dot, dash, dot-dash | | 'solid' | solid | | 'dot' | dotted | | 'dash' | dashed | | 'dotdash' | dot-dash | | No |
| Persistence | Integer. History depth display. Previous curve content may be displayed up to the depth defined by this property | No |
| ShowPoints | If 'true' data point markers will be displayed | No |

### CurveData

CurveData objects store the data associated with a curve. A curve can have more than one curve data object associated with it.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curve | ID of Curve associated with this CurveData object | Yes |
| Graph | Parent Graph ID | Yes |
| GUID |  | Yes |
| ID | ID ofthis object | Yes |
| Type | Type of this object - always CurveData | Yes |
| LineStyle | |  |  | | --- | --- | | 'auto' | Style chosen according to position in history | | 'solid' | solid | | 'dot' | dotted | | 'dash' | dashed | | 'dotdash' | dot-dash | | No |

### CurveMarker

An object used to title a curve or mark a feature.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Division | Division index of attached curve | Yes |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| Type | Type of object - always 'CurveMarker' | Yes |
| Colour | Background colour | No |
| Curve | ID of attached curve | No |
| Font | Font for label | No |
| FontColour | Text colour | No |
| Hidden | Boolean. If 'true' curve marker will be hidden | No |
| Label | Label of curve marker. May be a symbolic value. Default is %curve:label% which returns the label of the attached curve | No |
| SnapToCurve | 'On' or 'Off'. If 'On' marker tracks attached curve i.e its y position is determined by the y value of the curve at the marker's x position. If 'Off' marker may be freely located. | No |
| X1 | X-data value at arrowhead | No |
| Y1 | Y-data value at arrowhead | No |
| X2 | X position of label in view units relative to arrowhead | No |
| Y2 | Y position of label in view units relative to arrowhead | No |

### FreeText

Free text objects are items of text with no border or background that are not attached to any other object.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Date | Date that the object was created. If the object is on a graph that has been saved to a file then subsequently restored, the date will be the date that the object was originally created. | Yes |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| Parent | ID of parent object. If text is placed freely on the graph, this will be the same as the Graph property. FreeText objects. however are also used in TextBoxes in which case this returns the id for the TextBox | Yes |
| Time | Time that the object was created. If the object is on a graph that has been saved to a file then subsequently restored, the time will be the time that the object was originally created. | Yes |
| Type | Type of object - always 'FreeText' | Yes |
| Version | Product name and version | Yes |
| Alignment | String to define alignment: |  |  | | --- | --- | | 'LeftTop' |  | | 'LeftBottom' |  | | 'LeftMiddle' |  | | 'LeftAuto' |  | | 'RightTop' |  | | 'RightBottom' |  | | 'RightMiddle' |  | | 'RightAuto' |  | | 'CentreTop' |  | | 'CentreBottom' |  | | 'CentreMiddle' |  | | 'CentreAuto' |  | | 'AutoTop' |  | | 'AutoBottom' |  | | 'AutoMiddle' |  | | 'AutoAuto' |  |  The 'Auto' alignment options align according to the position of the object in the grid. X1=0 aligns to left, X1=1 aligns to right, Y1=0 aligns to bottom, Y1=1 aligns to top.     The Centre values may use the alternative Center spelling. | No |
| Font | Font for label | No |
| FontColour | Text colour | No |
| GlobalPosition | Boolean. If true, the position defined by X1 and Y1 will be relative to the entire graph drawing area. Otherwise it is relative to the Grid specified by the Grid property | No |
| Grid | ID for grid used for local position | No |
| Hidden | Boolean. If 'true', object will be hidden | No |
| Label | Text displayed. Symbolic values may be used. E.g. %Time% will display the time the object was created. | No |
| X1 | X location of object in view units. The Alignment, Grid and GlobalPosition affect the interpretation of this value | No |
| Y1 | Y location of object in view units. The Alignment, Grid and GlobalPosition affect the interpretation of this value | No |

### Graph

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| DefaultRef | The name of the reference vector (x-values) for the first curve added to the graph. Typically this would be 'Time' or 'Frequency' for typical transient and AC analyses respectively. The property is used to manage shared x-axes | Yes |
| DefaultSharedAxis | ID of the SharedAxis object used to connect x-axes. There can be any number of SharedAxis objects but there is always a single SharedAxis object that new x-axes are connected to. This may be read from this property | Yes |
| FirstCurve | ID of the oldest curve on the graph | Yes |
| Graph | ID of this object | Yes |
| Grids | String array. IDs of all grids in the graph | Yes |
| GroupTitle | Title of the data group that was current when the graph was created | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| SmallCursor | ID of the SmallCursor object | Yes |
| SourceGroup | The data group that was current when the graph was created | Yes |
| Type | Type of object - always 'Graph' | Yes |
| AcceptNewProbes | Boolean. If 'true', graph will accept curves created by fixed probes even if it was initially used for random probes. Usually fixed probes create a new graph sheet on the first run | Yes |
| CursorStatusDisplay | Sets method of displaying cursor positions and dimensions. Possible values: |  |  | | --- | --- | | Graph | Display on graph using CrosshairDimension object | | StatusBar | Display on status bar | | Both | Display on graph and status bar | | No |
| MainCursor | ID of Crosshair object comprising the main cursor. Value = -1 if cursors are not enabled. | Yes |
| Path | Path of file to save to. This is the file that will be used by the "File|Save" menu. When saving a graph, this property will be set to the full path name of the file. When a graph file is loaded, this property is set to the full path of the input file. (Note that this does not apply to graphs converted from the old binary format) | Yes |
| ProbeId | Used to manage fixed probes | No |
| RefCursor | ID of Crosshair object comprising the reference cursor. Value = -1 if cursors are not enabled. | Yes |
| TabTitle | The text in the title of the tabbed sheet. This can be symbolic. Default is %SourceGroup% %FirstCurve:Label% | No |
| TitleBar | Text to be displayed in the graph window title bar when the graph's sheet is in view. This may be symbolic. Default is %SourceGroup% (%GroupTitle%) | No |
| Visible | Boolean value set to TRUE if the graph is currently visible or partially visible. This property will be FALSE if the graph window is iconised or obscured by other windows | Yes |

### Grid

Grids are where curves are displayed and have at least one y-axis and one x-axis. There may be one or more grids in a graph.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curves | String array. | Yes |
| Graph | Parent graph ID | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| ProbeId | Used to manage fixed probes | Yes |
| SelectedYAxis | ID of the selected y-axis | Yes |
| Type | Object type. Always set to 'Grid' | Yes |
| XAxes | String array. IDs of all x-axes attached to the grid | Yes |
| YAxes | String array. IDs of all y-axes attached to the grid | Yes |
| GridType | 'Norm' (normal) or 'Dig' (digital). Digital axes are small and designed for digital traces, although they can be used for any curve | No |
| VertOrder | Integer. Defines vertical position of grid. For normal (non-digital) grids the grids are displayed in order bottom to top - the higher the value of VertOrder the higher up the display. The order for digital grids is the reverse of this | No |

### LegendBox

The LegendBox is used to display labels for every curve on the graph sheet. It consists of a box that is loaded with LegendText objects - one for each curve on the graph. The LegendText objects are automatically loaded when a curve is added to the graph and automatically deleted when a curve is deleted.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID | Yes |
| Objects | Semicolon delimited string providing the IDs for each of the LegendText objects defining text entries in the box | Yes |
| Type | Type of object. Always 'LegendBox' | Yes |
| Alignment | See Alignment property of FreeText object ([FreeText](applications_graphobjects.htm#applications_graphobjects__objectsandtheirproperties_freetext)) | No |
| AutoWidth | 'On' or 'Off'. If 'On' the width and height of the box automatically adjust according to contents. Otherwise the X2 and Y2 values may be adjusted to set the box dimensions | No |
| Colour | Background colour | No |
| Font | Text font | No |
| FontColour | Text colour | No |
| LegendLabel | Text of label that is loaded into box when a curve is added to the graph. This can be symbolic in which case it references properties of the LegendText object that displays the text. The default value is %DefaultLabel% | No |
| Hidden | Boolean. If 'true' object will be hidden | No |
| X1 | X position in view units | No |
| X2 | Width of box in mm if AutoWidth set to off | No |
| Y1 | Y position of box in view units | No |
| Y2 | Height of box in mm if AutoWidth set to off | No |

### LegendText

LegendText objects are used to load legend boxes and cannot be instantiated independently.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curve | ID of attached curve | Yes |
| Date | Date that the object was created. If the object is on a graph that has been saved to a file then subsequently restored, the date will be the date that the object was originally created. | Yes |
| DefaultLabel | The default value for the label. Actually equivalent to %Curve:Label%\textlangle n\textrangle%Curve:Measurements%. (\textlangle n\textrangle denotes a new line). | Yes |
| Division | For grouped multi-step curves there is a LegendText object for each division. The divison index may be read from this property | Yes |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| Parent | ID of parent legend box | Yes |
| Time | Time that the object was created. If the object is on a graph that has been saved to a file then subsequently restored, the time will be the time that the object was originally created. | Yes |
| Type | Type of object - always 'LegendText' | Yes |
| Version | Product name and version | Yes |
| Font |  | No |
| Label | Set to the value of the legend box's LegendLabel property when it is added to the box | No |

### Measurement

Measurement objects are displayed in the measurement window and are created when a measurement is made on a curve. The display in the measurement window has three columns showing the label of the associated curve, the measurement name and the measurement value.

For measurements made on multi-division data generated by multi-step runs, the measurement object has child objects that display additional data relevant for the multi-step analysis.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curve | ID of associated curve | Yes |
| DivisionLabel | String array. If Expression evaluates to a multi-division vector, this property will hold its division labels. Typically these are the labels associated with each step in a multi-step run. For example, if a resistor is swept, each division label will be in the form 'Rxx=value' | Yes |
| Graph | ID of parent Graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| MultiDivLabels | String array. Multi division labels displayed in the measurement window. This depends on the value of the MultiDivMode property. See MultiDivMode property for further details | Yes |
| MultiDivValues | String array. Multi division values displayed in the measurement window. This depends on the value of the MultiDivMode property. See MultiDivMode property for further details | Yes |
| NumDivisions | Number of divisions in the evaluated Expression | Yes |
| RawValues | String array. Raw result of evaluating Expression without any formatting or statistical collation | Yes |
| Statistics | String array. Statistics values | Yes |
| Statistics\_Names | String array. Same size as Statistics property. Parameter names for statistics values | Yes |
| Type | Object type. Always set to 'Measurement' | Yes |
| Value | String Array. Similar to RawValues but with the Template applied | Yes |
| Expression | Expression to be evaluated. Typically this would refer to the data from the associated curve using the expression 'cv(%curve%)' but this is not compulsory. | No |
| Label | Label displayed in the Label column | No |
| MultiDivMode | Mode for the display of multi-division data. Multi-division data is generated by multi-step runs such as parameter sweeps and Monte Carlo runs. For such runs there are two ways to display the measurement data: multiple and statistical. In multiple mode, an individual measurement is displayed for each division in the data; divisions correspond to step in a multi-step run. In statistical mode, statistical information is calculated such as mean, standard deviation, minimum and maximum.    The valid values for this property are |  |  | | --- | --- | | Curve | The mode (multiple or statistical) is obtained from the curve data itself | | Multiple | multiple mode | | Statistics | statistical mode | | AdvancedStatistics | statistical mode - additional statistical values are included. Currently this includes Skewness and Kurtosis |     This property controls the data that is actually displayed in the measurement window. | No |
| Template | Template applied to raw values to obtain the displayed values. This can be any text string including special values as shown below |  |  | | --- | --- | | %y*n*% | Where *n* is any integer 1 or higher. y1 returns the y-value result of the expression. If the expression evaluates to an array, y2 returns the second element, y3 the third etc. | | %x*n*% | As %y*n*% but returns x values | | %uy1% | The units for the y-values | | %ux1% | The units for the x-values | | No |

### SharedAxis

The SharedAxis object is used to connect x-axes. X-axes on the same graph are initially connected so that they share most of their properties, in particular their limits. So when one x-axis is zoomed, other connected x-axes change their zoom accordingly.

X-Axes always point to a SharedAxis object through their SharedId property. X-Axis that share the same SharedId will be connected.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| ConnectedAxes | String array. List of axes connected to this object | Yes |
| Graph | ID of parent graph object | Yes |
| GUID | GUID | Yes |
| ID | ID | Yes |
| Type | Type of this object. Always 'SharedAxis' | Yes |

### SmallCursor

The SmallCursor is a cursor that follows the mouse cursor but tracks displayed curves providing an X and Y readout of the curve's data. There is only ever one SmallCursor object in each graph.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Curve | ID of curve that the cursor is currently tracking | Yes |
| Division | Division index of curve that the cursor is currently tracking | Yes |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| Type | Type of object. Always 'SmallCursor' | Yes |
| X1 | Current x-position | Yes |
| Y1 | Current y-position | Yes |
| Hidden | Boolean. If 'true' cursor will not be visible | No |

### TextBox

A TextBox consists of a border with a definable background colour into which a FreeText object may be added. TextBox is also the basis of the LegendBox object.

|  |  |  |
| --- | --- | --- |
| **Name** | **Description** | **Read Only?** |
| Graph | ID of parent graph | Yes |
| GUID | GUID | Yes |
| ID | ID of this object | Yes |
| Type | Type of object - always 'TextBox' | Yes |
| Alignment | See Alignment property of FreeText object ([FreeText](applications_graphobjects.htm#applications_graphobjects__objectsandtheirproperties_freetext)) | No |
| Colour | Background colour. Either the name of a colour object or a colour specification. | No |
| Font | Font used for text objects added to the box. In practice this only affects the LegendBox object which is based on TextBox. | No |
| FontColour | Colour used for text. Either the name of a colour object or a colour specification |  |
| Grid | ID of Grid where object is located. Position values X1 and Y1 are relative to this grid | No |
| Hidden | Boolean. If 'true' object will be hidden | No |
| Label | Text displayed in box | No |
| X1 | X location of object in view units | No |
| Y1 | Y location of object in view units | No |
| X2 | Physical width of box in mm | Yes |
| Y2 | Physical height of box in mm | Yes |

## Graph Co-ordinate Systems

Three different units of measure are used to define the location and dimensions of an object on a graph sheet. These are 'View units', 'Physical units' and 'Data units'. These are explained as follows:

'Physical Units' relate to the physical size of the displayed object and have units of millimetres. Physical units are only used for dimensions of some annotation objects and are not used for location. When objects are displayed on a screen an assumption is made for the number of pixels per inch. This depends on the display driver but is typically in the range 75 - 100.

'Data Units' relate to the units of the X and Y axes. Typically an object such as curve marker is located using data units so that it always points to the same point on a curve regardless of how the graph is zoomed or scrolled.

'View Units' relate to the current viewable area of the graph. View units use a coordinate system whereby the bottom left of the grid area is co-ordinate (0,0) and the top right corner of the grid is co-ordinate (1,1). View units are used to define the location of objects that need to be at a fixed location on the graph irrespective of zoom magnification.

|  |  |  |
| --- | --- | --- |
| [◄ Data Import and Export](applications_dataimportexport.htm) |  | [Event Scripts ▶](applications_eventscripts.htm) |
