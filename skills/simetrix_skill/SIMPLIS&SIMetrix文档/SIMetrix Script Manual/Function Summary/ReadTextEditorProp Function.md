# ReadTextEditorProp Function

Reads a text editor property. This will work for all text based editors.

### Arguments

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Number** | **Type** | **Compulsory** | **Default** | **Description** |
| 1 | string | Yes |  | Property name |
| 2 | string | No |  | Editor type |

#### Argument 1

Name of the property. Valid values are 'path', 'modified' and 'type'

#### Argument 2

Optional flag to specify the type of editor. Possible values are:

* LogicDefinitionEditor
* NetlistEditor
* ScriptEditor
* TextEditor
* VerilogAEditor
* VerilogHDLEditor

### Returns

Return type: string

The property value for the requested property.

|  |  |  |
| --- | --- | --- |
| [▲Function Summary▲](functionsummary.htm#functionsummary__func_readtexteditorprop) | | |
| [◄ ReadSpiceFile](func_readspicefile.htm) |  | [ReadTouchstone ▶](func_readtouchstone.htm) |
