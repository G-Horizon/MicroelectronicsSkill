# NetWires Function

Returns wire handles of names net.

Note that this function requires that the schematic has been netlisted. This can be forced using the function  [Netlist](com_netlist.htm)  in the form:

```
Netlist /nooutput /nodescend
```

if required. Note also that, for a child schematic in a hierarchy, a local netname is expected, that is without the path prefix (e.g. 'voutn' not 'u1.voutn')

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Net name |
| 2 | real | No | -1 | Schematic ID |

#### Argument 1

Name of net whose wire handles are required.

#### Argument 2

Schematic ID as returned by the function  [OpenSchematic](func_openschematic.htm) . This allows this function to be used with a schematic that is not open or not currently selected. If omitted or -1, the currently selected schematic will be used.

### Returns

Return type: string array

Returns an array of strings holding the handles for all wires on the specified net. Returns an empty string if there are no wires on the net or if the net does not exist.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_netwires) | | |
| [◄ NetToCirc](func_nettocirc.htm) |  | [NewPassiveDialog ▶](func_newpassivedialog.htm) |
