# TemplateSetValue Command

Sets the value that will be used for the specified device's template during the current netlist operation. Note that this command does not change the value of the TEMPLATE property stored on the instance itself.

This command may only be executed in a template script. Please see  [Schematic Template Scripts](applications_schematictemplatescripts.htm)  for more information.

```
TemplateSetValue <ref> <template-value>
```

### Parameters

|  |  |
| --- | --- |
| ref | Component reference of instance. This would usually be the REF value passed to the template script. |
| template-value | Template value. |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_templatesetvalue) | | |
| [◄ TemplateEditProperty](com_templateeditproperty.htm) |  | [TextEditorCommentLines ▶](com_texteditorcommentlines.htm) |
