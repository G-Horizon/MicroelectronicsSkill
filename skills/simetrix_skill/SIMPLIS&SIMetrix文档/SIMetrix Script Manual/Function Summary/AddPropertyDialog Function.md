# AddPropertyDialog Function

Opens the dialog box used to create a new property in the symbol editor. (E.g as opened by **Property/Pin** > **Add Property...** ) The first and third arguments initialise the Name and Value boxes respectively. Argument 2 initialises the text location and property attributes. For details on the meaning of attribute flags see  [Attribute Flags in the Prop command](com_prop.htm) .

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty>> | initial property name |
| 2 | string | No | 0 | initial property attribute flags |
| 3 | string | No | <<empty>> | initial property value |
| 4 | string | No | <<empty>> | options |
| 5 | string | No | <<empty>> | font override style |
| 6 | string | No | <<empty>> | available font override styles |

### Returns

Return type: string array length 3

String array of length 4 providing the users settings. The function returns an empty vector if Cancel is selected.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Property name |
| 1 | Flags value |
| 2 | Property value |
| 3 | Font override style |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addpropertydialog) | | |
| [◄ AddModelFiles](func_addmodelfiles.htm) |  | [AddRemoveDialog ▶](func_addremovedialog.htm) |
