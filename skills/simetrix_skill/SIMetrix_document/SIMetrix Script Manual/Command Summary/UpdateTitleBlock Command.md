# UpdateTitleBlock Command

Updates the content of a title block.

Uses the currently selected schematic editor with the selected title block.

```
UpdateTitleBlock [/company <company name>] [/title <title name>] [/author <author name>] [/loc <x> <y>]
```

### Parameters

|  |  |
| --- | --- |
| /author | Updated author name. |
| /company | Updated company name. |
| /date | Updated date string, use <<auto>> for assigning the date automatically when the schematic is saved. |
| /force | Use this to force selection of a title block. This will cause the first title block it comes across to be used. Use this if its possible no title block will be selected, for example operating on a file that has been opened by a script call. |
| /layout | Updated layout, either  *Horizontal*  or  *Vertical* . |
| /logo | Updated logo image filename. |
| /notes | Updated notes. Use backslash n to mark new lines within the text. |
| /title | Updated title. |
| /updategiven | Flag that will force an update of only those elements that are defined in the command call. All other items use the values as they are currently. |
| /version | Updated version string, use <<auto>> for assigning the version number automatically when the schematic is saved. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_updatetitleblock) | | |
| [◄ UpdateSystemStyleInfo](com_updatesystemstyleinfo.htm) |  | [UseGlobalStyles ▶](com_useglobalstyles.htm) |
