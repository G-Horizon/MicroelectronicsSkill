# OpenPrinter Command

Starts a print session. This may be used for customised or non-interactive printing. See  [Non-interactive and Customised Printing](applications_noninteractivecustomisedprinting.htm)

```
OpenPrinter [/portrait ] [/numCopies <num-copies>] [/index <index>] [/title <title>] [/printer <printer>] [/greyscale on|off]
```

### Parameters

|  |  |
| --- | --- |
| /greyscale | Set to 'on' to enable grey-scale printing |
| /index | Printer to use. This can be found from the function  [GetPrinterInfo](func_getprinterinfo.htm) . If omitted, the application default printer will be used. |
| /numCopies | Number of copies to print. |
| /portrait | If specified, print will be in portrait orientation, otherwise it will be landscape |
| /printer | Specify printer by name. If omitted, printer will be defined by its index (see below) or the application default printer will be used. |
| /title | Title of  *print job* . This is used to identify a print job and will be displayed in the list of current print jobs that can be viewed for each installed printer from control panel. title is not printed on the final document. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_openprinter) | | |
| [◄ OpenNetlist](com_opennetlist.htm) |  | [OpenRawFile ▶](com_openrawfile.htm) |
