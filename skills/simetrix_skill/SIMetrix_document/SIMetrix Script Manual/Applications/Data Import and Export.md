# Data Import and Export

This section is also in the User's manual. It is reproduced here for convenience.

SIMetrix provides the capability to export simulation data to a file in text form and also to import data from a file in text form. This makes it possible to process simulation data using another application such as a spreadsheet or custom program.

In this topic:

## Importing Data

To import data use the [OpenGroup](com_opengroup.htm) command with the `/text` switch. E.g. at the command line type:

```
OpenGroup /text data.txt
```

This will read in the file data.txt and create a new group called text???MATH???n???MATH???, where ???MATH???n???MATH??? is an index as described in  [Data Files Text Format](applications_dataimportexport.htm#applications_dataimportexport__datafilestextformat)  below for details of format.

Note that if you create the file using another program such as a spreadsheet, the above command may fail if the file is still open in the other application. Closing the file in the other application will resolve this.

## Exporting Data

To export data, use the [Show](com_show.htm) command with the `/file` switch. E.g:

```
Show /file data.txt vout r1_p q1#c
```

will output to data.txt the vectors `vout`, `r1_p`, and `q1#c`. The values will be output in a form compatible with `OpenGroup /text`.

### Vector Names

In the above example the vector names are `vout`, `r1_p` and `q1#c`. If you simulate a schematic, the names used for voltage signals are the same as the node names in the netlist which in turn are assigned by the schematic's netlist generator. To find out what these names are, place the mouse cursor on the node of interest on the schematic then press ctrl-S. The node name - and therefore the vector name - will be displayed in the command shell. A similar procedure can be used for currents. Place the mouse cursor on the device pin of interest and press ctrl-P.

## Launching Other Applications

Data import and export makes it possible to process simulation data using other applications. SIMetrix has a facility to launch other programs using the Shell command. You could therefore write a script to export data, process it with your own program then read the processed data back in for plotting. To do this you must specify the `/wait` switch for the Shell command to force SIMetrix to wait until the external application has finished. E.g.

```
Shell /wait procdata.exe
```

will launch the program procdata.exe and will not return until procdata.exe has closed.

## Data Files Text Format

There are two alternative formats.

The first is simply a series of values separated by whitespace. This will be read in as a single vector with a reference equal to its index.

The second format is as follows:

A text data file may contain any number of *blocks*. Each block has a *header* followed by a list of *datapoints*. The header and each *datapoint* must be on one line. The *header* is of the form:

```
reference_name ydata1_name[ ydata2_name ... ]
```

Each *datapoint* must be of the form:

```
reference_value ydata1_value[ ydata2_value ... ]
```

The number of entries in each *datapoint* must correspond to the number of entries in the *header*.

The *reference* is the x data (e.g. time or frequency).

### Example

```
Time       Voltage1 	Voltage2

0          14.5396      14.6916
1e-09      14.5397      14.6917
2e-09      14.5398      14.6917
4e-09      14.54        14.6917
8e-09      14.5408      14.6911
1.6e-08    14.5439      14.688
3.2e-08    14.5555      14.6766
6.4e-08    14.5909      14.641
1e-07      14.6404      14.5905
1.064e-07  14.6483      14.5821
```

If the above was read in as a text file (using `OpenGroup /text`), a new group called textn where n is a number would be generated. The group would contain three vectors called: "Time", "Voltage1" and "Voltage2". The vectors "Voltage1" and "Voltage2" would have a reference of "Time". "Time" itself would not have a reference.

To read in complex values, enclose the real and imaginary parts in parentheses and separate with a comma. E.g:

```
Frequency : VOUT
1000        (-5.94260997 ,0.002837811 )
1004.61579  (-5.94260997 ,0.00285091 )
1009.252886 (-5.94260996 ,0.002864069 )
1013.911386 (-5.94260995 ,0.002877289 )
1018.591388 (-5.94260994 ,0.00289057 )
1023.292992 (-5.94260993 ,0.002903912 )
1028.016298 (-5.94260992 ,0.002917316 )
1032.761406 (-5.94260991 ,0.002930782 )
1037.528416 (-5.9426099  ,0.00294431 )
1042.317429 (-5.94260989 ,0.0029579 )
1047.128548 (-5.94260988 ,0.002971553 )
1051.961874 (-5.94260987 ,0.002985269 )
```

|  |  |  |
| --- | --- | --- |
| [◄ Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm) |  | [Graph Objects ▶](applications_graphobjects.htm) |
