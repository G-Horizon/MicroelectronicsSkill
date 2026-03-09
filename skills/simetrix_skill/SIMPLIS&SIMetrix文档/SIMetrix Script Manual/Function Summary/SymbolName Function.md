# SymbolName Function

Returns symbol name of specified instance.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | Yes |  | Property value |
| 3 | real | No | -1 | Schematic ID |

#### Argument 1

Along with argument 2, property name and value to identify instance. If these arguments are not supplied, the selected instance, if any, will be used instead. If there are no selected instances or no instances that match the arguments, the function will return an empty vector. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 2

See argument 1.

#### Argument 3

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string

Returns the symbol name used by the instance defined by property name and value supplied in arguments 1 and 2.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_symbolname) | | |
| [◄ SymbolLibraryManagerDialog](func_symbollibrarymanagerdialog.htm) |  | [SymbolNames ▶](func_symbolnames.htm) |
