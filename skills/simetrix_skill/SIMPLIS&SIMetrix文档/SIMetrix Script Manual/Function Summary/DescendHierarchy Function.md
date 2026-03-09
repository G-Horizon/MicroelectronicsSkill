# DescendHierarchy Function

Descends through the hierarchy from the current schematic and collects each distinct schematic in use. The result is a list of schematic path names. Each path name is accompanied by a list of hierarchy references where that schematic is used.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | 'Ref' | Property used to report 'where used' references |
| 2 | real | No | -1 | Schematic ID |
| 3 | string | Yes |  | options |

#### Argument 1

Name of property to be used to report 'where used' references. Each entry in the return value contains a list of schematic instance references that identify where the schematic component is used. The references are in the form of a series of property values separated by a period ('.'). The property used defaults to 'Ref' but this argument may be used to identify another property - e.g. 'Handle'.

#### Argument 2

Schematic ID as returned by the  [OpenSchematic](func_openschematic.htm)  function. This allows this function to be used with a schematic that is not open or not currently selected. If equal to -1, the currently selected schematic will be used.

#### Argument 3

If set to 'pathtypes' will return information on the type of path. Possible values are 'absolute', 'relative' and 'symbolic'

### Returns

Return type: string array

Returns a string array with one element for each schematic file used in the hierarchy. Each element is a semi-colon delimited list of values. The first value is the full path to the schematic in UNC form if applicable. UNC paths begin with '\ \' followed by a server name and path. Paths referenced by a local drive letter are not returned in UNC form even if sharing is enabled for that drive.

The remaining values are a list of hierarchical references identifying where that schematic is used within the hierarchy. The references use the value of the property defined in argument 1.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_descendhierarchy) | | |
| [◄ DescendDirectories](func_descenddirectories.htm) |  | [DestroyMutex ▶](func_destroymutex.htm) |
