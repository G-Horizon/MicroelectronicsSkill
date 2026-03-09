# AppendTextWindow Command

Inserts text into the schematic editor's simulator command window also known as the  *F11 window* .

```
AppendTextWindow [/file <filename>] [/text]
```

### Parameters

|  |  |
| --- | --- |
| /copy | If specified the text is copied to the F11 window replacing the existing text. Otherwise text is appended. |
| /file |  |
| filename | If specified, the contents of the specified file is placed in the F11 window |
| text | If '/file  *filename*  ' is absent, text is inserted in the F11 window |

### Notes

Text is always is always appended to the end of the window's existing contents.

### See Also

* [ReadF11Options](func_readf11options.htm)
* [WriteF11Options](func_writef11options.htm)
* [WriteF11Lines](func_writef11lines.htm)
* [GetF11Lines](func_getf11lines.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_appendtextwindow) | | |
| [◄ AppendGroup](com_appendgroup.htm) |  | [Arguments ▶](com_arguments.htm) |
