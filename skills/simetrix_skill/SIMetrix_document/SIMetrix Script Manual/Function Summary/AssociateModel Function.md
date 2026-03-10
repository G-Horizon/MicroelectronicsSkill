# AssociateModel Function

Special purpose function forms part of parts browser system. Function opens 'Associate Models' dialog box which allows user to associate electrical models with schematic symbols as well as be able to specify part categories and pin mapping. The function modifies the user catalog file (second argument. The return value is FALSE if the user cancels the box otherwise it returns TRUE. For full details on using this dialog box, refer to the "Device Library" chapter in the User's Manual.

The dialog box may be opened in one of two modes namely multiple and single. In multiple mode, a list of models and categories is displayed allowing the association of many devices together. In single mode, a single device name is provided as an argument and only that device may be associated.

To open in single mode, provide a two element string array to argument 4 with the first element set to the model to be associated and the second element set to 'single'. Otherwise the box will be opened in multiple mode in which the first element of argument 4 (if present) defines the initial selected device.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Catalog file (usually OUT.CAT) |
| 2 | string | Yes |  | User catalog file (usually USER.CAT) |
| 3 | string | No | <<empty>> | Command to execute to create symbol |
| 4 | string | No | <<empty>> | Options |

### Returns

Return type: Real

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_associatemodel) | | |
| [◄ asinh](func_asinh.htm) |  | [atan ▶](func_atan.htm) |
