# AddTitleBlock Command

Adds a title block to the currently selected schematic.

```
AddTitleBlock [/company <company name>] [/title <title name>] [/author <author name>] [/loc <x> <y>] [/notes <notes>] [/layout <layout>] [/logo <imagedata>] [/date <date>] [/version <version>]
```

### Parameters

|  |  |
| --- | --- |
| /author | The name of the author. |
| /company | The authoring company name. |
| /date | Optional string representing the date. If <<auto>> is used, this will use auto date on saving. |
| /layout | Either 'horizontal' or 'vertical'. |
| /loc | The location on the schematic to place the title block. Two integer arguments, first is x-position, second is y-position. |
| /logo | Full path to an image file to use as the logo image. Only available in the horizontal layout. |
| /notes | Notes about the schematic. Only available in the horizontal layout. The notes section can be long, however you must include a backslash n within the string to indicate where line breaks should happen in the text, otherwise the entire notes section will appear on a single line. |
| /title | The title of the schematic. |
| /version | Optional string representing the version number. If <<auto>> is used, this will use auto version on saving. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addtitleblock) | | |
| [◄ AddTextBox](com_addtextbox.htm) |  | [AlignText ▶](com_aligntext.htm) |
