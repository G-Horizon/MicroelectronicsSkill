# GetPrinterInfo Function

Returns information on installed printers.

### Arguments

No arguments

### Returns

Return type: string array

Returns array of strings providing system printer names and current application default printer. Format is as follows:

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Number of printers available in system |
| 1 | Index of printer that is currently set as default. (This is the default for the application  *not*  the system default printer - see below) |
| 2 | List of printer names (and subsequent indexes) |

### Example

The following is an example of executing the command `Show GetPrinterInfo`

```
Index    GetPrinterInfo()
0	'5'
1	'2'
2	'Dell Laser Printer 1100'
3	'Fax'
4	'HP Color LaserJet CP4020 Series PCL6'
5	'Microsoft XPS Document Writer'
6	'Send To OneNote 2010'
```

The default index is 2 so this means that 'HP Color LaserJet CP4020 Series PCL6' is currently set as the default printer. This is the current default for the  *application*  and is what will be set when you open a Print dialog box. When SIMetrix starts, it will be initialised to the  *system*  default printer but changes whenever you select a different printer in any of the printer dialogs.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getprinterinfo) | | |
| [◄ GetPlatformFeatures](func_getplatformfeatures.htm) |  | [GetPrintValues ▶](func_getprintvalues.htm) |
