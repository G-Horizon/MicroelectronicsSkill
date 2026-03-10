# AddGlobalStyle Command

Adds an additional global style to the available styles.

This will overwrite any styles with the same name unless the `nooverride` flag is set.

```
AddGlobalStyle 
        [/lineType <type>] [/lineColour <colour>] [/lineThickness <thickness>] [/fontName <name>] [/fontSize <size>] [/fontColour <colour>] [/italics /bold 0|1] [/overline 0|1]
        [/underline 0|1] [/propertyStyle 0|1] /nooverride <name>
```

### Parameters

|  |  |
| --- | --- |
| /bold | Bold font. |
| /fontColour | As a hex value in BGR format. E.g. Blue is FF0000, Red is 0000FF, or HTML format e.g. #0000FF is Blue |
| /fontName | Font family name. |
| /fontSize | A number. |
| /italics | Italic font. |
| /lineColour | As a hex value in BGR format. E.g. Blue is FF0000, Red is 0000FF, or HTML format e.g. #0000FF is Blue |
| /lineFixedThickness | Set to 1 to fix line thickness - i.e. does not scale with zoom |
| /lineThickness | A number. |
| /lineType | Options are Solid, Dash, Dot, DashDot, DashDotDot. |
| /nooverride | Use this to ensure that the style is only added if it does not already exist as a global style. |
| /overline | Overline the text. |
| /propertyStyle | Font should appear in the Property style options drop down box. |
| /underline | Underline the text. |
| name | Name of the style to use. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_addglobalstyle) | | |
| [◄ AddFreeText](com_addfreetext.htm) |  | [AddImage ▶](com_addimage.htm) |
