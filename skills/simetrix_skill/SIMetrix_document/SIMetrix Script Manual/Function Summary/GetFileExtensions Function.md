# GetFileExtensions Function

Returns a string array containing all valid extensions (without prefixed '.') for the given file type.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File type |

### Returns

Return type: string array

Returns a string array containing all valid extensions (without prefixed '.') for the given file type. The extension returned in the first element is the default. File extensions can be changed in the general options dialog box ( **File** > **Options** > **General...** ) and are stored in a number of option variables. These are listed in the following table.

|  |  |  |  |
| --- | --- | --- | --- |
| **Argument** | **Used for** | **Option name** | **Default** |
| 'Schematic' | Schematic files | SchematicExtension | sxsch |
| 'Data' | Data files | DataExtension | sxdat, dat |
| 'Text' | Text files | TextExtension | txt, log |
| 'Symbol' | Binary symbol files | SymbolExtension | sxslb, slb |
| 'LogicDef' | Logic definition files used with arbitrary logic block | LogicDefExtension | ldf |
| 'Script' | Script files | ScriptExtension | sxscr |
| 'Model' | Model files | ModelExtension | lb, lib, mod, cir, spi, fam, mdl, sp, sp2, model, pkg, prm, sub, sio, ckt |
| 'Catalog' | Catalog files | CatalogExtension | cat |
| 'Graph' | Graph binary files | GraphExtension | sxgph |
| 'Component' | Schematic hierarchical component | ComponentExtension | sxcmp |
| 'Snapshot' | Snapshot files | SnapshotExtension | sxsnp |
| 'Netlist' | Netlist files | NetlistExtension | net, cir, deck |
| 'Verilog-A' | Verilog-A files | VerilogAExtension | va, vams |
| 'Verilog-HDL' | Verilog-HDL files | VerilogHDLExtension | v |
| 'ASCIIFileEditor' | Schematic ASCII files | AsciiFileEditorExtension | sxsch, sxslb, sxcmp |

You can combine multiple file types delimited by '&'. For example "Netlist & Model" will return the extensions for both netlist and model file types.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getfileextensions) | | |
| [◄ GetFileDir](func_getfiledir.htm) |  | [GetFileInfo ▶](func_getfileinfo.htm) |
