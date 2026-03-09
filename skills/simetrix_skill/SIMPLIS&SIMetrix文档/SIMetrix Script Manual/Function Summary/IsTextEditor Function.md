# IsTextEditor Function

Returns true if selected editor is a text editor. By default the selected editor will be the currently highlighted editor. Alternately argument 1 can be passed a type of editor to test for.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | No | <<empty>> | Text editor type |

#### Argument 1

This can be used to search for a particular text editor type. Possible values are:

* LogicDefinitionEditor
* NetlistEditor
* ScriptEditor
* TextEditor
* VerilogAEditor
* VerilogHDLEditor

### Returns

Return type: boolean

True or false depending on whether the selected editor is a text editor.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_istexteditor) | | |
| [◄ IsStr](func_isstr.htm) |  | [IsTextEditorModified ▶](func_istexteditormodified.htm) |
