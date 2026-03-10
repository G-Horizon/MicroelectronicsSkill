# EditColour Command

Changes the spec for the named colour object. Named colour objects are simply option variables used to store colour information. This command will write the value to the variable in the form #rrggbb where rr, gg and bb are two digit hex values representing the magnitude of the red, green and blue components respectively.

```
EditColour <colour-name> <colour-spec>
```

### Parameters

|  |  |
| --- | --- |
| colour-name | Name of colour object. May be the name of a pre-v8 graph colour object. See notes. |
| colour-spec | Text string that defines the colour. The functions  [GetColourSpec](func_getcolourspec.htm)  and  [SelectColourDialog](func_selectcolourdialog.htm)  return colour spec values. A value in the form #rrggbb or the name of another colour object may also be entered. |

### Notes

Note that version 7.2 and earlier stored colour information differently and used different names. This command will still recognise the names of colour objects used for graphs and set the correct new colour object. Schematic colour objects used in version 7.2 and earlier are not supported. Refer to documentation on schematic styles in  [User's Manual/Schematic Editor/Styles](../../user_manual/topics/schematiceditor_styles.htm) .

|  |  |  |
| --- | --- | --- |
| [▲ Command Summary ▲](commandsummary.htm#commandsummary__com_editcolour) | | |
| [◄ Echo](com_echo.htm) |  | [EditCopy ▶](com_editcopy.htm) |
