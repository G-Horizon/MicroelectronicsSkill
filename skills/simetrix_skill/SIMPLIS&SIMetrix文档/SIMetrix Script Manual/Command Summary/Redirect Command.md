# Redirect Command

Redirects messages (i.e. text which is normally displayed in the message window) to a file. One or both of `/err` or `/out` must be specified.

```
Redirect /err|/out [<filename>]
```

### Parameters

|  |  |
| --- | --- |
| /err | Specifies that error and warning messages are to be redirected. |
| /out | Specifies that messages other than errors and warnings are to be redirected. |
| filename | Name of file to which messages are sent. If not specified messages are sent to the message window the specified redirect mode is cancelled and messages of that type will be sent to the command shell. |

### See Also

* [RedirectMessages](com_redirectmessages.htm)  redirects everything to a file.

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_redirect) | | |
| [◄ RebuildSymbols](com_rebuildsymbols.htm) |  | [RedirectMessages ▶](com_redirectmessages.htm) |
