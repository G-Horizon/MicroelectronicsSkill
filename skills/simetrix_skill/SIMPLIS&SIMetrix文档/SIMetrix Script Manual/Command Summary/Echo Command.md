# Echo Command

Echoes text to the message window or to a file

```
Echo <text>
```

### Parameters

|  |  |
| --- | --- |
| /append | If present  *text*  is appended to  *filename* . If  *filename*  does not exist, it is created. If the file points to a file that has already been opened for write using  [OpenFile](func_openfile.htm)  , the handle already opened will be used |
| /box | Text is output inside a box composed of asterix characters. This is useful for titles and headings. Currently only works correctly when used with `/file` or `/append`. |
| /debug |  |
| /file | If present  *text*  is output to  *filename* . If  *filename*  exists, it is overwritten. |
| /handle | File handle as returned by the function  [OpenFile](func_openfile.htm) . Text will output the file referenced by this handle. |
| /html | If present  *text*  is assumed to be html formatted. |
| /list |  |
| /page | Prefixes output with a ASCII form feed character. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_echo) | | |
| [◄ DrawPin](com_drawpin.htm) |  | [EditColour ▶](com_editcolour.htm) |
