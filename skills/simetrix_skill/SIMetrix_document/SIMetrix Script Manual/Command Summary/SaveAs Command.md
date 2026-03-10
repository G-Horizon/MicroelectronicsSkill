# SaveAs Command

Saves the currently selected schematic.

```
SaveAs [/force] [/writeSymbol] [/tab <tabnum>] [/id id] <filename>
```

### Parameters

|  |  |
| --- | --- |
| /ascii | Forces the file to be written in ASCII format. Otherwise the format of the existing file is used (ASCII or XML) or ASCII format if the file doesn't exist. ASCII format is compatible with SIMetrix version 5.0 and later and preserves all features |
| /binary | Forces the file to be written in binary format. Otherwise the format of the existing file is used (ASCII or XML) or ASCII format if the file doesn't exist. Binary format is compatible with SIMetrix versions 4.1 and later but does not preserve all features of the schematic |
| /export | Saves the schematic to specified file but does not change the file, if any, to which the schematic is linked. It also does not update the modified status of the schematic |
| /id | Use id obtained from  [OpenSchematic](func_openschematic.htm)  or  [GetSchematicTabs](func_getschematictabs.htm) |
| /nostyle | If specified, the style library will not be written to the schematic. |
| /tab | Tab id - used to specify which tabbed sheet within a schematic window is to be saved.  *tab\_id*  is a number between zero and 1 less than the number of tabbed sheets in the window. The function  [GetOpenSchematics](func_getopenschematics.htm)  can be used to determine the number of tabs open in a window. |
| /ui | Ignored. This is retained for compatibility with version 7.2 and earlier. This was used in conjunction with /tab to idenify a schematic from a window id and tab id. From version 8, the  [GetOpenSchematics](func_getopenschematics.htm)  function returns all schematics that are open independent of which window, so /ui is no longer required |
| /v25 | Forces the file to be written in binary 2.5 format. Otherwise the format of the existing file is used (ASCII or XML) or ASCII format if the file doesn't exist. Binary 2.5 format is compatible with SIMetrix versions 2.5 and later but is not SIMPLIS compatible and does not preserve all features of the schematic |
| /wid | Use id from:   * [WM\_GetAllVisibleContentWidgetNames](func_wm_getallvisiblecontentwidgetnames.htm) * [WM\_GetContentWidgetNames](func_wm_getcontentwidgetnames.htm) * [WM\_GetContentWidgetsOfType](func_wm_getcontentwidgetsoftype.htm) * [WM\_GetLastAccessedContentWidget](func_wm_getlastaccessedcontentwidget.htm) |
| /writeSymbol | If the schematic being saved has an embedded symbol (that forms part of a hierarchical component), the symbol will be written out if this switch is specified. Otherwise the symbol will not be written out. If  *filename*  already exists and already has a symbol, that symbol will remain intact if this switch is not specified |
| /xml | Forces the file to be written in XML format. Otherwise the format of the existing file is used (ASCII or XML) or ASCII format if the file doesn't exist. XML format is compatible with SIMetrix version 9.1 and later and preserves all features |
| filename | Name of file to which schematic is saved (  *filename*  is not optional as it was with earlier versions of SIMetrix). |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_saveas) | | |
| [◄ Save](com_save.htm) |  | [SaveGraph ▶](com_savegraph.htm) |
