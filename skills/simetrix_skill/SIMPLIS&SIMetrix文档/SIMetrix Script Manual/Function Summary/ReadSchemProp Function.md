# ReadSchemProp Function

Returns value of schematic window property value.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | No | Currently displayed | Schematic path |
| 3 | number | No |  | Schematic handle |

#### Argument 1

Property name. There are a number of built-in properties that are always available. Others can be created with the function  [WriteSchemProp](func_writeschemprop.htm) . The built-in properties are:

|  |  |
| --- | --- |
| 'Path' | Read-only. File system path name of schematic |
| 'RootPath' | Read/Write. Path of root in hierarchy. Value displayed in status bar of schematic |
| 'Reference' | Read/Write. Full component reference of block representing schematic. |
| 'Readonly' | Read-only. Readonly status of schematic. Return value may be 'TRUE' or 'FALSE' |
| 'UserStatus' | Read/Write. Contents of user status box at the bottom of the schematic. This is currently the 6th box from the left. |
| 'UserVersion' | Read-only. Current version number of schematic. This is updated each time the schematic is saved |
| 'ID' | Read-only. Returns ID of schematic (same value returned by  [OpenSchematic](func_openschematic.htm)  ) |
| 'Magnification' | Read-only. Current view magnification |
| 'Modified' | Modified status 'TRUE' or 'FALSE' |

#### Argument 2

Path of schematic to process. This must be a schematic that is currently displayed; the function can not operate on a closed schematic.If not specified, the currently selected schematic will be processed.

#### Argument 3

Schematic handle.

### Returns

Return type: string

Returns the value of the property

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readschemprop) | | |
| [◄ ReadRegSetting](func_readregsetting.htm) |  | [ReadSIMPLISF11Data ▶](func_readsimplisf11data.htm) |
