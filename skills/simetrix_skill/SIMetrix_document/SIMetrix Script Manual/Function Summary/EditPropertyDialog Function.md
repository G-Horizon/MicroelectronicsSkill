# EditPropertyDialog Function

Opens a dialog box intended to edit a property in both the symbol and schematic editors. Select the symbol editor's **Property/Pin** > **Edit Property...** menu then double click on one of the items. This will open this dialog box.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes | <<empty>> | property name |
| 2 | string | No | 0 | initial property flags |
| 3 | string | No | <<empty>> | initial property value |
| 4 | string | No |  | option |
| 5 | string | No | <<empty>> | font override style |
| 6 | string | No | <<empty>> | available font override styles |

#### Argument 1

Specifies the property name and this is displayed at the top left of the box. This cannot be edited by the user.

#### Argument 2

Initialises the text location and property attributes using the property flag value. For details on the meaning of flags values see  [Attribute Flags in the Prop command](com_prop.htm) .

#### Argument 3

Argument initialises the Value box

### Returns

Return type: string array

String array of length 2 providing the users settings, or empty vector if Cancel is pressed.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Flags value |
| 1 | Property value |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editpropertydialog) | | |
| [◄ EditProbeDialog](func_editprobedialog.htm) |  | [EditReactiveDialog ▶](func_editreactivedialog.htm) |
