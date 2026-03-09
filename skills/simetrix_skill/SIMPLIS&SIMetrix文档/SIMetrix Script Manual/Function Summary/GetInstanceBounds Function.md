# GetInstanceBounds Function

Returns the bounds occupied by a schematic instance identified by a property name and value.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | Yes |  | Property value |
| 3 | string | No | none | Options |

#### Argument 1

Property name to identify instance used in conjunction with parameter 2. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 2

Property value to identify instance, along with parameter 1. If the arguments identify more than one instance, the function will return information for one of them but there are no rules to define which one.

#### Argument 3

If set to 'body', the function will return the bounds of the grpahics of the symbol only. This excludes the area occupied by any displayed properties. If this is omitted, the bounding area returned will include all visible property text.

### Returns

Return type: real array

The function returns a four element real array which defines the area occupied by the instance. The values are in "sheet units". There are 120 sheet units per visible grid square at X 1 magnification. The four elements of the array are in the order top, left, right, bottom. Values increase left to right and top to bottom.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_getinstancebounds) | | |
| [◄ GetHttpContentSize](func_gethttpcontentsize.htm) |  | [GetInstanceConvergenceInfo ▶](func_getinstanceconvergenceinfo.htm) |
