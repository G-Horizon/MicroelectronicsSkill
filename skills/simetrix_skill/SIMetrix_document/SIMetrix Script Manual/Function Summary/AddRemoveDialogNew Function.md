# AddRemoveDialogNew Function

Opens a dialog box to allow user to select from a number of items. This function is identical to  [AddRemoveDialog](func_addremovedialog.htm)  except that the return value has an additional element to specify the number of selected items. This makes it possible for the selected items list to be empty.

### Arguments

No arguments

### Returns

Return type: string array

The first element of the result returns the number of items in the selected list which can be zero. This is followed by the items themselves. The return value will an empty vector if "Cancel" is selected.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_addremovedialognew) | | |
| [◄ AddRemoveDialog](func_addremovedialog.htm) |  | [AddSymbolFiles ▶](func_addsymbolfiles.htm) |
