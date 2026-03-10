# OpenSchematic Function

Opens a schematic given its file system path. The return value may be used with a number of other functions and commands. This function does not display the schematic.

The function  [GetSchematicTabs](func_getschematictabs.htm)  returns the IDs for all currently displayed schematics.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | File path |

#### Argument 1

File system path to schematic file. The schematic does not need to be currently displayed

### Returns

Return type: real

Returns an integer ID that can be used for a wide range of functions that return information about a schematic. It may also be used by some commands. If the schematic cannot be opened for any reason, the function returns -1.

### Notes

The OpenSchematic function along with the functions listed below that support schematic IDs, allow information to be retrieved from schematics that are not currently on display. If the specified schematic is displayed then the values returned by the supported functions will reflect the state of the displayed schematic and not the saved schematic. The return value from OpenSchematic can be used with the following functions:

* [CloseSchematicTab](func_closeschematictab.htm)
* [DescendHierarchy](func_descendhierarchy.htm)
* [ElementProps](func_elementprops.htm)
* [GetChildModulePorts](func_getchildmoduleports.htm)
* [GetComponentValue](func_getcomponentvalue.htm)
* [GetF11Lines](func_getf11lines.htm)
* [GetInstancePinLocs](func_getinstancepinlocs.htm)
* [GetModifiedStatus](func_getmodifiedstatus.htm)
* [GetReadOnlyStatus](func_getreadonlystatus.htm)
* [GetSchematicTabs](func_getschematictabs.htm)
* [GetSchematicVersion](func_getschematicversion.htm)
* [GetSimulatorMode](func_getsimulatormode.htm)
* [HasProperty](func_hasproperty.htm)
* [HighlightedNets](func_highlightednets.htm)
* [Instances](func_instances.htm)
* [InstNets2](func_instnets2.htm)
* [InstPins](func_instpins.htm)
* [InstPoints](func_instpoints.htm)
* [InstProps](func_instprops.htm)
* [NetNames](func_netnames.htm)
* [NetWires](func_netwires.htm)
* [PropFlags](func_propflags.htm)
* [PropFlags2](func_propflags2.htm)
* [PropFlagsAll](func_propflagsall.htm)
* [PropFlagsAnnotations](func_propflagsannotations.htm)
* [PropFlagsWires](func_propflagswires.htm)
* [PropValues](func_propvalues.htm)
* [PropValues2](func_propvalues2.htm)
* [SetComponentValue](func_setcomponentvalue.htm)
* [SetReadOnlyStatus](func_setreadonlystatus.htm)
* [SymbolName](func_symbolname.htm)
* [SymbolNames](func_symbolnames.htm)
* [WirePoints](func_wirepoints.htm)
* [Wires](func_wires.htm)

The schematic ID may also be used by these commands:

* [SaveAs](com_saveas.htm)
* [SelectSchematic](com_selectschematic.htm)

The handle returned by OpenSchematic may be closed using the function  [CloseSchematic](func_closeschematic.htm) . After a call to CloseSchematic, the handle will no longer be valid and any function it is supplied to will fail. However, it is not usually necessary to call CloseSchematic as handles are automatically closed when control returns to the command line.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_openschematic) | | |
| [◄ OpenSchem](func_openschem.htm) |  | [OptimiserAnalysisLine ▶](func_optimiseranalysisline.htm) |
