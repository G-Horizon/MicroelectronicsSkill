# TemplateEditProperty Command

Edits the property of a schematic instance.

This command may only be executed in a template script. It records an instruction to edit an instance property but the instruction will not be actioned until the netlist operation has completed. So a subsequent call to TemplateGetPropValue, for example, will return the unedited value of the property.

Please see  [Schematic Template Scripts](applications_schematictemplatescripts.htm)  for more information. In other situations use the command  [Prop](com_prop.htm) .

```
TemplateEditProperty [/hidenew] <ref> <propname> <propvalue>
```

### Parameters

|  |  |
| --- | --- |
| /hidenew | Hide added property. Does not affect any property already present on the instance |
| ref | Component reference of instance to be edited. This would usually be the REF value passed to the template script. |
| propname | Name of property to be changed. |
| propvalue | New value for property |

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_templateeditproperty) | | |
| [◄ SwitchModelSection](com_switchmodelsection.htm) |  | [TemplateSetValue ▶](com_templatesetvalue.htm) |
