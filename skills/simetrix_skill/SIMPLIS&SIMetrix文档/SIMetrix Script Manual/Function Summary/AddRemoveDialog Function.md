# AddRemoveDialog Function

Opens a dialog box to allow user to select from a number of items

This dialog box is used by the menu **File** > **Model Library** > **Add/Remove Models...** (horizontal style) and also by the schematic menu **View** > **Configure Toolbar...** (vertical style).

The function will display in the lower list box, all items found in both arguments 1 and arguments 2 with no duplicates. In the top list box, only the items found in argument 1 will be displayed. The user may freely move these items between the boxes. The function returns the contents of the top list box as an array of strings.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  |  |
| 2 | string array | Yes |  | All items available |
| 3 | string array | No | <<empty>> | Options |
| 4 | string | No | 'horizontal' | Box style |

#### Argument 1

Initial contents of selected list box

#### Argument 3

A string array of size up to four which may be used to specify a number of options. The first three are used for text messages and the fourth specifies a help topic to be called when the user presses the Help button. The help button will not be shown if the fourth element is empty or omitted.

#### Argument 4

Determines the style of the box. The default is 'horizontal' and with this style the two list boxes are on top of each other. If arg4 is set to 'vertical', the two list boxes will be arranged side by side.

### Returns

Return type: string array

The function returns the contents of the selected list or an empty vector if "Cancel" is selected. The function will also return an empty vector if there are no selected items and thus it is not possible to use this function to select no items at all. Instead use  [AddRemoveDialogNew](func_addremovedialognew.htm)  if it is necessary to be able to select no items.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addremovedialog) | | |
| [◄ AddPropertyDialog](func_addpropertydialog.htm) |  | [AddRemoveDialogNew ▶](func_addremovedialognew.htm) |
