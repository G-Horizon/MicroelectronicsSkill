# DialogDesigner Function

Simple dialog designer that generates an XML dialog definition. The dialog shows the dialog as a tree, where the user can drag and drop items in the tree, add groups and add tabs. A preview of the dialog is shown alongside.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty string>> | Initial XML definition |

#### Argument 1

This optional argument can contain a basic XML definition of the dialog. Note that XML nesting is not processed and all elements are added to the root of the tree.

### Returns

Return type: string

An XML file describing the dialog.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_dialogdesigner) | | |
| [◄ DestroyMutex](func_destroymutex.htm) |  | [diff ▶](func_diff.htm) |
