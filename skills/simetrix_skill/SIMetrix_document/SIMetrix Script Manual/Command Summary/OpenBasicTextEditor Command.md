# OpenBasicTextEditor Command

Open a plain text file for manual text editing. This command opens the text file with no syntax highlighting. Use one of the following commands to open files with specific formats:

* [OpenNetlist](com_opennetlist.htm)  to open a model file or netlist file
* [OpenLogicDefinitionEditor](com_openlogicdefinitioneditor.htm)  to open a logic definition file for the abritrary logic block
* [OpenScript](com_openscript.htm)  to open a script
* [OpenVerilogA](com_openveriloga.htm)  to open a Verilog-A source file
* [OpenVerilogHDL](com_openveriloghdl.htm)  to open a Verilog-HDL source file
* [OpenAsciiFile](com_openasciifile.htm)  to open a schematic file in the text editor

```
OpenBasicTextEditor <filename>
```

### Parameters

|  |  |
| --- | --- |
| /encoding | encoding. For details see documentation of second argument to  [LoadFile](func_loadfile.htm) |
| /fws | File watcher status, enable|disable|auto |
| filename | Path of text file to open |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_openbasictexteditor) | | |
| [◄ OpenAsciiFile](com_openasciifile.htm) |  | [OpenDirectory ▶](com_opendirectory.htm) |
