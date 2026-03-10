# MakeCatalog Command

This command builds a catalog file for use by the parts browser. This is normally called OUT.CAT and resides in the SCRIPT directory.

The MakeCatalog command is one of the components of the Parts Browser system. The parts browser requires a catalog file which lists all the models available to the simulator and for each provides the name of a suitable schematic symbol, a category, pin mapping if relevant, a symbol model property (e.g. X for subcircuits, Q for BJTs) and a preferred pathname if there is more than one model of that name. The MakeCatalog command builds this catalog using the data files  *all-catalog*  and  *user-catalog*  to obtain information about known parts.

```
MakeCatalog <out-catalog> <all-catalog> [<user-catalog>]
```

### Parameters

|  |  |
| --- | --- |
| /force |  |
| /listDups |  |
| out-catalog | File name for catalog. This must be OUT.CAT for use with browser. |
| all-catalog | Main database of parts. This would usually be ALL.CAT which resides in the SIMetrix root directory. |
| user-catalog | User database of parts. This would usually be called USER.CAT which resides in the script directory. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_makecatalog) | | |
| [◄ MakeAlias](com_makealias.htm) |  | [MakeSymbolScript ▶](com_makesymbolscript.htm) |
