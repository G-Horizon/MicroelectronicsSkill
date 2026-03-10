# UpdateGlobalStyle Command

Updates an existing global style. Will only update the options used.

```
UpdateGlobalStyle <name> /lineType [type] /lineColour [colour] /lineThickness [thickness] /fontName [name] /fontSize [size] /fontColour [colour] /italics /bold /overline /underline /propertyStyle
```

### Parameters

|  |  |
| --- | --- |
| /bold | 1|0 Bold font. |
| /fontColour | As an AABBGGRR value. |
| /fontName | Font family name. |
| /fontSize | Font size in points (integer). |
| /italics | 1|0 Italic font. |
| /lineColour | As an AABBGGRR value, 0x00ff00ff for blue=255, green=0, red=255. |
| /lineFixedThickness | Set to 1 to fix line thickness - i.e. does not scale with zoom |
| /lineThickness | Line thickness. Units 1/96 logical inches (real) |
| /lineType | Options are Solid, Dash, Dot, DashDot, DashDotDot. |
| /overline | 1|0 Overline the text. |
| /propertyStyle | 1|0 Font should appear in the Property style options drop down box. |
| /underline | 1|0 Underline the text. |
| /updateall | Optional flag that will notify and update all Editors and update the configuration file. Use once after a batch change of style settings. |
| name | Name of the style to use. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_updateglobalstyle) | | |
| [◄ UpdateDefaultStyle](com_updatedefaultstyle.htm) |  | [UpdateGraphColours ▶](com_updategraphcolours.htm) |
