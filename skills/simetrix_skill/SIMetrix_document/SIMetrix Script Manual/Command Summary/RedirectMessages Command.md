# RedirectMessages Command

Redirects all command shell messages to a file. Everything that would normally be displayed in the command shell such as error messages will be sent to the specified file. An option is available to copy command shell output to a file, that is the command shell messages continue to be displayed but are also written to a file.

Note that some messages are sent in HTML format to show bold text and other formatting. These will be shown in the file in their native form including the HTML tags.

```
RedirectMessages on <filename>|dup <filename>|off|flush
```

### Parameters

|  |  |
| --- | --- |
| on | Switch on redirect. All messages will go to  *filename*  and no output will appear in the message window |
| append | As  **on**  but appends text to file if it already exists |
| dup | Switch on redirect. All messages will go to  *filename*  and to the message window |
| off | Switch off redirect. Restore message output to command shell and close redirect file |
| flush | Flush file. When redirect is switched on, messages are buffered before being written to the target file. This will flush the buffer so that the file contents will be up to date |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_redirectmessages) | | |
| [◄ Redirect](com_redirect.htm) |  | [Redo ▶](com_redo.htm) |
