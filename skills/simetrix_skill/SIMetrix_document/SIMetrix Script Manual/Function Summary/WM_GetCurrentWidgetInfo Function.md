# WM\_GetCurrentWidgetInfo Function

Returns info of most recently accessed widget (GUI window) of given type

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | Type of widget |

#### Argument 1

Type of widget. Can be one of the following:

* Optimiser
* Symbol Editor
* Ascii File Editor
* Text Editor
* Command Shell
* Data Table
* File View
* Logic Definition Editor
* Netlist Editor
* Waveform Viewer
* Part Selector
* Result Analyser
* Schematic Editor
* Script Editor
* Verilog A Editor
* Verilog HDL Editor
* Web View
* Sensitivity Table

### Returns

8 element array providing the information shown below. The first three entries are specific to the current instance of that type. The remaining elements are general for all widgets of the given type

|  |  |
| --- | --- |
| 0 | Full path name associated with widget |
| 1 | Shortened version of filename |
| 2 | Globally unique reference to this instance |
| 3 | View context name. This is the same as the argument |
| 4 | Main menu name. Can be used to define menus for this widget type |
| 5 | Short version of view context name - used to pass to event scripts |
| 6 | Context menu name - may be empty |
| 7 | tool bar name |

Function returns empty if no widgets of the given type are open

### See Also

* [WM\_GetWidgetInstanceInfo](func_wm_getwidgetinstanceinfo.htm)

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wm_getcurrentwidgetinfo) | | |
| [◄ WM\_GetContentWidgetTypes](func_wm_getcontentwidgettypes.htm) |  | [WM\_GetCurrentWindowName ▶](func_wm_getcurrentwindowname.htm) |
