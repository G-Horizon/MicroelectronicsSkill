# OpenPrinter Function

Starts a print session. This may be used for customised or non-interactive printing. See  [Non-interactive and Customised Printing](applications_noninteractivecustomisedprinting.htm)

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | No |  | Configuration |

#### Argument 1

String array with up to 6 elements as described in the following table

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Print orientation: 'landscape' or 'portrait' |
| 1 | Number of copies |
| 2 | Printer id. This is an index and can be found from the function  [GetPrinterInfo](func_getprinterinfo.htm) . If omitted, the application default printer will be used. |
| 3 | Title of print job. This is used to identify a print job and will be displayed in the list of current print jobs that can be viewed for each installed printer from control panel. title is not printed on the final document. |
| 4 | Specify printer by name. If omitted, printer will be defined by its index (see above) or the application default printer will be used |

### Returns

Return type: string

Status of operation: either 'Success' or 'Failed'

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_openprinter) | | |
| [◄ OpenPDFPrinter](func_openpdfprinter.htm) |  | [OpenSchem ▶](func_openschem.htm) |
