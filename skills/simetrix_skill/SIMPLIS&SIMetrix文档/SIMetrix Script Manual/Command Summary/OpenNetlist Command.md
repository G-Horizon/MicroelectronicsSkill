# OpenNetlist Command

Opens a SPICE netlist or model file in the text editor. This will apply syntax highlighting for the simulator command language.

If the option setting `NetlistEditor` is set and points to a valid executable file, this command will instead call the specified application to open the file.

```
OpenNetlist <filename>
```

### Parameters

|  |  |
| --- | --- |
| /encoding | encoding. For details see documentation of second argument to  [LoadFile](func_loadfile.htm) |
| /fws | File watcher status, enable|disable|auto |
| filename | Path of netlist or model file to open |

### See Also

* [OpenLogicDefinitionEditor](com_openlogicdefinitioneditor.htm)  to open a logic definition file for the abritrary logic block
* [OpenBasicTextEditor](com_openbasictexteditor.htm)  to open a plain text file
* [OpenScript](com_openscript.htm)  to open a script
* [OpenVerilogA](com_openveriloga.htm)  to open a Verilog-A source file
* [OpenVerilogHDL](com_openveriloghdl.htm)  to open a Verilog-HDL source file
* [OpenAsciiFile](com_openasciifile.htm)  to open a schematic file in the text editor

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_opennetlist) | | |
| [◄ OpenLogicDefinitionEditor](com_openlogicdefinitioneditor.htm) |  | [OpenPrinter ▶](com_openprinter.htm) |
