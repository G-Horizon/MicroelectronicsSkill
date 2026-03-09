# ClosePrinter Command

ClosePrinter is one of a number of commands and functions used for non-interactive printing. This is explained in  [Non-interactive and Customised Printing](applications_noninteractivecustomisedprinting.htm) . Printing sessions are started with  [OpenPrinter](com_openprinter.htm)  after which print output commands such as  [PrintGraph](com_printgraph.htm)  and  [PrintSchematic](com_printschematic.htm)  may be called. The session is terminated with ClosePrinter which actually initiates the printing activity. If the `/abort` switch is specified, the print job is terminated and no print output will be produced.

### Parameters

|  |  |
| --- | --- |
| /abort | Any print job will be aborted and no print output will be produced. |

### See Also

* [NewPrinterPage](com_newprinterpage.htm)
* [OpenPrinter](com_openprinter.htm)
* [PrintGraph](com_printgraph.htm)
* [PrintSchematic](com_printschematic.htm)
* [GenPrintDialog](func_genprintdialog.htm)
* [GetPrinterInfo](func_getprinterinfo.htm)

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_closeprinter) | | |
| [◄ CloseLinkedRun](com_closelinkedrun.htm) |  | [CloseSchem ▶](com_closeschem.htm) |
