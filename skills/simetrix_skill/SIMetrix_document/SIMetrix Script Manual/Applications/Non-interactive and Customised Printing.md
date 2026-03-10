# Non-interactive and Customised Printing

In this topic:

## Overview

The SIMetrix script language provides a number of functions and commands that allow *non-interactive printing*. That is printing without user intervention. This is useful for - say - running multiple simulations in the background and automatically printing the results when the simulation is complete. The same printing facilities may also be used to customise the layout of printed schematics and graphs. The user interface provides a method of printing a single graph and schematic on the same sheet, but other arrangements are possible using the underlying printing commands.

The available printing commands are:

* [ClosePrinter](com_closeprinter.htm)
* [NewPrinterPage](com_newprinterpage.htm)
* [OpenPrinter](com_openprinter.htm)
* [PrintGraph](com_printgraph.htm)
* [PrintSchematic](com_printschematic.htm)

The functions are:

* [GenPrintDialog](func_genprintdialog.htm) (for interactive printing)
* [GetPrinterInfo](func_getprinterinfo.htm)

Each of these commands and functions is described in detail in its relevant section. Here we give a general overview for the printing procedure.

## Procedure

The sequence for a print job is:

1. Open printer. At this stage the printer to be used, page orientation, title and number of copies may be selected.
2. Print pages. The actual graphs/schematics to be printed along with scaling and margins are specified here. Any number of pages can be printed.
3. Close printer. This actually starts the physical printing. It is also possible to abort the print job.

## Example

Suppose we wish to create a PDF file using 'Acrobat Distiller' for the current graph. Of course you can readily do this by selecting File|Print... and making the appropriate selections using the dialog box. This is no good, however, if you want to create a PDF file for a graph created using an automated simulation, perhaps run overnight. The following script will do this without user intervention.

```
** Get info on system printers
Let printInfo = GetPrinterInfo()

** Search for acrobat distiller. The printer list from GetPrinterInfo
** starts at index 2 so we subtract 2 to get the index
** needed by OpenPrinter
Let distillerIndex = Search(printInfo, 'Acrobat Distiller')-2

** If Acrobat distiller is not on the system
** Search will return -1
if distillerIndex<0 then
Echo "Acrobat Distiller is not installed"
exit script
endif

** Open Printer using distiller.
** Orientation will be landscape which is the default
** Number of copies = 1.
** The title will be used by distiller to compose the file name
** for the PDF file i.e. Graph1.PDF
OpenPrinter /title Graph1 /index {distillerIndex}

** Now print the graph
** Major axis on minor axis off. All margins 20mm.
PrintGraph /major on /minor off /margin 20 20 20 20 /caption
"Test Print"

** Close Printer. This will actually start the print
ClosePrinter
```

You can of course replace 'Acrobat Distiller' with any printer that is on your system. You must use the printer's name as listed in the Printers section of the system control panel. You can also find a list of system printers from within SIMetrix by typing at the command line:

```
Show GetPrinterInfo()
```

The first two values are numbers but the remaining are the currently installed printers on your system.

If you omit /index switch for the [OpenPrinter](com_openprinter.htm) command, the application default printer (not the *system* default printer) will be used. The application default printer is the same as the system default printer when SIMetrix starts but will change whenever the user selects a different printer using the SIMetrix File|Print... dialog box.

|  |  |  |
| --- | --- | --- |
| [◄ User Defined Binary Functions](applications_userdefinedbinaryfunctions.htm) |  | [Schematic Template Scripts ▶](applications_schematictemplatescripts.htm) |
