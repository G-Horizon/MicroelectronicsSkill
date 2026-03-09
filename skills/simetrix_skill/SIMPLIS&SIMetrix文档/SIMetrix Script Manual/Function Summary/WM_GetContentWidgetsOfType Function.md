# WM\_GetContentWidgetsOfType Function

Returns content windows of a given type, either in a specific main window or in all windows. Returns a globally unique string identifying the window instance

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | String | Yes |  | View context name |
| 2 | String | No | Use all main windows | Main window |

#### Argument 1

View context name or short name. This following is a full list of names that can be used:

* Optimiser
* Symbol Editor
* Ascii File Editor
* Text Editor
* Data Table
* File View
* License Editor
* Logic Definition Editor
* Netlist Editor
* Waveform Viewer or Graph
* Part Selector
* Result Analyser
* Schematic Editor or Schematic
* Script Editor
* Verilog A Editor
* Verilog HDL Editor
* Web View
* Sensitivity Table

#### Argument 2

Main window

### Returns

Return type: string array

Globally unique id

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_wm_getcontentwidgetsoftype) | | |
| [◄ WM\_GetContentWidgetsLayout](func_wm_getcontentwidgetslayout.htm) |  | [WM\_GetContentWidgetTypes ▶](func_wm_getcontentwidgettypes.htm) |
