# OpenScript Command

Opens a script source file in the text editor. This will apply syntax highlighting for the script language along with prompts for function names and commands.

If the option setting `ScriptEditor` is set and points to a valid executable file, this command will instead call the specified application to open the file.

```
OpenScript <filename>
```

### Parameters

|  |  |
| --- | --- |
| /encoding | encoding. For details see documentation of second argument to  [LoadFile](func_loadfile.htm) |
| /fws | File watcher status, enable|disable|auto |
| filename | Path of script source file to open |

### See Also

* [OpenNetlist](com_opennetlist.htm)  to open a model file or netlist file
* [OpenBasicTextEditor](com_openbasictexteditor.htm)  to open a plain text file
* [OpenLogicDefinitionEditor](com_openlogicdefinitioneditor.htm)  to open a logic definition file for the abritrary logic block
* [OpenVerilogA](com_openveriloga.htm)  to open a Verilog-A source file
* [OpenVerilogHDL](com_openveriloghdl.htm)  to open a Verilog-HDL source file
* [OpenAsciiFile](com_openasciifile.htm)  to open a schematic file in the text editor

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_openscript) | | |
| [◄ OpenSchem](com_openschem.htm) |  | [OpenSimplisStatusBox ▶](com_opensimplisstatusbox.htm) |
