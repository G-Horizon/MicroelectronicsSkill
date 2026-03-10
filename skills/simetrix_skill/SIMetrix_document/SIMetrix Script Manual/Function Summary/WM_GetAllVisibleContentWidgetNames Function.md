# WM\_GetAllVisibleContentWidgetNames Function

Returns content windows of a given type, that are currently visible. Returns a globally unique string identifying the window instance

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | View context name |

#### Argument 1

View context name or short name. This is a name describing the type of window. The following is a full list:

* Optimiser
* Symbol Editor
* Ascii File Editor
* Text Editor
* Data Table
* File View
* License Editor
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

Return type: string array

Globally unique id

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wm_getallvisiblecontentwidgetnames) | | |
| [◄ WM\_CanRevertToSaved](func_wm_canreverttosaved.htm) |  | [WM\_GetCentralWidgetGeometry ▶](func_wm_getcentralwidgetgeometry.htm) |
