# XMLSchematicFromWindow Function

Returns an XML definition of the schematic identified by its window id. The window id is a unique reference that may be obtained from a number of script functions.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | window id |

#### Argument 1

Window id as returned by one of thes functions:

* [WM\_GetAllVisibleContentWidgetNames](func_wm_getallvisiblecontentwidgetnames.htm)
* [WM\_GetContentWidgetNames](func_wm_getcontentwidgetnames.htm)
* [WM\_GetContentWidgetsOfType](func_wm_getcontentwidgetsoftype.htm)
* [WM\_GetLastAccessedContentWidget](func_wm_getlastaccessedcontentwidget.htm)

### Returns

Return type: string

XML text description of schematic

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_xmlschematicfromwindow) | | |
| [◄ XMLSchematicFile](func_xmlschematicfile.htm) |  | [XMLToString ▶](func_xmltostring.htm) |
