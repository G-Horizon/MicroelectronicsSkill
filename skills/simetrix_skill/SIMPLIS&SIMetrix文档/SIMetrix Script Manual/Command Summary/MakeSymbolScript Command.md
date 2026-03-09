# MakeSymbolScript Command

Creates a script definition of a symbol or group of symbols. For details of script definitions see  [Schematic Symbol Script Definition](applications_schematicsymbolscriptdefinition.htm) .

```
MakeSymbolScript [/all] [/append] [/sortprops] [/catalog <catalog-name>] <filename> [<symbol-name> ...]
```

### Parameters

|  |  |
| --- | --- |
| /all | If specified, scripts for all symbols in the global library will be created. |
| /append | Result will be appended to specified file. |
| /catalog | If specified, scripts for all symbols in the specified catalog of the global library will be created. This overrides `/all`. |
| /sortProps | If specified, all visible properties are ordered alphabetically in the output script. Properties are defined with the command  [AddProp](com_addprop.htm) . |
| filename | Path of file to be written. |
| symbol-name | Name of symbol to be scripted. Any number may be specified. If `/all` or `/catalog` are specified, this argument will be ignored. If they are not this argument becomes compulsory. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_makesymbolscript) | | |
| [◄ MakeCatalog](com_makecatalog.htm) |  | [MakeTree ▶](com_maketree.htm) |
