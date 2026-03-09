# Navigate Function

Returns path name of hierarchical block given root path and full component reference.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Full component reference |
| 2 | string | Yes |  | Path of hierarchical root |

#### Argument 1

Component reference of block. This must be the full reference specifying the full path to the root. For example the reference U3.U4 refers to a block of reference U4 found in the underlying schematic of a block of reference U3 in the root schematic.

#### Argument 2

File system pathname of root schematic.

### Returns

Return type: string

Returns path name of schematic hierarchical block.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_navigate) | | |
| [◄ MSWReadHeader](func_mswreadheader.htm) |  | [NearestInst ▶](func_nearestinst.htm) |
