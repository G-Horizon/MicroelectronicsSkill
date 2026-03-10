# EditPinDialog Function

Opens a dialog box used to edit a pin in the symbol editor.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | initial pin name |
| 2 | string | No | '256' | initial flags value |
| 3 | string | No |  | not used |
| 4 | string | No |  | not used |
| 5 | string | No | <<empty>> | font override style |
| 6 | string | No | <<empty>> | available font override styles |

#### Argument 1

Specifies the initial value for the Pin name entry

#### Argument 2

Specifies the initial value for the remaining controls using the property attributes flag. See  [Attribute Flags in the Prop command](com_prop.htm)  for details.

### Returns

Return type: string

If the user selects Cancel the function returns an empty vector, otherwise The function returns a string array of length 2.

|  |  |
| --- | --- |
| **Index** | **Description** |
| 0 | Flags value defining justification and property attributes |
| 1 | Pin name |

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_editpindialog) | | |
| [◄ EditObjectPropertiesDialog](func_editobjectpropertiesdialog.htm) |  | [EditPotDialog ▶](func_editpotdialog.htm) |
