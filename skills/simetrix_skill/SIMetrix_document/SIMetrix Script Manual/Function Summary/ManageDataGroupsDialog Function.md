# ManageDataGroupsDialog Function

Specialised function that opens the Manage Data Group dialog box. The box displays data group information in tabular form with each row representing a single group. The box allows editing of the information and also for groups to be deleted.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string array | Yes |  | List of data groups and associated information |

#### Argument 1

String array with each element comprising a semi-colon delimited list of items that describe a single group. The items are as follows:

|  |  |
| --- | --- |
| **Field** | **Description** |
| 0 | Group name |
| 1 | Group title |
| 2 | Analysis mode |
| 3 | Flags: a combination of 'current', 'global', 'keep' |

### Returns

Return type: string array

String array of the same length as argument 1. Each array element comprising a semi-colon delimited list of items as follows:

|  |  |
| --- | --- |
| **Field** | **Description** |
| 0 | Group name |
| 1 | Group title |
| 2 | Flags: a combination of 'current', 'global', 'keep' and 'delete' |

Items marked 'delete' were deleted by the user.

The function will return an empty vector if the **Cancel** button is clicked.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_managedatagroupsdialog) | | |
| [◄ makevec](func_makevec.htm) |  | [ManageMeasureDialog ▶](func_managemeasuredialog.htm) |
